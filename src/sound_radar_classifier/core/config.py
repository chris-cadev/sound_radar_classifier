import os
from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite+aiosqlite:///radar.db")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is required")
if not DATABASE_URL.startswith("sqlite+aiosqlite://") and not DATABASE_URL.startswith("postgresql+asyncpg://"):
    raise ValueError(
        "DATABASE_URL must be compatible with either SQLite or PostgreSQL (e.g., sqlite+aiosqlite:///radar.db or postgresql+asyncpg://user:password@localhost/dbname)"
    )

AUDIO_DEVICE = os.environ.get("AUDIO_DEVICE", "default")
SAMPLE_RATE = int(os.environ.get("SAMPLE_RATE", "44100"))
CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", "1024"))
