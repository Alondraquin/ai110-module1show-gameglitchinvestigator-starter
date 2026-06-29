# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  The game looked like a decent guessing game. I gives the user to change the difficulty of the guessing game and allows to see the history. hTe game also gives the user to start anew game or to have the option to give hints.

- List at least two concrete bugs you noticed at the start 
One bug that I noticed first was that the hints were lying and directing me to the wrong number. The second bug I noticed was that the game wouldnt let me start a new game after I used all of my guesses. In order for me to continue a new game I had to refresh my screen.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  20   | the hint should have told me to go higher| The hint told me to go lower eventhough the answer was 28 | LOWER | 
|New game | the game should have started from the beginin again and let me put in new guesses | The game was stuck on game over and didnt let me put in any new guesses | GAME OVER |
| History | It was supposed to show me my past attempts |The game would delay showing the most recent guess|None|


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
The AI that I used during the project was Claude. I also used gemini as my helper during this project
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I asked my Ai helper why the game kept on leading me away from the number with its hints. It responded with that the output logic when the game compares the guess to the secret number was wrong. Instead of guiding the user to go lower if they put a high number thay would make the user go higher and vise versa.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). I asked my Ai helper the logic of storing the guessing history in the game. It told me that the the history was bieng appended to a list and that was it.However when I went to the app code I saw that I just needed to move the debug block affter the session state histroy is written. 


## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
