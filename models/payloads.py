from pydantic import BaseModel, Field, HttpUrl
from typing import List


class Location(BaseModel):
    lat: float
    lng: float


class CreatePlacePayload(BaseModel):
    location: Location
    accuracy: int
    name: str
    phone_number: str
    address: str
    types: List[str]
    website: HttpUrl
    language: str


class UpdatePlacePayload(BaseModel):
    place_id: str
    address: str
    key: str


class DeletePlacePayload(BaseModel):
    place_id: str
