# Roadmap — GenAI Engineer (not ML Engineer)

Six phases, 33 lessons, then portfolio projects. Each lesson has: what the concept actually
is, why a GenAI engineer needs it, a concrete hands-on exercise, and a pointer to the free
resource to learn it from (full details in RESOURCES.md).

**Rule for every lesson: nothing is "done" until you've written and run code.** Reading or
watching a video is prep, not completion.

**GenAI vs. agentic, so you know where the pivot is:** Phases 1–3 build the foundation — the
LLM is a smart function you call and a system you retrieve knowledge into. **Phase 4 is the
pivot** — the LLM stops just answering and starts *acting*, choosing tools in a loop. That's
where "agentic AI engineer" begins. You get there by finishing Phases 1–3 first; skipping
ahead to agents without the foundation is how people end up with agents they can't debug.

> ⚠️ Reminder: use only synthetic/made-up data in every exercise below. See the data-safety
> note in README.md ("The cost model" section).

---

## Phase 1 — LLM Foundations
*Goal: understand what's actually happening when you send a prompt and get a response back —
no training, no math derivations, just enough mechanics to reason about behavior and cost.*

- [ ] **Lesson 1 — AI, ML, Deep Learning & Generative AI**
  *Concept:* the nesting — AI ⊃ ML ⊃ Deep Learning ⊃ Generative AI. GenAI (LLMs, diffusion
  models) is a *product* of deep learning, applied to generating new content rather than
  just classifying/predicting.
  *Why it matters:* interviewers use these terms precisely; conflating them is a tell that
  you haven't done the reading.
  *Hands-on:* write a one-paragraph explanation, in your own words, of where an LLM sits in
  this hierarchy and why "GenAI Engineer" ≠ "ML Engineer." Save it as `notes.md`.
  *Resource:* RESOURCES.md, Lesson 1 section

- [ ] **Lesson 2 — Tokens**
  *Concept:* LLMs don't see words — they see tokens, sub-word chunks from a fixed vocabulary.
  *Why it matters:* pricing, context limits, and rate limits are all measured in tokens, not
  words or characters. You cannot reason about cost or context budget without this.
  *Hands-on:* using the Gemini SDK's token-counting call (or `tiktoken` as a stand-in), tokenize
  5 sentences of different languages/styles (plain English, code, a URL, emoji) and print the
  token count for each. Note which ones surprised you.
  *Resource:* RESOURCES.md, Lesson 2 section

- [ ] **Lesson 3 — Embeddings** ✅ *done — see `phase1_llm_foundations/lesson03_embeddings/embeddings_semantic_search.py`*
  *Concept:* a piece of text → a vector of numbers (coordinates in "meaning space"). Similar
  meanings land near each other regardless of shared words.
  *Why it matters:* this is the literal engine behind semantic search and RAG.
  *Hands-on (done):* embedded ~10 short IT-runbook paragraphs, found the nearest match to a
  plain-English query using cosine similarity, with no shared words between query and match.
  *Resource:* RESOURCES.md, Lesson 3 section

- [ ] **Lesson 4 — Positional Encoding**
  *Concept:* transformers process all tokens in parallel, so they need an explicit signal for
  *order* — positional encoding injects "this token is at position 5" into the representation.
  *Why it matters:* explains why "dog bites man" ≠ "man bites dog" to the model despite
  identical tokens.
  *Hands-on:* no code required — sketch (in `notes.md`) what would break if positional
  information were removed, using a concrete two-sentence example.
  *Resource:* RESOURCES.md, Lesson 4 section

