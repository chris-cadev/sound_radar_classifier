# Setup Guide

## Prerequisites

- Python 3.12+
- Node.js & Bun (for frontend build)
- PyAudio compatible audio input device
- PostgreSQL (optional, for production)

## Hardware Requirements

- Minimum 2 microphones (3 recommended for distance estimation)
- Microphones should be synchronized (I2S recommended)
- USB audio interface recommended for multiple mics

## Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd sound-radar-classifier

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Environment Variables

Create a `.env` file in the project root:

```bash
# Copy from example
cp example.env .env

# Edit .env with your values
DATABASE_URL=sqlite+aiosqlite:///radar.db
AUDIO_DEVICE=default
SAMPLE_RATE=44100
CHUNK_SIZE=1024
```

For production with PostgreSQL:
```bash
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
```

### 3. Verify Audio Device

List available audio devices:

```bash
python -c "import pyaudio; p = pyaudio.PyAudio(); [print(f'{i}: {p.get_device_info(i)}') for i in range(p.get_device_count())]"
```

### 4. Run Development Server

```bash
# Using PDM (recommended)
pdm start

# Or using FastAPI directly
fastapi dev src/sound_radar/app.py
```

The app will be available at `http://localhost:8000`

### 5. Frontend Development (Optional)

For live-reload frontend development:

```bash
# Using Bun (recommended)
bun run watch

# Or using Vite directly
npx vite
```

## Available Commands

| Command | Description |
|---------|-------------|
| `pdm start` | Run development server |
| `pdm prod` | Run production server on port 9091 |
| `pdm test` | Run tests with coverage |
| `pdm watch` | Watch mode for frontend |
| `bun run build` | Build frontend assets |

## Project Scripts (package.json)

```bash
# Build frontend
bun run build

# Watch mode
bun run watch
```

## Testing

```bash
# Run all tests
pdm test

# Or directly with pytest
pytest -v
```

## Building for Production

### 1. Build Frontend

```bash
bun run build
```

This outputs to `static/` directory.

### 2. Build Docker Container

```bash
docker build -t sound-radar .
docker run -p 9091:9091 --device /dev/snd sound-radar
```

Note: `--device /dev/snd` is needed for audio access.

### 3. Using Docker Compose

```bash
docker-compose up -d
```

## Database

### SQLite (Development)

Default database is `radar.db` (SQLite). Created automatically on first run.

### PostgreSQL (Production)

Set `DATABASE_URL` to PostgreSQL connection string:
```
postgresql+asyncpg://username:password@localhost/databasename
```

## Project Structure Reference

```
sound-radar-classifier/
├── src/sound_radar/           # Python source code
│   ├── app.py                # FastAPI application
│   ├── core/                 # Core utilities
│   │   ├── config.py         # Configuration
│   │   ├── database.py       # Database setup
│   │   └── responses.py      # Template rendering
│   └── features/             # Feature modules
│       ├── audio/             # Audio capture and processing
│       ├── localization/     # TDOA engine and position solver
│       ├── radar/            # Radar visualization
│       └── settings/         # User configuration
├── static/                    # Built frontend assets
├── docs/product/              # This documentation
├── tests/                     # Test suite
├── vite.config.js            # Vite build config
└── pyproject.toml            # Python project config
```

## Audio Configuration

### Microphone Setup

1. Go to Settings page
2. Add microphones with (x, y) coordinates in meters
3. Example for equilateral triangle:
   - Mic 1: (0, 0)
   - Mic 2: (1.0, 0)
   - Mic 3: (0.5, 0.866)

### Detection Settings

Adjust in Settings panel:
- **Threshold**: RMS energy level to trigger detection
- **Min Duration**: Minimum sound duration (e.g., 20ms)
- **Max Range**: Maximum detection distance in meters

## Troubleshooting

### Audio Device Not Found

1. Check `python -c "import pyaudio; print(pyaudio.get_device_count())"`
2. Verify device is not busy (another application using it)
3. Try running with sudo (Linux may need permissions)

### Database Errors

1. Check `DATABASE_URL` is set correctly
2. Ensure the database file/directory is writable
3. Try deleting `radar.db` to recreate

### Import Errors

1. Ensure you're in the virtual environment
2. Run `pip install -r requirements.txt` again

### Frontend Not Loading

1. Run `bun run build` to generate static files
2. Check `static/` directory has files
3. Ensure `/static` mount point works in app

### WebSocket Connection Failed

1. Check browser console for errors
2. Ensure server is running
3. Verify WebSocket endpoint is accessible

### Poor Localization Accuracy

1. Verify microphone positions are accurate
2. Ensure microphones are synchronized
3. Reduce ambient noise
4. Check speed of sound setting (or temperature)

## Development Workflow

1. Start backend: `pdm start`
2. Start frontend watch: `bun run watch` (optional)
3. Make changes to code
4. Run tests: `pdm test`
5. Build frontend: `bun run build` (before commit)

## Known Issues

- Microphone clock drift can affect accuracy
- USB microphones may desynchronize
- Echo and reflections cause false detections
- Multiple simultaneous sources may not be resolved accurately

For mitigation, see [Architecture](architecture.md).
