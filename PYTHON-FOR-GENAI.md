# Python for GenAI Engineering — A Beginner's Tutorial

This teaches you the Python you need to build GenAI things (RAG, agents, evals), starting
from zero. No prior programming knowledge assumed. Every example runs.

> **You've been using AI to write your code. This doc is the upgrade.**
> Getting AI to *generate* code is easy. The leap to being an *engineer* is being able to
> **read** that code, **understand** why it works, **debug** it when it breaks, and **know
> when the AI is wrong**. That's what this teaches. After this, AI becomes a power tool in
> your hands instead of a black box you copy-paste from.

**How to read this:** don't just read — open a terminal, type `python3`, and *type every
example yourself*. Change a value, re-run it, see what happens. Your fingers learn what your
eyes skip.

---

# Part 0 — The absolute basics (5 minutes)

**What is a program?** A text file of instructions the computer runs top to bottom.

**Running code two ways:**
- **The REPL** (interactive): type `python3` in your terminal. You get a `>>>` prompt.
  Type one line, hit enter, see the result instantly. Great for experimenting.
- **A script**: save lines in a file `hello.py`, run `python3 hello.py`. Great for real work.

```python
print("hello")        # print() shows something on screen. Output: hello
# this is a comment — Python ignores anything after #. Comments are notes for humans.
```

**The golden rule of Python:** **indentation (spaces at the start of a line) is meaningful.**
Lines indented the same amount belong together as a "block." Use **4 spaces** per level.
Never mix tabs and spaces — that's the #1 beginner error.

---

# Part 1 — Setup (do this once)

Your project needs an isolated space for its add-on libraries so projects don't clash. We
use **uv** (a fast, modern Python package/environment manager) instead of plain `pip`.

```bash
uv venv                        # create a "virtual environment" — a private box for this project
source .venv/bin/activate      # step into the box. Your prompt now shows (.venv)
uv pip install numpy requests  # install libraries INTO this box only
python my_script.py            # run your code
deactivate                     # step out of the box when done
```

- **library / package** = code someone else wrote that you install and use (e.g. `numpy`).
- **uv** = the tool that creates the virtual environment and installs libraries into it —
  a faster, modern replacement for `pip`/`venv` used separately.
- **venv** = the private box. Always work inside one. If you skip it, libraries from
  different projects fight each other and things break mysteriously.

---

# Part 2 — TIER 1: the essentials (learn before Lesson 3's hands-on exercise)

## 2.1 Variables — named boxes that hold a value

```python
device_id = 1234          # a whole number (called an "int")
job_name = "batch-runner"  # text (a "string" / str) — always in quotes
healthy = True             # yes/no value (a "bool") — True or False
ratio = 95.4                # a decimal number (a "float")
nothing = None              # "no value / empty" — Python's word for nothing
```

A variable is just a name pointing at a value. You can change it anytime:
`device_id = 5678` now points `device_id` at a different number. You don't declare a type —
Python figures it out from the value. `type(device_id)` tells you what type something is.

## 2.2 Strings and f-strings (how you build prompts to an AI)

A string is text. **f-strings** let you drop variables inside text — you'll use these
constantly to build prompts for an LLM.

```python
device_id = 1234
status = "offline"

msg = f"Device {device_id} is {status}"   # the f before the quote enables the {} substitution
print(msg)                                # Output: Device 1234 is offline

# triple quotes = multi-line text, perfect for long AI prompts:
prompt = f"""
You are a triage assistant.
The device is {device_id}.
Answer only from the logs provided.
"""
```

Without the `f`, the `{device_id}` would print literally as "{device_id}". The `f` is what
makes it insert the value.

## 2.3 Lists — an ordered collection of things

```python
devices = [1234, 5678, 8998]     # a list, written with square brackets
devices.append(9999)             # add an item to the end -> [1234, 5678, 8998, 9999]
print(devices[0])                # first item (counting starts at 0!) -> 1234
print(devices[-1])                # last item (negative counts from the end) -> 9999
print(devices[0:2])               # a "slice": items 0 and 1 -> [1234, 5678]
print(len(devices))                # how many items -> 4
```

**Counting starts at 0.** The first item is `[0]`, the second is `[1]`. This trips up
everyone at first — just remember it.

## 2.4 Dicts — labeled data (THE most important one for GenAI)

A dict stores values under named labels ("keys"). **Almost every response from an AI API
comes back as a dict**, so master this.

```python
device = {
    "id": 8528,
    "status": "offline",
    "error_count": 1,
}

print(device["status"])                 # look up a value by its key -> offline
print(device.get("region", "UNKNOWN"))  # safe lookup: returns "UNKNOWN" if key is missing
device["region"] = "west"               # add or change a key
print("status" in device)               # check if a key exists -> True

for key, value in device.items():       # loop over every key/value pair
    print(f"{key} = {value}")
```

