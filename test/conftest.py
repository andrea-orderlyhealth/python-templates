import pytest

from src.user import UserServiceFactory

factory = UserServiceFactory.create_factory({})


@pytest.fixture(scope="session")
def user_service():
    return factory.create_service()
