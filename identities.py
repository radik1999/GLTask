class User:
    def __init__(self, email: str):
        self.email = email


class Role:
    def __init__(self, name):
        self.name = name


class Binding:
    def __init__(self, user: User, role: Role):
        self.user = user
        self.role = role

    def __str__(self):
        return f"{self.user.email} - {self.role.name}"