**Why `.get()` matters:** `device["missing"]` *crashes* if the key isn't there.
`device.get("missing", default)` returns a fallback instead. AI responses often have
optional fields, so `.get()` saves you from crashes.

## 2.5 Sets — a bag of unique items

```python
seen = set()
seen.add(1234)
seen.add(1234)          # duplicate ignored — sets keep only unique items
print(1234 in seen)     # True — very fast "have I seen this?" check
```

Used for removing duplicates and "did I already process this?" checks.

## 2.6 JSON ↔ dict (the everyday AI-API move)

AI APIs talk in **JSON** (a text format). Python works with **dicts**. Converting between
them is constant. Good news: **JSON looks almost identical to a Python dict.**

```python
import json                                   # bring in the built-in json tool

data = {"device_id": 1234, "healthy": True}
text = json.dumps(data)                       # dict  -> JSON text  (to send to an API)
back = json.loads('{"device_id": 1234}')      # JSON text -> dict   (to read a reply)
print(back["device_id"])                      # 1234
```

Remember: a JSON "object" *is* a dict, a JSON "array" *is* a list. So if you know dicts and
lists, you can read any API response.

## 2.7 Functions — reusable, named blocks of code

A function packages steps so you can run them again with different inputs.

```python
def greet(device_id):                     # "def" defines a function; device_id is the input
    return f"Checking device {device_id}"  # "return" hands a value back to whoever called it

message = greet(1234)            # "call" the function with input 1234
print(message)                   # Checking device 1234
```

**Default and keyword arguments** — inputs can have defaults and be named when calling:

```python
def search(query, k=3, threshold=0.4):     # k and threshold default if not given
    return f"top {k} results for '{query}' above {threshold}"

search("job not completing")               # uses defaults k=3, threshold=0.4
search("job not completing", k=5)          # override just k
search("job not completing", threshold=0.6)  # name the one you want — order doesn't matter
```

You'll see this everywhere in GenAI libraries, e.g. `model.encode(text, normalize=True)`.

## 2.8 Loops and comprehensions

A loop repeats an action for each item:

```python
devices = [1234, 5678, 8998]
for d in devices:                # "for each item d in devices..."
    print(f"device-{d}")         # ...do this (note the indentation = the loop's body)
```

A **comprehension** is Python's compact way to build a new list from an old one. You'll read
these constantly, so learn the shape:

```python
labels = [f"device-{d}" for d in devices]        # -> ['device-1234', 'device-5678', 'device-8998']
big    = [d for d in devices if d > 5000]         # with a filter -> [5678, 8998]
lookup = {d: f"device-{d}" for d in devices}      # a dict comprehension {1234: 'device-1234', ...}
```

Read it right-to-left-ish: "for each `d` in devices, make `f"device-{d}"`, collect into a list."

## 2.9 If / else and "truthiness"

```python
labels = []
if labels:                       # an EMPTY list counts as False ("falsy")
    print("have labels")
else:
    print("none")                # this runs, because the list is empty

score = 0.3
status = "match" if score > 0.4 else "no match"   # compact one-line if/else
print(status)                    # no match
```

Empty things (`[]`, `{}`, `""`, `0`, `None`) are "falsy" (act like False). Non-empty things
are "truthy". So `if labels:` means "if the list has anything in it."

## 2.10 Imports — using libraries and built-in tools

```python
import json                      # use as json.loads(...)
import numpy as np               # "as np" gives it a short nickname -> np.array(...)
from datetime import datetime    # grab one specific tool from a library
```

`import` loads code so you can use it. `as` renames it (numpy is always `np`, pandas `pd`).

## 2.11 Handling errors so your program doesn't crash

```python
try:
    value = device["missing_key"]         # this would crash...
except KeyError:                          # ...but we catch that specific crash type
    print("that key wasn't there")
except Exception as e:                    # catch anything else; 'e' holds the error details
    print(f"unexpected problem: {e}")
finally:
    print("this always runs, error or not")
```

`try` = "attempt this." `except` = "if it fails this way, do this instead." This keeps one
bad AI response from taking down your whole program.

---

# Part 3 — TIER 2: pick up as you build RAG, agents, and evals (Lessons 18–32)

## 3.1 Calling an API and reading the JSON reply

```python
import requests

resp = requests.get("https://api.example.com/health", params={"device_id": 1234})
print(resp.status_code)          # 200 means success
data = resp.json()               # turn the JSON reply into a dict
print(data["status"])            # navigate it like any dict
```

Every AI model call is, underneath, an HTTP request that returns JSON you read as a dict.
SDKs hide this, but knowing it makes debugging obvious.

## 3.2 numpy — fast math on lists of numbers (used in Lesson 3)

