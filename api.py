from pydantic import BaseModel


class RestaurantResponseAll(BaseModel):
    pass


class RestaurantResponseItem(BaseModel):
    id: int
    name: str
    description: str
    image: str
    rating: int
    lat: float
    lon: float