# Task Documentation

This file details each task in the project, explaining what it is, why it matters, and where to start working on it.

---

## Project Setup

**Priority:** High

**What:** Set up the basic project structure with FastAPI, SQLAlchemy, and HTMX frontend.

**Why:** Foundation for all other tasks.

**Where to start:**
- Create `pyproject.toml` with dependencies
- Create `src/sound_radar/app.py` - FastAPI application setup
- Create `src/sound_radar/core/` module with config, database, responses
- Set up `vite.config.js` and frontend structure

**Related files:**
- `pyproject.toml` - Python dependencies
- `src/sound_radar/app.py` - Main application
- `vite.config.js` - Frontend build config

---

## Audio Capture Module

**Priority:** High

**What:** Capture audio from multiple microphones using PyAudio.

**Why:** Core input for the entire system.

**Where to start:**
- Create `features/audio/capture.py` - PyAudio wrapper
- Create `features/audio/buffer.py` - Ring buffer for audio samples
- Implement multi-device capture
- Handle sample rate and chunk size configuration

**Related files:**
- `features/audio/__init__.py`
- `features/audio/capture.py`
- `features/audio/models.py`

---

## Audio Preprocessing

**Priority:** High

**What:** Apply filtering and gain to audio before event detection.

**Why:** Improves detection accuracy and handles different volume levels.

**Where to start:**
- Create `features/audio/preprocessing.py`
- Implement bandpass filter
- Implement automatic gain control (AGC)
- Make preprocessing configurable

**Related files:**
- `features/audio/preprocessing.py`
- `core/config.py` - Audio settings

---

## Sound Event Detection

**Priority:** High

**What:** Detect when a sound event occurs based on RMS energy threshold.

**Why:** Identifies when to run localization.

**Where to start:**
- Create `features/audio/detection.py`
- Implement RMS energy calculation
- Implement threshold detection
- Add minimum duration filtering (e.g., 20ms)
- Emit events when detected

**Related files:**
- `features/audio/detection.py`
- `features/audio/models.py` - Event model

---

## TDOA Engine

**Priority:** High

**What:** Calculate Time Difference of Arrival using cross-correlation.

**Why:** Core algorithm for determining sound direction.

**Where to start:**
- Create `features/localization/tdoa.py`
- Implement cross-correlation between mic pairs
- Handle phase alignment
- Return time delays for each mic pair

**Related files:**
- `features/localization/tdoa.py`
- `features/localization/models.py`

---

## Position Solver

**Priority:** High

**What:** Solve hyperbolic equations to convert TDOA to (x, y) position.

**Why:** Converts time delays to spatial coordinates.

**Where to start:**
- Create `features/localization/solver.py`
- Implement nonlinear least squares solver
- Use scipy.optimize for optimization
- Handle edge cases (no solution possible)
- Return confidence score

**Related files:**
- `features/localization/solver.py`
- `features/localization/models.py` - Position model

---

## Sound Tagging System

**Priority:** Medium

**What:** Assign metadata (label, color, emoji) to detected sounds.

**Why:** Provides visual distinction on radar.

**Where to start:**
- Create `features/radar/tags.py`
- Define default tags (Voice, Clap, Engine, Unknown)
- Implement tag assignment logic
- Allow custom tag configuration

**Related files:**
- `features/radar/tags.py`
- `features/radar/models.py`

---

## Radar WebSocket API

**Priority:** High

**What:** Real-time WebSocket endpoint for radar updates.

**Why:** Enables live radar visualization in browser.

**Where to start:**
- Create `features/radar/routes.py`
- Implement `/ws/radar` endpoint
- Create `ConnectionManager` for broadcasting
- Define JSON message format for events

**Related files:**
- `features/radar/routes.py`
- `features/radar/websocket.py`

---

## Radar Frontend Visualization

**Priority:** High

**What:** Display circular radar with detected sound events.

**Why:** User-facing component for the system.

**Where to start:**
- Create `features/radar/client/radar.ts`
- Implement canvas-based radar drawing
- Implement logarithmic distance scaling
- Handle WebSocket updates
- Display microphone positions