```python
import numpy as np

a = np.array([0.1, 0.2, 0.3])    # a numpy array = a list built for math
b = np.array([0.2, 0.1, 0.4])

print(a * 2)                     # [0.2 0.4 0.6] — math applies to every item, no loop needed
print(a @ b)                     # 0.16 — the "dot product" (this measures similarity of vectors)
print(np.argsort([0.3, 0.9, 0.1]))   # [2 0 1] — the positions that would sort it, smallest first
```

**Why it matters:** embeddings (the number-lists that represent meaning) are numpy arrays.
`@` and `argsort` are the core of similarity search — exactly what Lesson 3 uses.

## 3.3 Type hints — labels that document what goes in and out

```python
def search(query: str, k: int = 3) -> list[str]:    # takes a str and an int, returns a list of str
    ...
```

Hints (`: str`, `-> list[str]`) don't change how code runs — they document intent and make
your editor autocomplete and catch mistakes. Prod code is full of them, so learn to **read**
them; writing them is optional at first.

## 3.4 Classes — blueprints that bundle data + actions

You'll *use* classes (from libraries) long before you write your own. A class is a template;
an "object" is one thing made from that template.

```python
class Retriever:
    def __init__(self, docs):        # __init__ runs when you create one; sets up its data
        self.docs = docs             # "self" = this particular object; store docs on it

    def search(self, query):         # a method = a function that belongs to the object
        return [d for d in self.docs if query in d]

r = Retriever(["job failed", "device offline"])   # create an object (no "new" keyword)
print(r.search("job"))                             # call its method -> ['job failed']
```

`self` always refers to "this specific object." Every method lists `self` first. When you do
`langchain`'s `retriever.invoke(...)`, you're calling a method on an object just like this.

## 3.5 Jupyter notebooks — your experiment lab

```bash
uv pip install notebook
jupyter notebook          # opens in your browser
```

You write code in "cells" and run them one at a time, seeing output right below each cell.
State carries between cells, so you can embed once and then experiment with queries without
re-running everything. Most GenAI tutorials come as notebooks.

---

# Part 4 — TIER 3: later, when a lesson needs it

## 4.1 async / await — doing several slow things at once (Lesson 26+)

```python
import asyncio

async def fetch_logs(device_id):      # "async def" = a function that can pause and resume
    await asyncio.sleep(1)            # "await" = pause here, let other work run meanwhile
    return f"logs for {device_id}"

async def main():
    results = await asyncio.gather(   # run both at the same time instead of one-then-the-other
        fetch_logs(1234), fetch_logs(5678)
    )
    print(results)

asyncio.run(main())                   # start it all
```

**Why it matters:** an agent often calls several tools or the LLM multiple times. `async`
lets those happen concurrently, cutting wait time. Skip it until an agent forces you to.

## 4.2 pydantic — force data into an exact shape (Lesson 18, structured output)

```python
from pydantic import BaseModel

class RootCause(BaseModel):           # define the exact shape you want
    cause: str
    failing_stage: str
    confidence: float

rc = RootCause(cause="upstream API timeout", failing_stage="ingest", confidence=0.8)
print(rc.confidence)                  # 0.8 — validated and typed
print(rc.model_dump())                # turn it back into a dict
```

This is how you make an AI return **exactly** `{cause, failing_stage, confidence}` instead of
messy free text you'd have to parse by hand. Huge for reliability.

## 4.3 pandas — working with tables of data (Lesson 11 and Phase 5's evaluation work)

```python
import pandas as pd

df = pd.read_csv("eval_results.csv")     # load a spreadsheet/CSV into a table
print(df["score"].mean())                # average a column
print(df[df["score"] < 0.5])             # keep only rows where score < 0.5 (like a filter)
print(df.groupby("symptom")["score"].mean())   # average score per symptom type
```

Perfect for measuring how good your RAG is across many test questions.

---

# Part 5 — The next layer (grow into these as the lessons need them)

These separate "working script" from "real engineer." You don't need them to start; you'll
meet each one naturally at the lesson noted.

## 5.1 Generators and `yield` — streaming (Lesson 6/19+, VERY relevant to GenAI)

A normal function returns everything at once. A **generator** hands back items one at a time,
as they're ready. **This is exactly how an AI streams its answer token-by-token** (the words
appearing one by one).

```python
def stream_words(sentence):
    for word in sentence.split():
        yield word                # "yield" = hand back one item, then pause until asked for more

for w in stream_words("the job is not completing"):
    print(w)                      # prints one word per line, as produced
```

When you see an LLM reply appear gradually, a generator is behind it.

## 5.2 Context managers (`with`) — safe setup/cleanup (useful from Lesson 3 onward)

```python
with open("runbook.txt") as f:    # opens the file...
    text = f.read()
# ...and automatically closes it here, even if an error happened inside
```

