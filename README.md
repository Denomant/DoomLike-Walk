# Doom-like Walking Game

## Table of Contents
1. [Project Overview](#Project-Overview)
2. [How to Run](#How-To-Run)
3. [Controls](#Controls)
4. [Technical Breakdown](#Technical-Breakdown)

## Project Overview
A Python & Pygame-based ray casting engine used to implement a walking simulator game, 
inspired by classic Doom-style movement and rendering.  
This project demonstrates real-time pseudo-3D rendering of a 2D environment, fully 
built from scratch, without relying on 3D libraries.

## How To Run
1. Ensure you have Python 3 and git installed.
2. Navigate to the project directory in your terminal.  
3. Clone the git repository:
   ```bash
   git clone https://github.com/Denomant/DoomLike-Walk.git
   ```
4. <b>Optionally create / activate a virtual environment:</b>
   ```bash
   python3 -m venv venv
   ```
   ```bash
   # On Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```
5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run the game:
   ```bash
   python run.py
   ```

## Controls
| Action | Key |  Alternative |
|--------|-----|--------------|
| Move Forward | W | ↑ | 
| Move Backward | S | ↓ |
| Turn Left | A | ← |
| Turn Right | D | → |
| Exit | ESC | On-screen `X` |

---

## Technical Breakdown

### <em>1. Code Architecture</em>
The project is split into several clean, self-contained modules:

| File | Responsibility |
|------|----------------|
| `run.py` | Game loop, variable tracking, event handling, map customization. |
| `Render.py` | Ray casting logic, wall shading, and drawing. |
| `Player.py` | Player movement, rotation, and collision detection. |

### <em>2. Ray Casting Logic (`Render.py`)</em>
- <b><em>Ray Creation</b></em>  
For each vertical 'slice' of the screen, a separate `Ray` object is cast with its
corresponding angle and starting point in mind.
- <b><em> Distance Calculation</b></em>  
Rays move forward in small 'steps' in the given angle from the given starting point
until they hit a wall (`#`) or exceed the view distance.
- <b><em> Visuals Calculations </b></em>  
Given the length of the Ray (distance to the wall) and using proportions, We compute
the following:  
  - Visible height = (<sup>distance to projection screen</sup>/<sub>
Ray length</sub>) × wall expected height at projection screen distance
  - <sup>shade</sup>/<sub>255</sub> = <sup>Ray length</sup>/
<sub>view distance</sub>
    - shade = 255 - <sup>(Ray length × 255)</sup>/<sub>view distance</sub>

### <em>3. Player System (`Player.py`)</em>
- Each `Player` object stores its own position (as a floating-point (y, x) tuple to 
simulate array indexation) and its current viewing angle (in degrees).
- Rotation is handled by the `turn_counterclockwise` method, which adds or 
subtracts from the current viewing angle, and then normalizes it to the 0-360 range.
- Movement is handled through a separate helper function `move_point_in_angle` 
that uses trigonometric calculations to determine the new expected position 
based on the right triangle formed by the movement (cos and -sin are used). Same
helper function is then used in ray casting to move rays forward in the given angle.
- `is_valid_point` can be used to prevent the new point from entering walls,
or getting outside the map boundaries.

### <em>4. Game Loop (`run.py`)</em>
- Timer-based movement and rotation makes it framerate independent, and ensures 
consistent movement speed across different hardware.
- `apply_key` adjusts the player's movement speed based on the keys pressed (KEYDOWN) and 
released (KEYUP) to ensure up-to-date movements at every timer tick.
- <b><em>Rendering pipeline</b></em>
  - Clear screen -> Render 3D views -> Draw UI elements
- Map and player starting position / angle can be customized by modifying the
`game_map` and `player` initialization variables at the top of the file.