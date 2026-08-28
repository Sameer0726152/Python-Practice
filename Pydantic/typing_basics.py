from pydantic import BaseModel
from typing import List, Dict, Optional
class Cart(BaseModel):
    id : int
    items : List[str]
    quantities : Dict[str, int]
class Post(BaseModel):
    title : str
    content : str
    img_url : Optional[str] = None