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

- Every time you interact with the app, Streamlit reruns the whole script from top to bottom, so normal variables reset. `st.session_state` is how you keep things like the secret number and score alive between reruns. Without it, the game was resetting itself on every click.

---

## 5. Looking ahead: your developer habits

- Writing tests after fixing a bug is something I want to keep doing. It's easy to think a fix works just because the app looks fine, but having a pytest case that specifically targets the bug means I'll know immediately if it breaks again. I also liked committing after each logical step instead of dumping everything at the end.

- Next time I'd double-check AI suggestions before accepting them, especially around framework-specific behavior. The "Press Enter" thing taught me that the AI can sound confident about how Streamlit works but still get the details wrong. Running the app myself was what actually cleared it up.

- AI-generated code can look clean and complete but still be full of subtle bugs. This project showed me that you can't just trust it — you have to play with it, read through it, and test it yourself.
