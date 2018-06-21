import numpy as np
import asyncio
import pytest
import aiotf

@pytest.mark.asyncio
async def test_client_connection():
  async with aiotf.AsyncTensorflowServing('localhost:9000') as client:
    x = np.random.rand(10, 391, 21)
    predictions = await client.predict('model', x)