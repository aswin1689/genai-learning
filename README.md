# GenAI Learning

A hands-on repository for transitioning from **Software Engineer → Generative AI Engineer**
(not ML Engineer) using **Python** and the **Google Gemini API**, entirely on free resources.

> **The distinction that shapes this whole repo:** an ML Engineer trains/fine-tunes models.
> A **GenAI Engineer builds applications on top of models someone else trained** — RAG
> systems, agents, tool-calling workflows, evaluation pipelines, and production services
> that call an LLM API. You will not train a model from scratch here. You will get very
> good at *using* one, reliably, in production-shaped code.

---

## Who this is for

You — a working senior software engineer who already knows how to code, ship, and operate
production systems, but has never built anything with an LLM API. This repo assumes strong
general engineering skill and **zero prior GenAI/ML knowledge**. Every lesson explains the
concept from first principles, then has you write code that actually runs.

---

## Goals

- Understand how Large Language Models work well enough to reason about their behavior,
  cost, and failure modes — without needing the math of training one.
- Master the **Gemini Python SDK** (`google-genai`) as your daily driver LLM API.
- Build **production-shaped** AI applications: structured output, streaming, retries,
  observability, deployment — the engineering half most tutorials skip.
- Understand **Retrieval-Augmented Generation (RAG)** deeply enough to build it by hand
  before reaching for a framework.
- Build **AI agents** — tool-calling loops, not just chat completions.
- Learn **evaluation** — the skill that separates an engineer from someone who got lucky
  with a demo.
- Leave with a **portfolio of shipped projects** and the concept fluency to pass a GenAI
  engineer interview.

---

## Learning philosophy

1. **Understand concepts before frameworks.** You build RAG and a ReAct agent by hand
   before you touch LangChain/LangGraph. Frameworks make sense once you've felt the pain
   they solve.
2. **Build every concept with code.** No lesson is "done" until something runs on your
   laptop. Watching a video with no code doesn't count.
3. **Prefer simple Python over heavy abstractions**, at least on the first pass. Simple
   code you understand beats a framework you copy-paste.
4. **Production practices alongside APIs, not bolted on at the end.** Cost, latency,
   evaluation, and observability show up from Phase 2 onward, not just in Phase 5.
5. **Ship rough, iterate.** Don't polish Lesson 1's script in Lesson 20. Breadth of reps
   beats a handful of perfect ones.
6. **This is a scaffold, not a contract.** Miss a week? Shift, don't quit. Consistency
   over perfection.

---

## The cost model — this should cost you ~$0

**LLM inference is the only thing that can cost money**, and even that has a reliable free
route:

- **Google Gemini** via AI Studio (aistudio.google.com) — free, no credit card, a generous
  daily request quota on Gemini Flash. Far more than these lessons need.
- Everything else — courses, vector DB, RAG framework, evaluation, agents, observability,
  deployment — is free and open source. See RESOURCES.md for the full, lesson-by-lesson
  list of free tools and search terms.

> ⚠️ **Data safety rule — read this before Lesson 1.** Free-tier Gemini may train on the
> prompts you send it. **Only ever send synthetic / made-up data through these exercises —
> never real, sensitive, or confidential data of any kind.** If you later want to point a
> lesson at real data, that happens on a paid/enterprise LLM endpoint with a no-training
> guarantee (e.g. Vertex AI), not the free AI Studio tier.

---

## Repository map

