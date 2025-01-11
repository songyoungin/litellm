from litellm import completion
from litellm.types.utils import ModelResponse
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()


def test_get_sync_chat_completion_response() -> ModelResponse:
    """
    Test sync chat completion request

    Returns:
        ModelResponse: Response from completion
    """
    messages = [{"content": "Hello, how are you?", "role": "user"}]

    # openai call
    response = completion(model="openai/gpt-3.5-turbo-0125", messages=messages)
    return response


response = test_get_sync_chat_completion_response()
pprint(response)
