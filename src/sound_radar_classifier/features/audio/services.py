from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sound_radar_classifier.features.audio.models import Microphone
from sound_radar_classifier.features.audio.schemas import MicrophoneCreate, MicrophoneUpdate


async def get_microphones(session: AsyncSession) -> list[Microphone]:
    result = await session.execute(select(Microphone))
    return list(result.scalars().all())


async def get_microphone(session: AsyncSession, microphone_id: int) -> Microphone | None:
    result = await session.execute(select(Microphone).where(Microphone.id == microphone_id))
    return result.scalar_one_or_none()


async def create_microphone(session: AsyncSession, data: MicrophoneCreate) -> Microphone:
    microphone = Microphone(**data.model_dump())
    session.add(microphone)
    await session.commit()
    await session.refresh(microphone)
    return microphone


async def update_microphone(session: AsyncSession, microphone_id: int, data: MicrophoneUpdate) -> Microphone | None:
    microphone = await get_microphone(session, microphone_id)
    if microphone is None:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(microphone, key, value)
    await session.commit()
    await session.refresh(microphone)
    return microphone


async def delete_microphone(session: AsyncSession, microphone_id: int) -> bool:
    microphone = await get_microphone(session, microphone_id)
    if microphone is None:
        return False
    await session.delete(microphone)
    await session.commit()
    return True
