import os
from typing import Any, Dict
import requests

from loguru import logger
from dotenv import load_dotenv

load_dotenv()


LITELLM_PROXY_URL = os.getenv("LITELLM_PROXY_URL", "http://localhost:4000")
LITELLM_MASTER_KEY = os.getenv("LITELLM_MASTER_KEY", "test")


def create_internal_user(
    username: str, user_email: str, user_role: str = "internal_user"
) -> None:
    """
    Create a new internal user with the given email and password using the proxy

    Args:
        username (str): The username of the user
        user_email (str): The email of the user
        user_role (str): The role of the user
    """
    response = requests.post(
        f"{LITELLM_PROXY_URL}/user/new",
        json={"user_alias": username, "user_email": user_email, "user_role": user_role},
        headers={"Authorization": f"Bearer {LITELLM_MASTER_KEY}"},
    )
    logger.info(
        f"User alias: {response.json()['user_alias']}, User ID: {response.json()['user_id']}, Created virtual key: {response.json()['key']}"
    )


def get_internal_users(role: str | None = None) -> Dict[str, Any]:
    """
    Get all internal users with the given role

    Args:
        role (str): The role of the users to get

    Returns:
        Dict[str, Any]: The response from the proxy
    """
    response = requests.get(
        f"{LITELLM_PROXY_URL}/user/list",
        params={"role": role},
        headers={"Authorization": f"Bearer {LITELLM_MASTER_KEY}"},
    )
    return response.json()


if __name__ == "__main__":
    create_internal_user(
        username="internal-user-viewer-1",
        user_email="internal-user-viewer-1@test.com",
        user_role="internal_user_viewer",
    )
    create_internal_user(
        username="internal-user-viewer-2",
        user_email="internal-user-viewer-2@test.com",
        user_role="internal_user_viewer",
    )

    create_internal_user(
        username="proxy-admin-1",
        user_email="proxy-admin-1@test.com",
        user_role="proxy_admin",
    )
    create_internal_user(
        username="proxy-admin-viewer-1",
        user_email="proxy-admin-viewer-1@test.com",
        user_role="proxy_admin_viewer",
    )

    all_users = get_internal_users()
    logger.info(f"All users: {all_users}")

    internal_user_viewer_users = get_internal_users(role="internal_user_viewer")
    logger.info(f"Internal user viewer users: {internal_user_viewer_users}")

    proxy_admins = get_internal_users(role="proxy_admin")
    logger.info(f"Proxy admins: {proxy_admins}")

    proxy_admin_viewers = get_internal_users(role="proxy_admin_viewer")
    logger.info(f"Proxy admin viewers: {proxy_admin_viewers}")
