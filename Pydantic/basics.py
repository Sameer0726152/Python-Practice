from pydantic import BaseModel
class User(BaseModel):
    id : int
    name : str
    active : bool
input = {'id' : 12, 'name' : "Sam", 'active' : True}
user = User(**input)
print(user)