from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sound_radar_classifier.features.radar.models import SoundEvent
from sound_radar_classifier.features.radar.schemas import SoundEventCreate


async def get_sound_events(session: AsyncSession, limit: int = 100) -> list[SoundEvent]:
    result = await session.execute(select(SoundEvent).order_by(SoundEvent.timestamp.desc()).limit(limit))
    return list(result.scalars().all())


async def get_sound_event(session: AsyncSession, event_id: int) -> SoundEvent | None:
    result = await session.execute(select(SoundEvent).where(SoundEvent.id == event_id))
    return result.scalar_one_or_none()


async def create_sound_event(session: AsyncSession, data: SoundEventCreate) -> SoundEvent:
    event = SoundEvent(**data.model_dump())
    session.add(event)
    await session.commit()
    await session.refresh(event)
    return event
