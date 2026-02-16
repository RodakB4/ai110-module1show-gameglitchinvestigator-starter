# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. When I first ran the game I realized when I submited a number the hints were backwards. It would say lower when it should've been higher and then says higher when it should've said lower as well as the fact the secret number changed.
  2. When I input an even number it tries to convert it to a string and then that string is compared to the secret number which leads to a type error. 
  3. Once the game is over and I click "new game" the history in the developers debug info doesn't reset and the game doesn't start a new it simply changed the Secret word in the developers side. 
  4. At the 7th attempt it tells me I've finished all my and gives me what the actual number was despite the fact I still have one more attempt left.
  5. I have to click submit twice for it to actually register my submision.
  6. It is unclear how the scorring is meant to work and doesn't actualy update acurately when comparing what's on the developers score and what's actually seen by the user.
  7. There's an easy, normal and hard mode but the normal mode is harder than the hard mode when it should be reversed.
  8. I keep needing to click the submit button twice just to enter a number in when it should only happen once.
  9. If I am midway through a game and decide to switch modes before finishing the game doesn't reset to a new game but still continues the one I was playing.
  

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used the claude chat bot with the "Ask before edits" mode to help make sure I knew what changes were being made as well as what it understood I wanted changed.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude was quickly able to see the problem with the logic for higher and lower being flipped and was able to give a good solution to fix the problem by simply swapping them out.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Initially as I mentioned earlier there was a problem with the way the "Out of attempts" was being shown before I had completely run out of attempts and in an effort to fix it problems arised. Initially it had made the correct suggestion on how to fix it as the attempts being made weren't all consistent throughout the code and once that change was made it seemed to have worked. Later on though when I was revising the history that was being shown in the developers tab I switched it's postion so that it would update with the numbers being submitted and not before and that messed up with the attempts being shown on top. So when the mistake about "Out of attempts" arrived a step to early again I thought that was the problem and asked it to hone in on this set of problems although it was able to come up with suggestions it wasn't the root off the issue which led to bad code. It was only until I ran another manual test and noticed the number in the dev tab and UI screen were different (they had initially been the same when i took 1 attempt it would say I have 7 left) this made me realize it was simply a display issue and not a logic issue and once I pointed it out it was quickly able to make that fix.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I mainly decided by doing manual tests even though I did a few py tests, although ineficient manual tests felt more reliable to actually play the game for myself than do seperate logic tests. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tested the hint logic once I made the changes by going back to the game running it and seeing if inputing a number below the secret would tell me if it's too low or not.
- Did AI help you design or understand any tests? How?
Yes. A test it helped me understand was one where I did a py test for the "normal difficulty" the idea was to simulate a full game without actually running one and it was done so that it could check the status, the attempts left and the score to actuarely show what it should be like in each of those outcomes as in a manual test there might be some things I miss. 


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Since streamlit ran the entire app from top to bottom each time the user interacted with the page this made it so that the Secret would change.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain it as a sort of shop and the "Secret" as an item in the store with no labels and each time you pick up this item from this shelf the price changes by the time you bring it to the counter and so to make sure these things dont change st.session_state acts as this label printed on these items stating how much the price is. 

- What change did you make that finally gave the game a stable secret number?

By putting a condition
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)
Each time "secret" didn't have this label then it was free to change it's number. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  In future labs I'd like to continue using things like #codebase and #file as it helped hone in on what it is I wanted to be looked at and what changes needed to be made.

- What is one thing you would do differently next time you work with AI on a coding task?
I would like to make sure I remember that despite the face it has access to all of our code that doesn't necessarily mean it's looking at everything at the same time all at once and that it will focus on whatever direction you've pointed it to so your own limitation off understanding will limit what the AI can do.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I see it as a helping hand and something that can very much streamline the process but it's not something that can simply do it all it's as best as it's user. 
