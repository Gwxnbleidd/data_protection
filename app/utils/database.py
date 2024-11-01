import json
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
    active: bool = True
    restrictions: bool = True

class Database():
    def init(self) -> None:
        pass

    def read(self, filename: str = 'database.txt') -> dict[str, User]:
        try:
            with open(file=filename, mode='r') as file:
                database = json.load(file)
                return database
        except FileNotFoundError:
            return {}

    def add_user(self, user_data: User, filename: str = 'database.txt'):
        db = self.read()
        
        if db.get(user_data.username):
            raise Exception('Пользователь с таким именем уже существует')
        
        db[user_data.username] = user_data.model_dump()

        with open(file=filename, mode='w') as file:
            json.dump(db, file, indent=4)
        
    def find_user(self, username: str) -> User:
        db = self.read()

        if user_data := db.get(username):
            return User(**user_data)
        raise Exception('Пользователь не найден')
    
    def change_password(self, username: str, new_password: str, filename: str = 'database.txt'):
        db = self.read()

        db[username]['password'] = new_password

        with open(file=filename, mode='w') as file:
            json.dump(db, file, indent=4)
    
    def change_active_user(self, username: str, active: bool, filename: str = 'database.txt'):
        db = self.read()

        db[username]['active'] = active

        with open(file=filename, mode='w') as file:
            json.dump(db, file, indent=4)
    
    def change_restriction_user(self, username: str, restrictions: bool, filename: str = 'database.txt'):
        db = self.read()

        db[username]['restrictions'] = restrictions

        with open(file=filename, mode='w') as file:
            json.dump(db, file, indent=4)    
    
    def drop(self, filename: str = 'database.txt'):
        db = self.read()

        db.clear()

        with open(file=filename, mode='w') as file:
            json.dump(db, file, indent=4)