from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "features" / "audio" / "templates"
CORE_TEMPLATES_DIR = BASE_DIR / "core" / "templates"

templates = Environment(
    loader=FileSystemLoader([TEMPLATES_DIR, CORE_TEMPLATES_DIR]),
    autoescape=True,
)


@router.get("/audio", response_class=HTMLResponse)
async def audio_index():
    template = templates.get_template("audio/index.html")
    return template.render(title="Audio", page_title="Audio")
