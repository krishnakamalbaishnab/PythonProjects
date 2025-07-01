# 🎲 Dice Rolling Game

An interactive dice rolling game that allows you to roll multiple dice and keeps track of your rolling statistics during the session.

## Features

- **Customizable Dice Count**: Choose how many dice you want to roll (1 or more)
- **Session Tracking**: Keeps count of how many times you've rolled during the current session
- **Interactive Gameplay**: Simple Y/N prompts for continuous play
- **Random Results**: Uses Python's random module for fair dice rolls

## How to Play

1. Run the game:
   ```bash
   python app.py
   ```

2. Choose whether you want to play (Y/N)

3. If yes, specify how many dice you want to roll

4. View your dice results and session statistics

5. Continue playing or exit as desired

## Sample Output

```
Do you want to play a Dice Rolling Game? Select One :- (Y/N): y
How many dice would you like to roll? 3
You rolled: 4, 2, 6
Total rolls in this session: 1
Do you want to play a Dice Rolling Game? Select One :- (Y/N): n
Thank you for playing! You rolled the dice 1 times. Goodbye!
```

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: Built-in `random` module only
- **File**: `app.py`

## Game Logic

- Each die generates a random number between 1 and 6
- The program validates user input for the number of dice
- Session counter increments with each roll
- Clean exit with session summary

Enjoy rolling the dice! 🎲 