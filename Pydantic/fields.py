from pydantic import BaseModel, Field
class User(BaseModel):
    id : int
    age : int = Field(
        ..., ge = 0, le = 100
    )
    name : str = Field(
        ..., min_length = 2, max_length = 50, description = "Name of the User"
    )
user1 = {'id' : 20, 'age' : 34, 'name' : "Sam"}
userr = User(**user1)
print(userr)