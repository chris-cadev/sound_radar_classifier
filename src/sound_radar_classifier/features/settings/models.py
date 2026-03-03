from datetime import datetime
from sqlalchemy import Integer, Float, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sound_radar_classifier.core.base import Base


class SystemSettings(Base):
    __tablename__ = "system_settings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, default=1)
    detection_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    speed_of_sound: Mapped[float] = mapped_column(Float, nullable=False)
    temperature: Mapped[float] = mapped_column(Float, nullable=False)
    max_range: Mapped[float] = mapped_column(Float, nullable=False)
    logarithmic_scale: Mapped[bool] = mapped_column(Boolean, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now)
