from pydantic import BaseModel
class Address(BaseModel):
    city : str
    postal_code : str

class User(BaseModel):
    name : str
    age : int
    location : Address

user1 = User(name = 'Sam', age = 19, location = {'city' : 'Pune', 'postal_code' : '411018'})
print(user1)