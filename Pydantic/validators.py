from pydantic import BaseModel, field_validator, model_validator
class User(BaseModel):
    name : str
    @field_validator('name')
    def name_len(cls, v):
        if len(v) < 4:
            raise ValueError("Name is too small")
        return v
class SignUp(BaseModel):
    real_pass : str
    con_pass : str
    @model_validator(mode = 'after')
    def match(cls, values):
        if values.real_pass != values.con_pass:
            raise ValueError("PassWords dont match")
        return values

user = {'name' : 'Sameer'}
sign = {'real_pass' : 'idkbro', 'con_pass' : 'idkbro'}
u1 = User(**user)
s1 = SignUp(**sign)
print(u1)
print(s1)
