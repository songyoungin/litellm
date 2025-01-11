from litellm import CustomStreamWrapper, acompletion
from dotenv import load_dotenv
from pprint import pprint
import asyncio

from litellm.types.utils import ModelResponse

load_dotenv()


async def test_get_async_chat_completion_response() -> (
    ModelResponse | CustomStreamWrapper
):
    """
    Test async chat completion request

    Returns:
        ModelResponse | CustomStreamWrapper: Response from completion
    """
    user_message = "Hello, how are you?"
    messages = [{"content": user_message, "role": "user"}]
    response = await acompletion(model="openai/gpt-3.5-turbo-0125", messages=messages)
    return response


response = asyncio.run(test_get_async_chat_completion_response())
pprint(response)
