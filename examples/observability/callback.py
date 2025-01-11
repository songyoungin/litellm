from typing import Any, Dict
from litellm.types.utils import ModelResponse
import litellm

from loguru import logger
from dotenv import load_dotenv

load_dotenv()


def track_cost_callback(
    kwargs: Dict[str, Any],
    completion_response: ModelResponse,
    start_time: float,
    end_time: float,
) -> None:
    """
    Track cost callback

    Args:
        kwargs (Dict[str, Any]): kwargs to completion
        completion_response (ModelResponse): response from completion
        start_time (float): start time
        end_time (float): end time
    """
    try:
        response_cost = kwargs.get("response_cost", 0)

        logger.info(
            {
                "streaming response_cost": response_cost,
                "completion_response": completion_response,
                "start_time": start_time,
                "end_time": end_time,
            }
        )
    except Exception as e:
        logger.error(f"Error raised when tracking cost: {e}")


litellm.success_callback = [track_cost_callback]  # set custom callback function


def test_get_sync_chat_completion_response() -> ModelResponse:
    """
    Test sync chat completion request

    Returns:
        ModelResponse: Response from completion
    """
    messages = [{"content": "Hello, how are you?", "role": "user"}]
    response = litellm.completion(model="openai/gpt-3.5-turbo-0125", messages=messages)
    return response


response = test_get_sync_chat_completion_response()
logger.info(response)


# def test_get_streaming_chat_completion_response() -> None:
#     """
#     Test streaming chat completion request with callback

#     Returns:
#         None
#     """
#     messages = [{"content": "Hello, how are you?", "role": "user"}]
#     response = litellm.completion(model="openai/gpt-3.5-turbo-0125", messages=messages, stream=True)

#     for part in response:
#         logger.info(part)


# test_get_streaming_chat_completion_response()
