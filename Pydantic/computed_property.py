from pydantic import BaseModel, computed_field, Field
class Booking(BaseModel):
    user_id : int
    room_id : int
    nights : int = Field(..., ge = 1)
    rate : float
    @computed_field
    @property
    def total(idk) -> float:
        return idk.nights * idk.rate
book = Booking(user_id=12, room_id=34, nights=4, rate=122.0)
print(book.total)