# Architecture

## Overview

sound-radar-classifier is an acoustic localization system that uses Time Difference of Arrival (TDOA) to estimate sound source positions. It follows a feature-based architecture similar to blog-chat, where each major functionality is organized as a self-contained module.

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    FastAPI Backend                       │
├──────────────┬──────────────┬───────────────────────────┤
│    Audio     │ Localization │         Radar             │
│  (PyAudio)   │   (TDOA)     │    (WebSocket)             │
├──────────────┴──────────────┴───────────────────────────┤
│              SQLAlchemy Async ORM                        │
│              (SQLite / PostgreSQL)                      │
└─────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────┐
│                  Vite + TypeScript                      │
│    main.ts  │  radar.ts  │  settings.ts                 │
├─────────────────────────────────────────────────────────┤
│              HTMX for HTML-based interactivity          │
└─────────────────────────────────────────────────────────┘
```

## Backend Components

### Core Module (`src/sound_radar/core/`)

- **config.py** - Environment configuration (DATABASE_URL, AUDIO_SETTINGS, etc.)
- **database.py** - SQLAlchemy async engine setup, session management
- **responses.py** - Jinja2 template rendering helpers
- **base.py** - SQLAlchemy declarative base

### Features Module (`src/sound_radar/features/`)

Each feature is a self-contained module with its own routes, models, and services:

#### Audio (`features/audio/`)

- PyAudio capture from multiple microphones
- Audio buffer management
- Preprocessing (filter + gain)
- Event detection (RMS threshold)

#### Localization (`features/localization/`)

- TDOA engine using cross-correlation
- Position solver using nonlinear least squares
- Confidence scoring

#### Radar (`features/radar/`)

- WebSocket endpoint for real-time updates
- Circular radar with logarithmic scaling
- Sound tagging (name, color, emoji)

#### Settings (`features/settings/`)

- Microphone configuration (positions in 2D)
- System scale (meters)
- Detection sensitivity
- Speed of sound / temperature

## Frontend Architecture

### Build System (Vite)

Entry points defined in `vite.config.js`:

- `core/client/main.ts` - Theme initialization, HTMX setup
- `features/radar/client/radar.ts` - Radar visualization
- `features/settings/client/settings.ts` - Configuration UI

Output goes to `static/` directory.

### HTMX Integration

The frontend uses HTMX for server-side rendered interactivity:

- HTML responses from FastAPI include `hx-*` attributes
- HTMX handles AJAX requests and DOM swapping
- Reduces client-side JavaScript complexity

### WebSocket Radar Client

- Connects to `/ws/radar`
- Receives real-time sound event updates
- Renders HTML templates from server
- Updates radar visualization

## Data Flow

### Audio Detection Flow

1. PyAudio captures audio from multiple microphones
2. Audio buffer stores recent samples
3. Event detection checks RMS threshold
4. When event detected, pass to localization

### Localization Flow

1. Receive audio snippet from event detection
2. Perform cross-correlation between mic pairs
3. Calculate time differences (TDOA)
4. Solve hyperbolic equations for (x, y)
5. Return position with confidence score

### Radar Update Flow

1. Localization returns detected position
2. Apply sound classification (basic tagging)
3. Store event in database
4. Render radar point template
5. Broadcast via WebSocket to all clients
6. Each client updates radar visualization

## Database Schema

### Microphones Table

```
id: INTEGER PRIMARY KEY
name: VARCHAR(50)
position_x: FLOAT  (meters)
position_y: FLOAT (meters)
created_at: DATETIME
```

### Sound Events Table

```
id: INTEGER PRIMARY KEY
label: VARCHAR(50)
color: VARCHAR(20)
emoji: VARCHAR(10)
position_x: FLOAT
position_y: FLOAT
confidence: FLOAT (0-1)
timestamp: DATETIME
```

### Settings Table

```
id: INTEGER PRIMARY KEY
key: VARCHAR(50) UNIQUE
value: TEXT
```

## Configuration

### Environment Variables

| Variable     | Description                            | Required                 |
| ------------ | -------------------------------------- | ------------------------ |
| DATABASE_URL | SQLite or PostgreSQL connection string | Yes                      |
| AUDIO_DEVICE | Audio device index or name             | No (default: default)   |
| SAMPLE_RATE  | Audio sample rate (Hz)                 | No (default: 44100)     |
| CHUNK_SIZE   | Audio chunk size                       | No (default: 1024)       |

## Security

- CORS configured for localhost
- GZip compression for responses
- SQLAlchemy prevents SQL injection

## Performance Targets

- Total latency: < 100ms (target: < 50ms)
- Angular accuracy: ±5-10°
- Distance accuracy: ±10-20%
