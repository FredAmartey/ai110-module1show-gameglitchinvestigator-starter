# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
   (for example: "the hints were backwards").
  "Press enter to apply" didn't work
  The hint told me to go higher when the answer was lower
  Hint told me to go higher than the range bounds

---

## 2. How did you use AI as a teammate?

- I used Claude Code in the terminal for most of this project.

- **Correct suggestion:** I told Claude Code the hints were backwards and it pulled up `check_guess()` and pointed out that when your guess is too high, the message says "Go HIGHER!" which makes no sense. That was exactly right — I could see it in the code on lines 38-41. After it swapped the messages, I ran pytest and the hint direction tests passed. Pretty straightforward once you see it.

- **Misleading suggestion:** I mentioned "Press enter to apply" wasn't working and Claude Code said there was no logic to handle Enter at all. That's not quite right though. Streamlit actually does rerun when you press Enter, it just doesn't trigger the `if submit:` block because that's tied to the button. So Enter does _something_, it just doesn't process your guess. I figured this out by running the app and watching what happened — pressing Enter changed the input but nothing happened until I clicked the button.

---

## 3. Debugging and testing your fixes

- Mostly I ran pytest after each fix. If the tests passed, the fix worked. I also opened the app a few times to make sure things looked right visually, like checking that the range displayed correctly for each difficulty.

- I ran `pytest tests/test_game_logic.py -v` and got 7 passing tests. The one that stood out was `test_hint_direction_when_too_high` — it guesses 75 when the secret is 50 and checks that the message says "LOWER." Before the fix that would've said "HIGHER" which is wrong.

- Claude Code wrote all four regression tests for me. I told it what bugs I found and it turned each one into a test case. That was actually useful because it made me think about what "fixed" really means — like the string comparison bug, I wouldn't have thought to test passing a string as the secret, but that's what the old code was doing on even attempts.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