| File | Purpose |
|---|---|
| **README.md** | You are here — overview, philosophy, setup. |
| **ROADMAP.md** | The full curriculum: 6 phases, 41 lessons + portfolio projects, each with a concept explainer, a hands-on exercise, and a completion checkbox. |
| **RESOURCES.md** | Every free resource this roadmap uses — courses, docs, videos — organized by phase/lesson, plus setup/install steps. |
| **INTERVIEW_PREP.md** | Concept-fluency questions, system-design prompts, and portfolio talking points to get interview-ready. |
| **PYTHON-FOR-GENAI.md** | A from-zero Python primer scoped to exactly what these lessons need. Read this first if any lesson's code looks unfamiliar. |
| **LOG.md** | One line per session: what you built, what surprised you. Read it back on low-motivation days. |
| **archive/** | Earlier planning docs (a rung-based ladder and a 12-week day-by-day plan) — superseded by ROADMAP.md but kept for reference. |

---

## Repository structure (planned)

Folders are created as you reach each phase — don't pre-create empty ones.

```
genai-learning/
├── README.md
├── ROADMAP.md
├── RESOURCES.md
├── INTERVIEW_PREP.md
├── PYTHON-FOR-GENAI.md
├── LOG.md
├── archive/
│   ├── ROADMAP-friday-rung-ladder.md
│   └── genai-daily-plan-12-week.md
│
├── phase1_llm_foundations/        # Lessons 1–15 — concepts, mostly no API key needed
│   └── lesson03_embeddings/
│       └── embeddings_semantic_search.py   # done — local embeddings + cosine similarity
├── phase2_gemini_api/             # Lessons 16–21 — API basics, multimodal, resilience
├── phase3_knowledge_systems/      # Lessons 22–27 — embeddings in practice, vector DBs, RAG
├── phase4_ai_agents/              # Lessons 28–34 — function calling, agents, MCP, security
├── phase5_production_genai/       # Lessons 35–41 — FastAPI, deployment, cost, safety
└── projects/                      # Phase 6 portfolio projects
```

Each lesson folder should end up with: example code, a short notes file (what you learned,
what surprised you), and at least one exercise you completed from scratch (not copied).

---

## Technologies

- **Python** 3.12+
- **Google Gemini API** (`google-genai`) — the LLM
- **Pydantic** — structured output validation
- **FastAPI** — serving your AI apps
- **Chroma** (local) / FAISS / pgvector — vector databases
- **sentence-transformers** — local, free embeddings for early lessons
- **LangGraph** — agent framework (after you've built a ReAct loop by hand)
- **Google ADK**, **MCP** — reusable agent tooling
- **RAGAS** — evaluation
- **Langfuse** — observability
- **Docker** — packaging for deployment
- **GitHub Actions** — CI eval gates (catching prompt/model regressions on push)

---

## Getting started

```bash
# 1. Environment (uv creates and manages the virtual environment)
uv venv
source .venv/bin/activate

# 2. Get a free Gemini API key — no credit card
#    https://aistudio.google.com
export GOOGLE_API_KEY="your-key-here"     # add to your shell profile to persist

# 3. Install the SDK to start Phase 2 (Phase 1 mostly needs no installs)
uv pip install google-genai

# 4. Corporate network note: if your first API call fails with CERTIFICATE_VERIFY_FAILED,
#    point Python at your corporate CA bundle:
export SSL_CERT_FILE=<path-to-corp-ca.pem>
```

New to Python? Read PYTHON-FOR-GENAI.md first — it's a from-zero primer scoped exactly to
what this roadmap needs, not a full Python course.

---

## Progress

- [ ] **Phase 1 — LLM Foundations** *(in progress — embeddings lesson done, see `embeddings_semantic_search.py`)*
- [ ] **Phase 2 — Gemini API**
- [ ] **Phase 3 — Knowledge Systems (RAG)**
- [ ] **Phase 4 — AI Agents**
- [ ] **Phase 5 — Production GenAI**
- [ ] **Phase 6 — Portfolio Projects**

Full lesson-by-lesson checklist lives in ROADMAP.md.

---

## Habits that make this stick

- **Read one real-world reference implementation per phase** once you've built the concept
  by hand — seeing a production version after you understand the fundamentals cements it.
- **Write a one-line log entry per session** in `LOG.md` — what you built, what surprised
  you. This becomes both your memory and your portfolio narrative.
- **Always try to break what you just built** — feed it an out-of-scope input and watch it
  fail. Understanding failure modes is half of engineering.
- **Watch cost and latency from Phase 2 onward** — which model, how many tokens, how long
  it took. GenAI engineers reason about this by default, not as an afterthought.

Happy building!
