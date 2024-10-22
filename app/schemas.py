from pydantic import BaseModel
from typing import List, Optional

class ReviewBase(BaseModel):
    rating: float
    text: str
    reviewer_name: str
    review_date: str

class Product(BaseModel):
    id: int
    brand: str
    model: str
    price: float
    specifications: Optional[str] = None
    image_url: Optional[str] = None
    reviews: List[ReviewBase] = []

    class Config:
        orm_mode = True
