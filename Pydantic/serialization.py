from pydantic import BaseModel
class Address(BaseModel):
    city : str
    postal_code : str

class User(BaseModel):
    name : str
    id : int
    address : Address

user1 = User(name = "Sam", id = 90, address = {'city' : "Pune", 'postal_code' : '4444'})
print(user1)
print("=" * 30)
print(user1.model_dump()) #converts to dictionary
print("=" * 30)
print(user1.model_dump_json()) #converts to json