`with` guarantees cleanup (closing files, connections). You'll use it for files and for many
library resources. Just remember: `with <thing> as <name>:` then an indented block.

## 5.3 Decorators — a label that adds behavior (Lessons 28–32)

A decorator is a `@something` line placed above a function to give it extra powers, without
you changing the function's body. You mostly *use* them, not write them.

```python
# You'll see these in frameworks:
# @app.get("/health")     -> "run this function when someone hits /health"
# @tool                   -> "make this function available to the AI agent as a tool"
# @retry                  -> "if this fails, automatically try again"

@some_decorator
def my_function():
    ...
```

For now: when you see `@name` above a function, read it as "this function has been given the
`name` superpower." Understanding is enough; you rarely author them early.

## 5.4 `*args` and `**kwargs` — "accept any extra arguments" (reading frameworks)

```python
def flexible(*args, **kwargs):
    print(args)        # a tuple of any positional arguments passed
    print(kwargs)      # a dict of any named arguments passed

flexible(1, 2, device_id=1234)     # args=(1, 2)   kwargs={'device_id': 1234}
```

You'll see `*args, **kwargs` in almost every library function signature. It just means "this
function accepts extra arguments and passes them along." Recognize it; that's enough.

## 5.5 Mutability — the sneaky bug source

Lists and dicts are **mutable** (changeable in place). Two names can point at the *same* list,
so changing one changes "both":

```python
a = [1, 2, 3]
b = a              # b points at the SAME list, not a copy
b.append(4)
print(a)           # [1, 2, 3, 4]  <-- surprise! a changed too

c = a.copy()       # make a real copy to avoid this
```

This causes real bugs (an AI response you thought you copied gets mutated). When in doubt,
`.copy()`.

## 5.6 Testing with pytest — proving your code works (Lesson 11, Phase 5)

```python
# in a file test_search.py
def add(a, b):
    return a + b

def test_add():                   # pytest runs any function named test_*
    assert add(2, 3) == 5         # "assert" = "this must be true, or fail the test"
```

Run `pytest`. **Evals in GenAI are basically testing** — checking the AI's output meets a bar.
Learning pytest and learning evals reinforce each other.

---

# Part 6 — How to read an error (a superpower for AI-assisted coders)

When code crashes, Python prints a **traceback**. Beginners panic; engineers read it. The
**last line** names the problem; the lines above show where it happened.

```
Traceback (most recent call last):
  File "embeddings_semantic_search.py", line 12, in <module>
    print(device["region"])
KeyError: 'region'
```

Read bottom-up: **`KeyError: 'region'`** = "you asked for key 'region' but it doesn't exist,"
at **line 12**. Now you know exactly what and where. Common ones:

| Error | Plain meaning | Usual fix |
|---|---|---|
| `IndentationError` | your spacing is off | use consistent 4 spaces |
| `KeyError: 'x'` | dict has no key 'x' | check the key, or use `.get()` |
| `NameError: x` | using a variable/name that doesn't exist | typo, or you forgot to define/import it |
| `TypeError` | wrong type (e.g. added a str to an int) | check what you're passing |
| `ModuleNotFoundError` | library not installed | `uv pip install <it>` (in your venv!) |
| `IndexError` | list position doesn't exist | list is shorter than you think |

**Pro move:** paste the *whole* traceback to an AI and ask "what does this mean and how do I
fix it?" — but now you'll understand the answer instead of blindly pasting a fix.

---

# Part 7 — Using AI to LEARN, not just to generate

You already code with AI. Here's how to make it teach you instead of keeping you dependent:

- **Ask it to explain, line by line:** "Explain this function line by line like I'm new to
  Python." Do this for code it writes you.
- **Ask "why this and not that?"** — "Why a dict here instead of a list?" That builds judgment.
- **Predict, then check:** before running AI code, guess what it outputs. Run it. When you're
  wrong, you just found a gap — ask about exactly that.
- **Make it quiz you:** "Give me 3 small exercises on dicts with answers hidden."
- **Never paste code you can't read.** If you don't understand a line, ask before you ship it.
  That single habit is the whole difference between a copy-paster and an engineer.

---

# Part 8 — What to practice, in order

1. Open `python3`. Make a `device` dict. Read a value with `[]` and with `.get()`.
2. Write a function with a default argument; call it three different ways.
3. Turn a `for`-loop-that-appends into a list comprehension.
4. `json.loads` a small JSON string, then `json.dumps` a dict back.
5. `np.array` two number lists; compute `a @ b`.
6. Cause an error on purpose (look up a missing dict key) and read the traceback.
7. Then run **`embeddings_semantic_search.py`** — you'll now understand every single line.

**You only need Part 2 (Tier 1) to start Lesson 3's hands-on exercise.** Skim the rest so you
know it exists, and come back to each section when its lesson needs it. Learn by building,
not by finishing this document.
