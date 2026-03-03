from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sound_radar_classifier.features.settings.models import SystemSettings
from sound_radar_classifier.core.config import (
    DETECTION_THRESHOLD,
    SPEED_OF_SOUND,
    TEMPERATURE,
    MAX_RANGE,
    LOGARITHMIC_SCALE,
)


async def seed_default_settings(session: AsyncSession) -> SystemSettings:
    result = await session.execute(select(SystemSettings).where(SystemSettings.id == 1))
    settings = result.scalar_one_or_none()

    if settings is None:
        settings = SystemSettings(
            id=1,
            detection_threshold=DETECTION_THRESHOLD,
            speed_of_sound=SPEED_OF_SOUND,
            temperature=TEMPERATURE,
            max_range=MAX_RANGE,
            logarithmic_scale=LOGARITHMIC_SCALE,
        )
        session.add(settings)
        await session.commit()
        await session.refresh(settings)

    return settings


async def get_settings(session: AsyncSession) -> SystemSettings:
    result = await session.execute(select(SystemSettings).where(SystemSettings.id == 1))
    settings = result.scalar_one_or_none()
    if settings is None:
        settings = await seed_default_settings(session)
    return settings


async def update_settings(session: AsyncSession, **kwargs) -> SystemSettings:
    settings = await get_settings(session)
    for key, value in kwargs.items():
        if value is not None and hasattr(settings, key):
            setattr(settings, key, value)
    await session.commit()
    await session.refresh(settings)
    return settings
