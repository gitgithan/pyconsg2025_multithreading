# Abstract
Ever stared at a Python thread deadlock and thought, "But... why now?" 

This talk dives deep into one of Python’s sneakiest concurrency traps: a simple-looking ThreadPoolExecutor example from PEP 3148 that sometimes deadlocks—and sometimes doesn’t. 

We'll unravel the mystery behind its behavior by combining theory, real-world debugging, and practical strategies for making nondeterministic deadlocks reproducible and understandable.
Through hands-on walkthroughs, we'll use VS Code debugger and internal APIs to hunt down Heisenbugs, reveal shutdown timing races, and explore how thread shutdown interacts with future.result() and executor.submit.

Along the way, we'll explain blocking vs. non-blocking calls, thread lifecycle, Python’s shutdown hooks, and why importing modules like concurrent.futures.thread may just save your sanity.
Attendees will leave with a reusable debugging strategy for multithreaded Python, insight into deadlock timing, and mental models to reason about nested concurrency (even mixing ThreadPoolExecutor and ProcessPoolExecutor). 

Bonus: you'll learn how to intentionally cause deadlocks—because to fix them, you must first control them.


Audience: Intermediate to Advanced Python developers who've ever seen threading deadlocks, or who want to confidently debug multithreaded code using real tools and strategies

# Outline
1. Introducing the undeterministic function at https://peps.python.org/pep-3148/#threadpoolexecutor (2 min)
2. The situation explained: Who wins the race (5 min)
3. Using the debugger: Heisenbug appears (3min)
4. Unswallowing RuntimeError: Heisenbug strikes back (3min)
5. Two types of shutdown: Introducing with ThreadPoolExecutor (3min)
6. Discussing Solutions (3min)
7. Why Nested Concurrency (5 min)
8. QnA (6min)

# Key Takeaways
1. We can learn transferrable problem solving principles from unrealistic examples
2. OS Thread switching is undeterministic, seemingly reproducible behaviour may need multiple runs before seeing it's not the only case possible
3. Running VSCode debugger can change the timing and behaviour of programs
4. time.sleep() uses real world time, pausing too long before stepping during debugging would make time.sleep() not have it's intended effect
5. There are reasons to nest threadpoolexecutors/processpoolexecutors

# Pre-requisites
1. Understands concept of blocking vs non-blocking code
2. Understands concept of locking to protect resource in shared memory during multithreading (threading.Lock)
3. Understands how VSCode debugger works, how to set breakpoints and step
4. Willingness to dive into source code

# Speaker Bio
Han Qi is a full-time Data Scientist who first got into tech in 2017, then pivoted into the AI/Data space in 2019 through self-study.

He has a deep curiosity for questioning assumptions, a knack for spotting inconsistencies, and a love for diving into how things work.
He writes technical articles to fill the gaps he wishes someone had covered when he was learning, aiming to equip others with critical problem-solving skills and hard-won insights. 

He lives by the Boy Scout Rule: leave things better than you found them—especially for those facing the same challenges.
Every now and then, he teaches at programming bootcamps to stay grounded in the struggles of being self-taught—and to inspire others from non-CS backgrounds that with effort and passion, they too can thrive in the rich, ever-evolving world of tech.

In his free time, he enjoys singing, playing piano, badminton, and watching talent shows.

# Past Speaking Experience
- First Time on stage on any paid conference
- 3 years teaching data science bootcamp to 100+ adults in Le Wagon in informal setting.
- Delivered 2 hour session alone in AIESEC conference during university to inspire audience to run for executive position.
- Designed and delivered 20 x 2hour personal development classes to romanian teenagers during university. (Profile at Page 12, row 3, col 5: https://issuu.com/scoaladevalori/docs/raport_anual_grow_2013)
- Performed songs on stage more than 10 times 
- Joined toastmasters in University, completed 3/10 in "first 10 speeches" series.

# Links to past talks/slides
No past examples of talks/slides.
Aim to go through all related talks around the world in past 10 years to fill experience gap.

Collection of video links: https://vigorous-freeze-7ed.notion.site/Youtube-Links-1c876fd8e60980d2a79be2735e239481?pvs=4

Have various medium articles to show how i explain both technical and non-technical things so you can understand my tone/style

1. Long winding journey to the destination of creating a recursion visualizer: https://medium.com/p/cb08103b54fe
2. Inspiring others to challenge themselves: https://medium.com/data-science/20-days-to-google-cloud-professional-machine-learning-engineer-exam-beta-b48909499942?sk=d7b9b9b21f897e510d67cea124ace7d6
3. Leaving no stone unturned in explanation: https://medium.com/data-science/cherry-pickup-bottom-up-explanation-ecc14487db05?sk=79af94d5a9f1b68d78d4c11ab5a26606
4. Noticing edge cases: https://medium.com/towards-artificial-intelligence/understanding-pickle-to-make-decorators-work-with-multiprocessing-b28c212da9b5
5. Comprehensive coverage of patterns: https://medium.com/p/6724d439ede0