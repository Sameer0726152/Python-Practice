from pydantic import BaseModel, field_validator, model_validator
class User(BaseModel):
    first_name : str
    last_name : str
    @field_validator('first_name')
    def name_len(cls, v):
        if len(v) < 4:
            raise ValueError("First Name is too small")
        return v
    @field_validator('first_name', 'last_name')
    def name_title(cls, v):
        if not v.istitle():
            raise ValueError("Names must be capitalised")
        return v
class SignUp(BaseModel):
    real_pass : str
    con_pass : str
    @model_validator(mode = 'after')
    def match(cls, values):
        if values.real_pass != values.con_pass:
            raise ValueError("PassWords dont match")
        return values

class emails(BaseModel):
    email : str
    @field_validator('email')
    def normalize(cls, v):
        return v.lower().strip()

class Product(BaseModel):
    price : float
    @field_validator('price', mode = 'before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', '').replace(',', '.'))
        return v


user = {'first_name' : 'Sameer', 'last_name' : 'Talekar'}
sign = {'real_pass' : 'idkbro', 'con_pass' : 'idkbro'}
u1 = User(**user)
s1 = SignUp(**sign)
e1 = emails(email = "    SamWr@gmIl.com  ")
p1 = Product(price = "$44,44")
print(u1)
print(s1)
print(e1)
print(p1)