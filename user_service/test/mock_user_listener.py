from typing import List

<<<<<<< HEAD:user_service/test/mock_user_listener.py
from user_service.abstract_user import UserListener, User
=======
from user_service.src import UserListener, User
>>>>>>> b2aebacabf109b4538dc93c30f260b765902ac00:test/mock_user_listener.py


class MockUserListener(UserListener):

    users_created: List[User] = []
    users_removed: List[User] = []

    def user_created(self, user: User) -> None:
        self.users_created.append(user)

    def user_removed(self, user: User) -> None:
        self.users_removed.append(user)
