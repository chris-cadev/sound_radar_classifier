# 📄 Product Requirements Document (PRD)

# Product Name

**Acoustic Radar – Basic Localization System**

---

# 1. Purpose

Develop a near real-time acoustic localization system that:

1. Detects acoustic events (any sound source)
2. Estimates direction and distance using multi-microphone TDOA
3. Displays detected sources on a circular logarithmic radar
4. Tags detected sounds with:
   - Name
   - Color
   - Emoji / symbol

User configures only:

- Microphone positions (x, y)
- System scale (meters)

---

# 2. Product Scope

## Included (Phase 1)

- 2D localization (x, y)
- Real-time detection (<100 ms target latency)
- Circular radar UI
- Logarithmic distance scaling
- Manual sound category tagging
- Configurable mic geometry

## Excluded (Phase 1)

- 3D elevation
- AI-heavy sound classification
- Cloud storage
- Historical replay system

---

# 3. System Architecture Overview

```
Microphones
     ↓
Audio Buffer
     ↓
Preprocessing (Filter + Gain)
     ↓
Event Detection
     ↓
TDOA Engine
     ↓
Position Solver (x, y)
     ↓
Sound Classification (basic)
     ↓
Radar Renderer
```

---

# 4. Functional Requirements

---

## 4.1 Microphone Configuration

### Requirement

User must be able to define microphone layout in 2D space.

### Inputs

Example:

```
Mic 1: (0, 0)
Mic 2: (1.0, 0)
Mic 3: (0.5, 0.866)
```

### Constraints

- Minimum 2 microphones required
- 3 microphones recommended for distance estimation
- Coordinates in meters
- System calculates inter-microphone distances internally

---

## 4.2 Sound Event Detection

### Requirement

System detects sound events above threshold.

### Method

- RMS energy threshold
- Optional frequency band selection
- Minimum duration threshold (e.g., 20 ms)

### Output

When event detected:

```
Event ID
Timestamp
Audio snippet buffer
```

Latency target: < 30 ms

---

## 4.3 Localization Engine (Core)

### Method

Time Difference of Arrival (TDOA)

For each mic pair:

Δt = time delay from cross-correlation

Using speed of sound:

v = 343 m/s (configurable for temperature)

Solve hyperbolic equations:

For mic pair i,j:

√((x-xi)²+(y-yi)²) - √((x-xj)²+(y-yj)²) = v \* Δtij

Use nonlinear least squares solver.

### Output

```
x, y position (meters)
Confidence score (0–1)
```

Latency target: < 10 ms

---

## 4.4 Radar Visualization

### Layout

- Circular radar
- Center = microphone array centroid
- 360° display
- Configurable max radius (e.g., 50m)

---

## 4.5 Logarithmic Distance Scaling

### Requirement

Distance must be displayed logarithmically.

### Mapping

Let:

r_real = actual distance (meters)
R_max = maximum detection range
R_screen = radar radius in pixels

Use:

r_display = R_screen \* log(1 + r_real) / log(1 + R_max)

This allows:

- Near sounds spaced apart visually
- Far sounds compressed toward edge

---

## 4.6 Sound Tagging System

System assigns metadata to detected events.

### Each Tag Includes

- Label (e.g., "Clap", "Car", "Voice", "Unknown")
- Color
- Emoji or Symbol

### Example

| Type    | Color  | Emoji |
| ------- | ------ | ----- |
| Voice   | Blue   | 🗣    |
| Clap    | Yellow | 👏    |
| Engine  | Red    | 🚗    |
| Unknown | Gray   | ●     |

Tag is attached to radar point.

---

## 4.7 Confidence Indicator

Each detection must include:

- Confidence score from TDOA solver
- Visual opacity scaled by confidence

Low confidence → semi-transparent dot

---

# 5. Non-Functional Requirements

---

## 5.1 Latency

Total system latency target:

< 100 ms

Stretch goal:
< 50 ms

---

## 5.2 Accuracy

Target (with 3 mics spaced 1 m apart):

- Angular accuracy: ±5–10°
- Distance accuracy: ±10–20% (environment dependent)

---

## 5.3 Environmental Tolerance

Must handle:

- Moderate echo
- Wind noise
- Multiple simultaneous sources (best-effort)

---

# 6. User Interface Requirements

---

## Main Screen Must Show

- Circular radar grid
- Logarithmic rings
- Microphone positions
- Real-time plotted sound events
- Tag label + emoji
- Distance in meters
- Angle in degrees

---

## Settings Panel

User can configure:

- Microphone coordinates
- Speed of sound (or temperature)
- Detection sensitivity
- Max range
- Log scale toggle

---

# 7. Technical Stack (Suggested)

### Prototype

- Python
- NumPy / SciPy
- PyAudio
- Matplotlib / PyQt

### Production

- C++ or Rust DSP core
- OpenGL or WebGL radar rendering
- Embedded Linux or Jetson

---

# 8. Risks

- Microphone clock drift
- Echo interference
- USB mic desynchronization
- Multi-path reflections

Mitigation:

- Use synchronized I2S microphones
- Add confidence scoring
- Apply filtering

---

# 9. Definition of Done

System is complete when:

- User configures mic positions
- Makes a sound
- Sees a colored tagged point appear on radar
- Position updates in near real-time
- System remains stable for 1 hour continuous use
