<h1 align="center">aiotf</h1>

<div align="center">
  <strong>Asyncio-based <code>Tensorflow Serving</code> Prediction</strong>
</div>

<br />

<div align="center">
  <!-- Build Status -->
  <a href="https://travis-ci.org/brunoalano/aiotf">
    <img src="https://img.shields.io/travis/brunoalano/aiotf/master.svg?style=flat-square"
      alt="Build Status" />
  </a>

  <!-- Test Coverage -->
  <a href="https://codecov.io/github/brunoalano/aiotf">
    <img src="https://img.shields.io/codecov/c/github/brunoalano/aiotf/master.svg?style=flat-square"
      alt="Test Coverage" />
  </a>

  <!-- Downloads !-->
  <a href="http://pepy.tech/badge/aiotf">
    <img src="http://pepy.tech/badge/aiotf"
      alt="Downloads" />
  </a>
</div>

## Features
- __asyncio:__ better use of your cpu idle time
- __pep8 compliant:__ following best code standards
- __high-performance prediction:__ we use `aio-grpc`

## Example
```python
import aiotf

async def make_prediction(model_name: str, data):
  async with aiotf.AsyncTensorflowServing('localhost:9000') as client:
    predictions = await client.predict(model_name, data)
```
You can find more examples in the `examples/` subdirectory.


## Installation
```sh
$ pip install aiotf
```

## License
[MIT](https://tldrlegal.com/license/mit-license)
