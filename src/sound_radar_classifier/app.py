from sound_radar_classifier.features.radar.routes import router as radar_router
from sound_radar_classifier.features.audio.routes import router as audio_router
from sound_radar_classifier.features.settings.routes import router as settings_router
from contextlib import asynccontextmanager
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from fastapi import FastAPI
from sound_radar_classifier.core.database import init_db


@asynccontextmanager
async def lifespan(_: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["localhost"],
    allow_methods=["GET", "POST"],
)
app.add_middleware(GZipMiddleware, minimum_size=500)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(radar_router)
app.include_router(audio_router)
app.include_router(settings_router)
