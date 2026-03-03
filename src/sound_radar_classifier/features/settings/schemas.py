from datetime import datetime
from pydantic import BaseModel


class SystemSettingsBase(BaseModel):
    detection_threshold: float
    speed_of_sound: float
    temperature: float
    max_range: float
    logarithmic_scale: bool


class SystemSettingsCreate(SystemSettingsBase):
    pass


class SystemSettingsUpdate(BaseModel):
    detection_threshold: float | None = None
    speed_of_sound: float | None = None
    temperature: float | None = None
    max_range: float | None = None
    logarithmic_scale: bool | None = None


class SystemSettings(SystemSettingsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