- [ ] **Lesson 5 — Attention**
  *Concept:* for each token, attention computes a weighted mix of *every other token* to decide
  what's relevant to it right now — this is how "it" in a sentence resolves to the right noun.
  *Why it matters:* attention is *the* mechanism that made modern LLMs possible; you'll hear
  "self-attention," "multi-head attention," "cross-attention" constantly.
  *Hands-on:* work through Jay Alammar's "Illustrated Transformer" interactively, then write
  a 3-sentence explanation of self-attention using your own example sentence (not the article's).
  *Resource:* RESOURCES.md, Lesson 5 section

- [ ] **Lesson 6 — Decoder & Text Generation**
  *Concept:* modern chat LLMs are decoder-only — they generate one token at a time, feeding
  each new token back in as input for the next prediction (autoregressive generation).
  *Why it matters:* explains streaming, why long outputs take longer than long inputs, and
  why the model can't "go back and edit" earlier tokens mid-generation.
  *Hands-on:* call the Gemini API with `stream=True`, print each token as it arrives, and time
  how long the first token takes vs. the full response.
  *Resource:* RESOURCES.md, Lesson 6 section

- [ ] **Lesson 7 — Sampling (Temperature, Top-K, Top-P)**
  *Concept:* the model outputs a probability distribution over next tokens; sampling
  parameters control how that distribution turns into an actual chosen token.
  *Why it matters:* `temperature=0` for deterministic/factual tasks, higher for creative
  tasks — a real production knob you'll tune constantly.
  *Hands-on:* run the identical prompt at `temperature=0`, `0.7`, and `1.5`, three times each.
  Record whether outputs are identical, similar, or wildly different at each setting.
  *Resource:* RESOURCES.md, Lesson 7 section

- [ ] **Lesson 8 — Context Window**
  *Concept:* the maximum number of tokens (input + output combined) a model can attend to
  in one call. Content beyond it is invisible to the model.
  *Why it matters:* determines how much conversation history / retrieved documents you can
  stuff into one call — a hard architectural constraint on RAG and chat design.
  *Hands-on:* deliberately overflow the context window with a very long input and observe
  what error (or truncation behavior) the API returns.
  *Resource:* RESOURCES.md, Lesson 8 section

- [ ] **Lesson 9 — KV Cache**
  *Concept:* to avoid recomputing attention over the whole growing sequence at every
  generation step, the model caches intermediate key/value tensors from prior tokens.
  *Why it matters:* the dominant memory cost on the serving side, and the reason context
  length affects both latency and infra cost — a favorite "do you actually get inference"
  interview question.
  *Hands-on:* no code — write a 3-sentence explanation of why doubling context length more
  than doubles memory pressure, using the KV cache concept.
  *Resource:* RESOURCES.md, Lesson 9 section

- [ ] **Lesson 10 — Hallucinations**
  *Concept:* the model generates *plausible-sounding* tokens, not necessarily *true* ones —
  it has no built-in fact-checking step; fluency and correctness are separate axes.
  *Why it matters:* the single most important failure mode to design around — it's why RAG,
  evals, and guardrails all exist.
  *Hands-on:* deliberately prompt the model for a fact you know is fabricated-bait (e.g. a
  citation for a paper that doesn't exist) and observe it confidently invent one.
  *Resource:* RESOURCES.md, Lesson 10 section

- [ ] **Lesson 11 — Model Evaluation**
  *Concept:* how you measure whether an LLM's outputs are actually good — rule-based checks,
  human review, and LLM-as-judge scoring.
  *Why it matters:* preview of Phase 3/5's eval work; "how do you know it's working" is the
  question that separates engineers from people demoing vibes.
  *Hands-on:* write 3 rule-based checks (non-empty response, valid JSON if expected, no
  refusal language) and run them against 5 sample outputs.
  *Resource:* RESOURCES.md, Lesson 11 section

- [ ] **Lesson 12 — Fine-Tuning**
  *Concept:* continuing to train an existing model's weights on your own examples to shift
  its behavior/style, instead of prompting alone.
  *Why it matters:* you need to know when *not* to reach for this — as a GenAI engineer,
  prompting + RAG solves 90% of what people assume needs fine-tuning.
  *Hands-on:* no code — write a decision note: for 3 hypothetical tasks (customer support
  tone, extracting a fixed schema, teaching new facts), decide prompt/RAG vs. fine-tuning
  and justify each.
  *Resource:* RESOURCES.md, Lesson 12 section

- [ ] **Lesson 13 — LoRA & QLoRA**
  *Concept:* parameter-efficient fine-tuning — freeze the base model, train small
  low-rank adapter matrices instead of all weights, at a fraction of the cost.
  *Why it matters:* the practical reason fine-tuning became affordable outside big labs;
  common interview vocabulary even if you never run one yourself.
  *Hands-on:* no code — read one LoRA explainer and write a 3-sentence summary of what
  "low-rank" means in your own words (no formulas required).
  *Resource:* RESOURCES.md, Lesson 13 section

- [ ] **Lesson 14 — RLHF**
  *Concept:* Reinforcement Learning from Human Feedback — how base models get tuned into
  helpful, harmless assistants using human preference data and a reward model.
  *Why it matters:* explains *why* ChatGPT/Gemini/Claude behave like assistants at all,
  rather than raw next-token predictors; also the root of a lot of model "personality."
  *Hands-on:* no code — diagram (in `notes.md`) the 3-stage RLHF pipeline (SFT → reward
  model → RL fine-tuning) in your own words.
  *Resource:* RESOURCES.md, Lesson 14 section

- [ ] **Lesson 15 — Quantization**
  *Concept:* representing model weights with fewer bits (e.g. 8-bit or 4-bit instead of 32-bit)
  to shrink memory footprint and speed up inference, at a small quality cost.
  *Why it matters:* the reason you can run a "7B" model on a laptop at all — directly
  relevant if you use Ollama for the offline route.
  *Hands-on:* pull a quantized model with Ollama (e.g. a 4-bit variant) and compare its
  response quality/speed against the full Gemini API on the same prompt.
  *Resource:* RESOURCES.md, Lesson 15 section

---

## Phase 2 — Gemini API
*Goal: become fluent in the actual tool you'll use daily — the Gemini Python SDK — including
the production-shaped controls (structured output, streaming) most tutorials skip.*

- [ ] **Lesson 16 — Gemini API Fundamentals**
  *Concept:* getting a free API key, making your first call, understanding system vs. user
  messages, and the response object's shape.
  *Hands-on:* send one prompt, print the response text, then add a system prompt and observe
  the behavior change.
  *Resource:* RESOURCES.md, Lesson 16 section

- [ ] **Lesson 17 — Prompt Engineering**
  *Concept:* role + context + task + format as the anatomy of a reliable prompt; zero-shot
  vs. few-shot; chain-of-thought for multi-step reasoning tasks.
  *Hands-on:* take one vague prompt, rewrite it with all four anatomy parts, and diff the two
  outputs side by side. Then build a 3-example few-shot classifier and test it on 5 new inputs.
  *Resource:* RESOURCES.md, Lesson 17 section

- [ ] **Lesson 18 — Structured Outputs**
  *Concept:* forcing the model to return data matching a schema (JSON/Pydantic) instead of
  free text you have to regex out of a response.
  *Why it matters:* this is what makes an LLM call safely usable inside real application
  code — no fragile string parsing.
  *Hands-on:* define a Pydantic model `{name: str, email: str, topic: str}`, prompt the model
  to extract these fields from a messy paragraph, and validate the response against the schema.
  *Resource:* RESOURCES.md, Lesson 18 section

- [ ] **Lesson 19 — Streaming Responses**
  *Concept:* receiving tokens as they're generated instead of waiting for the full response.
  *Why it matters:* the difference between a UI that feels instant and one that feels frozen
  for 5+ seconds — a real UX/production concern, not a nicety.
  *Hands-on:* build a tiny CLI chatbot that streams tokens live to the terminal and retains
  conversation history across turns.
  *Resource:* RESOURCES.md, Lesson 19 section

---

## Phase 3 — Knowledge Systems (RAG)
*Goal: understand retrieval well enough to build it by hand before you touch a framework —
this is the single most common thing you'll be asked to build as a GenAI engineer.*

- [ ] **Lesson 20 — Embeddings in Applications**
  *Concept:* moving from Lesson 3's toy example to using embeddings as the retrieval layer
  of a real application — batching, storing, and querying at scale.
  *Hands-on:* embed 50+ chunks of a real (but non-confidential) document and measure how
  embedding time scales with chunk count.
  *Resource:* RESOURCES.md, Lesson 20 section

- [ ] **Lesson 21 — Vector Databases**
  *Concept:* a database purpose-built for storing embeddings and running fast
  nearest-neighbor search over millions of them (Chroma locally; FAISS/pgvector as
  alternatives).
  *Hands-on:* reimplement Lesson 3/20's storage and retrieval using Chroma instead of a
  plain Python list + manual cosine similarity.
  *Resource:* RESOURCES.md, Lesson 21 section

- [ ] **Lesson 22 — RAG Fundamentals**
  *Concept:* Retrieval-Augmented Generation — chunk documents → embed → store → retrieve
  top-k relevant chunks for a query → stuff them into the prompt → generate a grounded
  answer.
  *Why it matters:* the highest-leverage pattern for reducing hallucination and answering
  questions about data the model never saw.
  *Hands-on:* build a from-scratch (no framework) RAG loop over a document you care about
  (a PDF, your own notes) — chunk it, embed it, retrieve, generate, and note where retrieval
  picks the wrong chunk.
  *Resource:* RESOURCES.md, Lesson 22 section

- [ ] **Lesson 23 — Advanced RAG**
  *Concept:* the failure modes of naive RAG and how to fix them — chunk size/overlap tuning,
  metadata filtering, reranking, and returning citations so answers are verifiable.
  *Hands-on:* rebuild Lesson 22's RAG with a RAG framework (LangChain), add a reranking step
  or metadata filter, and compare answer quality before/after on the same test questions.
  *Resource:* RESOURCES.md, Lesson 23 section

---

## Phase 4 — AI Agents ⭐ *the GenAI → agentic pivot*
*Goal: the LLM stops just talking and starts acting — choosing which tool to call, in a loop,
based on what it observes. This is agentic engineering.*

- [ ] **Lesson 24 — Function Calling**
  *Concept:* describing a Python function's signature to the model so it can decide *when*
  and *with what arguments* to call it, instead of you hardcoding the logic.
  *Hands-on:* give the model a fake `get_weather(city)` function description; prompt it with
  a question that should trigger a call, and inspect the structured call it returns.
  *Resource:* RESOURCES.md, Lesson 24 section

- [ ] **Lesson 25 — Tool Calling**
  *Concept:* generalizing function calling into a library of tools an agent can select
  from — the building block of every agent framework.
  *Hands-on:* give the model 3 tool descriptions (calculator, fake search, fake `query_logs`)
  and, for 5 different questions, verify it picks the right tool each time.
  *Resource:* RESOURCES.md, Lesson 25 section

- [ ] **Lesson 26 — AI Agents**
  *Concept:* the ReAct pattern — Thought → Action → Observation, looped until the model
  decides it has enough information to answer.
  *Hands-on:* hand-roll a ReAct loop from scratch (no framework) with 2 real tools and a
  `max_steps` guard so it can't loop forever; trace each Thought/Action/Observation to a
  print statement.
  *Resource:* RESOURCES.md, Lesson 26 section

- [ ] **Lesson 27 — Agent Frameworks (LangGraph, Google ADK, CrewAI)**
  *Concept:* frameworks that formalize the agent loop as a state machine, adding memory,
  retries, and multi-agent orchestration you'd otherwise hand-roll.
  *Hands-on:* rebuild Lesson 26's hand-rolled agent in LangGraph; add conversation memory;
  note exactly what the framework automated for you.
  *Resource:* RESOURCES.md, Lesson 27 section

- [ ] **Lesson 28 — Model Context Protocol (MCP)**
  *Concept:* an open protocol for exposing tools/resources to *any* MCP-compatible agent
  (Claude, VS Code, etc.) instead of wiring tools into one specific app.
  *Hands-on:* expose one read-only tool (e.g. a fake log query) as an MCP server and call
  it from an MCP-compatible client (e.g. Claude Code, which you're using right now).
  *Resource:* RESOURCES.md, Lesson 28 section

---

## Phase 5 — Production GenAI
*Goal: everything that makes a GenAI prototype into a GenAI *product* — this is where your
existing production-engineering background becomes your biggest edge over ML-background peers.*

- [ ] **Lesson 29 — FastAPI for GenAI**
  *Concept:* wrapping an LLM call (or agent) in a real HTTP API — request/response models,
  async calls, streaming endpoints.
  *Hands-on:* wrap your Phase 3 RAG assistant in a FastAPI endpoint that accepts a question
  and streams back an answer.
  *Resource:* RESOURCES.md, Lesson 29 section

- [ ] **Lesson 30 — AI Application Architecture**
  *Concept:* how the pieces fit together in a real system — API layer, retrieval layer,
  LLM layer, evaluation layer, observability layer — and where each failure mode is caught.
  *Hands-on:* draw (in `notes.md` or a diagram tool) the architecture of your Phase 3/4
  project, labeling every external call and every point where it could fail.
  *Resource:* RESOURCES.md, Lesson 30 section

- [ ] **Lesson 31 — Deployment**
  *Concept:* getting your FastAPI app running somewhere other than your laptop, on a free
  hosting tier.
  *Hands-on:* deploy Lesson 29's API to a free host (Render/Railway) and hit it from outside
  your machine (curl from your phone's browser, or a friend's laptop).
  *Resource:* RESOURCES.md, Lesson 31 section

- [ ] **Lesson 32 — Observability**
  *Concept:* tracing every LLM call — prompt, response, tokens, latency, cost — so you can
  debug and optimize a production AI app the way you'd debug any other service.
  *Hands-on:* add Langfuse tracing to your deployed app; make 10 requests and review the
  trace dashboard for cost/latency patterns.
  *Resource:* RESOURCES.md, Lesson 32 section

- [ ] **Lesson 33 — AI Safety & Guardrails**
  *Concept:* input validation, PII detection, prompt-injection defenses, and output filtering
  — the controls that keep an LLM app from doing something it shouldn't.
  *Hands-on:* add one input guardrail (reject obviously malicious/off-topic input) and one
  output guardrail (refuse to return if the answer isn't grounded in retrieved context) to
  your project.
  *Resource:* RESOURCES.md, Lesson 33 section

---

## Phase 6 — Portfolio Projects

Pick 2–3 of these to build to a polished, demo-ready state — these are what you show in
interviews, not the lesson exercises above.

- [ ] **Chat with PDF (RAG)** — document Q&A with citations. Your Phase 3 project, polished.
- [ ] **Documentation Assistant** — RAG over a real (non-confidential) doc set you actually use.
- [ ] **Codebase Assistant** — an agent that can answer questions about a codebase using
  file-read tools + RAG over the repo.
- [ ] **Customer Support AI** — an agent with guardrails, escalation logic, and an eval suite
  proving it stays on-topic.
- [ ] **Research Agent** — multi-step agent that searches, reads, and synthesizes an answer
  with citations.
- [ ] **Workflow Automation** — an agent wired to real (sandboxed) tools that takes an
  action, not just answers a question.
- [ ] **Multimodal AI App** — using Gemini's multimodal input (image/audio + text) for a
  concrete use case.

**For each project you finish:** write a short README with a one-paragraph what/why/result,
and include an **eval number** if you have one ("faithfulness 0.82 → 0.91 after adding
reranking"). That eval number is what makes a portfolio project read as engineering rather
than a demo.

---

## Habits that make it stick

- **Read one reference implementation per phase**, after you've built the concept by hand —
  not before. Seeing a production version once you understand the fundamentals cements them.
- **Log every session** in `LOG.md` — one line: what you built, what surprised you.
- **Always try to break what you just built.** Feed it an out-of-scope input and watch it
  fail — understanding failure modes is half of engineering.
- **Watch cost and latency from Phase 2 onward** — which model, how many tokens, how long it
  took. This habit alone is a strong interview signal.