**Related files:**
- `features/radar/client/radar.ts`
- `features/radar/templates/radar.html`

---

## Microphone Configuration UI

**Priority:** High

**What:** User interface to configure microphone positions.

**Why:** Required for TDOA calculations.

**Where to start:**
- Create `features/settings/routes.py`
- Create `features/settings/templates/settings.html`
- Implement position input (x, y coordinates)
- Validate minimum 2 microphones
- Store in database

**Related files:**
- `features/settings/routes.py`
- `features/settings/templates/settings.html`

---

## Settings Panel

**Priority:** Medium

**What:** Settings panel for system configuration.

**Why:** Allows user to tune system behavior.

**Where to start:**
- Create `features/settings/templates/settings.html`
- Add configuration options:
  - Microphone coordinates
  - Speed of sound (or temperature)
  - Detection sensitivity
  - Max range
  - Log scale toggle
- Persist settings to database

**Related files:**
- `features/settings/routes.py`
- `features/settings/templates/settings.html`

---

## Database Models

**Priority:** High

**What:** SQLAlchemy models for persistence.

**Why:** Stores configuration and event history.

**Where to start:**
- Create `core/base.py` - Declarative base
- Create `features/audio/models.py` - Microphone model
- Create `features/radar/models.py` - SoundEvent model
- Create `features/settings/models.py` - Settings model

**Related files:**
- `core/base.py`
- `features/*/models.py`

---

## Frontend Build System

**Priority:** High

**What:** Set up Vite + TypeScript for frontend build.

**Why:** Required for HTMX and radar visualization.

**Where to start:**
- Create `vite.config.js`
- Create `package.json`
- Set up TypeScript configuration
- Configure output to `static/` directory

**Related files:**
- `vite.config.js`
- `package.json`
- `tsconfig.json`

---

## HTMX Integration

**Priority:** Medium

**What:** Server-side rendered UI with HTMX for interactivity.

**Why:** Reduces client-side complexity.

**Where to start:**
- Set up Jinja2 templates
- Add HTMX script to base template
- Create components with `hx-*` attributes
- Test partial page updates

**Related files:**
- `core/responses.py`
- `features/*/templates/*.html`

---

## Confidence Indicator

**Priority:** Low

**What:** Visual opacity scaled by confidence score.

**Why:** Helps users assess detection reliability.

**Where to start:**
- Pass confidence from solver to template
- Apply CSS opacity based on confidence value
- Low confidence → semi-transparent dot

**Related files:**
- `features/localization/solver.py`
- `features/radar/templates/radar.html`

---

## Multiple Sound Sources

**Priority:** Low

**What:** Handle multiple simultaneous sound sources (best-effort).

**Why:** Real-world scenarios often have multiple sounds.

**Where to start:**
- Modify detection to find multiple peaks
- Handle overlapping events in solver
- Consider source separation techniques

**Related files:**
- `features/audio/detection.py`
- `features/localization/solver.py`

---

## Docker Support

**Priority:** Medium

**What:** Containerize the application with Docker.

**Why:** Easy deployment.

**Where to start:**
- Create `Dockerfile`
- Create `docker-compose.yml`
- Handle audio device access in container

**Related files:**
- `Dockerfile`
- `docker-compose.yml`

---

## Testing

**Priority:** Medium

**What:** Write tests for core functionality.

**Why:** Ensures reliability.

**Where to start:**
- Set up pytest with pytest-asyncio
- Write unit tests for TDOA engine
- Write unit tests for position solver
- Test WebSocket endpoints

**Related files:**
- `tests/` directory
- `pyproject.toml` - test config

---

## Performance Optimization

**Priority:** Low

**What:** Optimize for latency targets (< 100ms, ideally < 50ms).

**Why:** Real-time requirements.

**Where to start:**
- Profile audio processing pipeline
- Optimize cross-correlation
- Consider Cython/Numba for hot paths
- Monitor end-to-end latency

**Related files:**
- `features/audio/` - all files
- `features/localization/` - all files
