from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR = BASE_DIR / "features" / "radar" / "templates"
CORE_TEMPLATES_DIR = BASE_DIR / "core" / "templates"

templates = Environment(
    loader=FileSystemLoader([TEMPLATES_DIR, CORE_TEMPLATES_DIR]),
    autoescape=True,
)


@router.get("/", response_class=HTMLResponse)
async def radar_index():
    template = templates.get_template("radar/index.html")
    return template.render(title="Radar", page_title="Radar")
