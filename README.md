# Zero Squares
### By: Rony Mansour



---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/rony-e-mansour/zero-squares.git
   
   cd zero-squares
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the game:
    ```bash
    python main.py
    ```
---

## Project Overview

Zero Squares is a Python-based game designed by me -Rony Mansour- for Intelligent Search Algorithms course at DU. 

---

## Project Structure

The project is organized into several files:

- `cell.py`: Cell class
- `state.py`: State class
- `algo.py`: Contains algorithm implementations
- `game_logic.py`: Implements main game logic
- `levels.py`: Contains the representation of several phases as two-dimensional arrays
- `main.py`: Contains drawing functions and user input control

---

## Guid
in the begin of `main.py` there is three value you can change:
- `algo`: manual, BFS, or DFS
- `time_between_moves`: Increase this value to increase the time between movements (in millisecond)
- `chosen_level`: chose a level to play (from level1 to level20)