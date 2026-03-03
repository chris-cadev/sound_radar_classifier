from jinja2 import Environment, FileSystemLoader
from pathlib import Path


def create_templates(template_dir: str) -> Environment:
    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True,
    )
    return env
