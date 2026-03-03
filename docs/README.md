# Sound Radar Classifier - Documentation

Welcome to the sound-radar-classifier documentation. This project implements an acoustic localization system using TDOA (Time Difference of Arrival) with a FastAPI backend and HTMX frontend.

## Quick Links

- [Architecture Overview](architecture.md) - System design and component breakdown
- [Task Details](tasks.md) - Detailed breakdown of all project tasks
- [Setup Guide](setup.md) - How to run the project locally
- [Roadmap](roadmap.md) - Project roadmap and milestones
- [PRD](PRD.md) - Product requirements document
- [Collaboration](collaboration.md) - How to contribute

## What is Sound Radar Classifier?

A near real-time acoustic localization system that:

- Detects acoustic events (any sound source)
- Estimates direction and distance using multi-microphone TDOA
- Displays detected sources on a circular logarithmic radar
- Tags detected sounds with name, color, and emoji

## Tech Stack

- **Backend:** FastAPI + SQLAlchemy async
- **Frontend:** Vanilla TypeScript + Vite + HTMX
- **Real-time:** WebSockets for radar updates
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Audio:** PyAudio for microphone input

## Project Structure

```
sound-radar-classifier/
├── src/sound_radar/           # Python source code
│   ├── app.py                # FastAPI application
│   ├── core/                 # Core utilities
│   │   ├── config.py         # Configuration
│   │   ├── database.py       # Database setup
│   │   └── responses.py      # Template rendering
│   └── features/             # Feature modules
│       ├── audio/            # Audio capture and processing
│       ├── localization/    # TDOA engine and position solver
│       ├── radar/            # Radar visualization
│       └── settings/         # User configuration
├── static/                   # Built frontend assets
├── docs/product/             # This documentation
└── pyproject.toml            # Python project config
```

For more details, see [Architecture](architecture.md).
