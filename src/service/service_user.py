from src.models.store import Store
from src.models.user import User


class ServiceUser:
    def __init__(self):
        self.store = Store()

    def add_user(self, name, job):
        if not isinstance(name, str) or not isinstance(job, str):
            return "Invalid parameters"

        if not name or not job:
            return "Empty parameters not allowed"

        for stored_user in self.store.bd:
            if stored_user.name == name:
                return "User already exists"

        user = User(name, job)
        self.store.bd.append(user)
        return "User added"

    def remove_user(self, name, job):
        if not isinstance(name, str) or not isinstance(job, str):
            return "Invalid parameters"

        if not name or not job:
            return "Empty parameters not allowed"

        for stored_user in self.store.bd:
            if stored_user.name == name:
                self.store.bd.remove(stored_user)
                return "User removed"

        return "User does not exist"
