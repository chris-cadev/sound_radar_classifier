from datetime import datetime
from pydantic import BaseModel


class MicrophoneBase(BaseModel):
    __slots__ = ("name", "x_position", "y_position",
                 "device_index", "is_active")
    name: str
    x_position: float
    y_position: float
    device_index: int | None = None
    is_active: bool = True


class MicrophoneCreate(MicrophoneBase):
    pass


class MicrophoneUpdate(BaseModel):
    __slots__ = ("name", "x_position", "y_position",
                 "device_index", "is_active")
    name: str | None = None
    x_position: float | None = None
    y_position: float | None = None
    device_index: int | None = None
    is_active: bool | None = None


class Microphone(MicrophoneBase):
    __slots__ = ("id", "created_at", "updated_at")
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
