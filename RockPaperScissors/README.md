# 🪨📄✂️ Rock Paper Scissors

Play the classic Rock, Paper, Scissors game against the computer! Features fun emoji representations and continuous gameplay.

## Features

- **Play Against Computer**: Computer makes random choices for fair gameplay
- **Visual Symbols**: Fun emoji representations for each choice
  - 🪨 Rock (r)
  - 🔖 Paper (p)  
  - ✂️ Scissors (s)
- **Input Validation**: Ensures valid choices only
- **Continuous Play**: Option to play multiple rounds
- **Clear Results**: Shows both player and computer choices with winner announcement

## How to Play

1. Run the game:
   ```bash
   python app.py
   ```

2. Choose your option by entering:
   - `r` for Rock 🪨
   - `p` for Paper 🔖
   - `s` for Scissors ✂️

3. See the computer's choice and find out who wins!

4. Choose to continue playing or exit

## Game Rules

- **Rock** beats **Scissors**
- **Scissors** beats **Paper**
- **Paper** beats **Rock**
- Same choices result in a **Tie**

## Sample Gameplay

```
Please Select your choice (r/p/s) : r
You selected:  🪨
Computer selected : ✂️
Congratulations! You Won
Do you want to continue playing? (Yes/No) : yes

Please Select your choice (r/p/s) : p
You selected:  🔖
Computer selected : ✂️
Sorry, You lost!
Do you want to continue playing? (Yes/No) : no
```

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: Built-in `random` module only
- **File**: `app.py`

## Game Logic

- Computer uses `random.choice()` for fair selection
- Input validation prevents invalid choices
- Win conditions checked with logical operators
- Continuous play loop with exit option

## Input Options

- `r` or `R` → Rock
- `p` or `P` → Paper
- `s` or `S` → Scissors
- `yes`/`no` for continue playing

Ready to challenge the computer? May the best player win! 🏆 