# 🔢 Number Guessing Game

A classic number guessing game where you try to guess a randomly generated number between 1 and 100. The game provides helpful feedback to guide you to the correct answer!

## Features

- **Random Number Generation**: Computer generates a random number between 1 and 100
- **Intelligent Feedback**: Get "Too High" or "Too Low" hints after each guess
- **Input Validation**: Handles invalid input gracefully with error messages
- **Continuous Play**: Keep guessing until you find the right number
- **Victory Celebration**: Special message when you guess correctly

## How to Play

1. Run the game:
   ```bash
   python app.py
   ```

2. The computer will secretly choose a random number between 1 and 100

3. Enter your guess when prompted

4. Use the feedback ("Too High" or "Too Low") to adjust your next guess

5. Keep guessing until you find the correct number!

## Sample Gameplay

```
Guess the number between 1 and 100: 50
Too High, Guess Again
Guess the number between 1 and 100: 25
Too Low, Guess Again
Guess the number between 1 and 100: 35
Congratulations, You guessed the number!
```

## Strategy Tips

- Start with 50 (middle of the range)
- Use binary search strategy - narrow down the range with each guess
- Pay attention to the feedback to eliminate impossible numbers

## Technical Details

- **Language**: Python 3.x
- **Dependencies**: Built-in `random` module only
- **File**: `app.py`
- **Input Validation**: Handles non-numeric input with try-catch blocks

## Game Logic

- Uses `random.randint(1, 100)` for number generation
- Infinite loop until correct guess
- Exception handling for invalid input
- Simple comparison logic for feedback

Good luck with your guessing! 🎯 