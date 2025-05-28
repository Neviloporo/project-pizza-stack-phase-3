class User:
    _id_counter = 1
    _users = []

    def __init__(self, name, email):
        self.id = User._id_counter
        self.name = name
        self.email = email
        User._id_counter += 1
        User._users.append(self)


    def __repr__(self):
        return f"<User {self.id}: {self.name} ({self.email})>"
    
    
    def create_user(cls, name, email):
        if any (user.email == email for user in cls._users):
            raise ValueError("User with this email already exists.")
        return cls(name, email)
    
    def get_user_by_id(cls, user_id):
        return next ((user for user in cls._users.id == user_id), None)
    
    def get_user_by_email(cls, email):
        return next ((user for user in cls._users if user.email == email), None)
    
    def list_users(cls):
        return cls._users.copy()