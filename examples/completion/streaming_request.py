from litellm import completion
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()


def test_get_streaming_chat_completion_response() -> None:
    """
    Test streaming chat completion request

    Returns:
        None
    """
    messages = [{"content": "Hello, how are you?", "role": "user"}]
    response = completion(
        model="openai/gpt-3.5-turbo-0125", messages=messages, stream=True
    )

    for part in response:
        pprint(part)


test_get_streaming_chat_completion_response()
