# Project Roadmap

This roadmap outlines the development phases for the Sound Radar Classifier project.

## Phase 1: Foundation

**Goal:** Set up the basic project structure and ensure everything compiles.

- [x] Create `pyproject.toml` with all dependencies
- [x] Create `src/sound_radar_classifier/app.py` - FastAPI application entry point
- [x] Create `src/sound_radar_classifier/core/config.py` - Configuration management
- [x] Create `src/sound_radar_classifier/core/database.py` - SQLAlchemy setup
- [x] Create `src/sound_radar_classifier/core/base.py` - Declarative base
- [x] Create `src/sound_radar_classifier/core/responses.py` - Jinja2 template setup
- [x] Set up `vite.config.js` and `package.json` for frontend
- [x] Verify `fastapi dev src/sound_radar_classifier/app.py` runs

**Checkpoints:**
- App starts without errors
- Static files are served
- Database connection works

---

## Phase 2: Data Layer

**Goal:** Create database models and settings infrastructure.

- [x] Create `src/sound_radar_classifier/features/audio/__init__.py`
- [x] Create `src/sound_radar_classifier/features/audio/models.py` - Microphone model
- [x] Create `src/sound_radar_classifier/features/radar/__init__.py`
- [x] Create `src/sound_radar_classifier/features/radar/models.py` - SoundEvent model
- [x] Create `src/sound_radar_classifier/features/settings/__init__.py`
- [x] Create `src/sound_radar_classifier/features/settings/models.py` - Settings model
- [x] Run database migrations to create tables
- [x] Verify models can be created/queried

**Checkpoints:**
- Database tables created
- Can add/retrieve microphones
- Can add/retrieve settings

---

## Phase 3: Audio Capture

**Goal:** Capture audio from microphones.

- [ ] Create `src/sound_radar_classifier/features/audio/capture.py` - PyAudio wrapper
- [ ] Create `src/sound_radar_classifier/features/audio/buffer.py` - Ring buffer
- [ ] Add audio device selection to settings
- [ ] Create audio capture routes/settings API
- [ ] Verify audio stream starts

**Checkpoints:**
- Can list audio devices
- Audio capture starts without errors
- Buffer accumulates samples

---

## Phase 4: Event Detection

**Goal:** Detect when sound events occur.

- [ ] Create `src/sound_radar_classifier/features/audio/detection.py`
- [ ] Implement RMS energy calculation
- [ ] Implement threshold detection
- [ ] Add minimum duration filter
- [ ] Emit events when detected

**Checkpoints:**
- Detection triggers on loud sounds
- No false positives on silence
- Event objects created correctly

---

## Phase 5: TDOA Engine

**Goal:** Calculate time differences between microphones.

- [ ] Create `src/sound_radar_classifier/features/localization/__init__.py`
- [ ] Create `src/sound_radar_classifier/features/localization/models.py`
- [ ] Create `src/sound_radar_classifier/features/localization/tdoa.py`
- [ ] Implement cross-correlation
- [ ] Return time delays for mic pairs

**Checkpoints:**
- TDOA produces reasonable delays
- Works with different mic configurations

---

## Phase 6: Position Solver

**Goal:** Convert TDOA to (x, y) coordinates.

- [ ] Create `src/sound_radar_classifier/features/localization/solver.py`
- [ ] Implement nonlinear least squares
- [ ] Handle edge cases (no solution)
- [ ] Return confidence score

**Checkpoints:**
- Solves for position correctly
- Confidence reflects quality
- Handles 2-mic (direction only) vs 3-mic (distance too)

---

## Phase 7: Radar WebSocket

**Goal:** Real-time updates to frontend.

- [ ] Create `src/sound_radar_classifier/features/radar/websocket.py` - ConnectionManager
- [ ] Create `src/sound_radar_classifier/features/radar/routes.py` - `/ws/radar` endpoint
- [ ] Integrate with event detection
- [ ] Broadcast detected events

**Checkpoints:**
- WebSocket connects
- Events broadcast to all clients

---

## Phase 8: Frontend Radar

**Goal:** Display radar visualization in browser.

- [ ] Create `src/sound_radar_classifier/features/radar/templates/radar.html`
- [ ] Create `src/sound_radar_classifier/core/client/main.ts` - HTMX setup
- [ ] Create `src/sound_radar_classifier/features/radar/client/radar.ts` - Canvas rendering
- [ ] Implement circular radar grid
- [ ] Implement logarithmic distance scaling
- [ ] Handle WebSocket messages and update canvas

**Checkpoints:**
- Radar displays on page
- Points appear when events detected
- Logarithmic scaling visible

---

## Phase 9: Settings UI

**Goal:** Configure microphones and system parameters.

- [ ] Create `src/sound_radar_classifier/features/settings/templates/settings.html`
- [ ] Create microphone position input form
- [ ] Add settings controls (threshold, sensitivity, etc.)
- [ ] Persist settings to database
- [ ] Display microphone positions on radar

**Checkpoints:**
- Can add/edit/remove microphones
- Settings persist across restarts
- Mic positions visible on radar

---

## Phase 10: Sound Tagging

**Goal:** Assign metadata to detected sounds.

- [ ] Create `src/sound_radar_classifier/features/radar/tags.py`
- [ ] Define default tags (Voice, Clap, Engine, Unknown)
- [ ] Implement tag assignment
- [ ] Display tags with colors/emojis on radar

**Checkpoints:**
- Tags assigned to events
- Colors and emojis display correctly

---

## Phase 11: Polish & Optimization

**Goal:** Refine and optimize.

- [ ] Add confidence indicator (opacity)
- [ ] Improve latency (< 100ms target)
- [ ] Write unit tests
- [ ] Add Docker support
- [ ] Handle edge cases gracefully
- [ ] Document any remaining issues

**Checkpoints:**
- All tests pass
- Docker builds successfully
- Latency meets target

---

## Suggested Order

```
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6
                              ↓
Phase 7 ← Phase 10 ← Phase 9 ← Phase 8
                ↓
          Phase 11
```

**Rationale:**
- Foundation first (1-2)
- Core audio pipeline (3-6)
- Frontend visualization (7-9)
- Finishing touches (10-11)
