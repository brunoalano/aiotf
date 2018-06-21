import numpy as np
from aiogrpc import insecure_channel
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2
from tensorflow.contrib.util import make_tensor_proto

class AsyncTensorflowServing(object):
  def __init__(self, endpoint: str):
    self.endpoint = endpoint
    self._channel = None

  async def __aenter__(self):
    self._channel = insecure_channel(self.endpoint)
    self._stub = prediction_service_pb2.beta_create_PredictionService_stub(self._channel)
    return self

  async def __aexit__(self, exc_type, exc, tb):
    await self._channel.close()

  async def predict(self, model_name: str, values,
                    signature_name: str = 'serving_default',
                    input_name: str = 'input',
                    timeout: float = 60.0,
                    dtype: np.dtype = None):
    # We first convert value to a numpy array or scalar.
    if isinstance(values, (np.ndarray, np.generic)):
      if dtype:
        nparray = values.astype(dtype)
      else:
        # python/numpy default float type is float64. We prefer float32 instead.
        if (values.dtype == np.float64) and dtype is None:
          values = values.astype(np.float32)

        # python/numpy default int type is int64. We prefer int32 instead.
        elif (values.dtype == np.int64) and dtype is None:
          downcasted_array = values.astype(np.int32)

          # Do not down cast if it leads to precision loss.
          if np.array_equal(downcasted_array, values):
            values = downcasted_array
    elif callable(getattr(values, "__array__", None)) or isinstance(
        getattr(values, "__array_interface__", None), dict):
      # If a class has the __array__ method, or __array_interface__ dict, then it
      # is possible to convert to numpy array.
      if dtype:
        values = np.asarray(values, dtype=dtype)
      else:
        values = np.asarray(values, dtype=np.float32)
    else:
      if values is None:
        raise ValueError("None values not supported.")

    request = predict_pb2.PredictRequest()
    request.model_spec.name = model_name
    request.model_spec.signature_name = signature_name
    request.inputs[input_name].CopyFrom(make_tensor_proto(values))
    return self._stub.Predict(request, timeout)