# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A Streamlit number guessing game where the player picks a difficulty, gets a range, and tries to guess the secret number within a limited number of attempts. Hints guide the player higher or lower after each guess.

- [x] **Bugs found:**
  1. Hints were backwards — guessing too high said "Go HIGHER!" and too low said "Go LOWER!"
  2. Hard mode had a smaller range (1-50) than Normal (1-100), making it easier
  3. The info text always said "between 1 and 100" regardless of difficulty
  4. On even attempts, the secret was cast to a string, causing broken comparisons
  5. "New Game" reset attempts to 0 instead of 1 (off-by-one) and used a hardcoded range

- [x] **Fixes applied:**
  1. Swapped hint messages so "Too High" says "Go LOWER!" and vice versa
  2. Changed Hard mode range to 1-200
  3. Replaced hardcoded text with dynamic `{low}` and `{high}` values
  4. Removed the `str()` cast — secret is always compared as an int now
  5. Fixed New Game to reset attempts to 1 and use `randint(low, high)`
  6. Refactored all game logic into `logic_utils.py` and added 4 regression tests

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]
      ![alt text](<Screenshot 2026-03-16 at 2.50.35 AM.png>)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
