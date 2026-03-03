from datetime import datetime
from pydantic import BaseModel


class SoundEventBase(BaseModel):
    x_position: float
    y_position: float
    confidence: float


class SoundEventCreate(SoundEventBase):
    pass


class SoundEvent(SoundEventBase):
    id: int
    timestamp: datetime
    created_at: datetime

    class Config:
        from_attributes = True
