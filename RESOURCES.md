# Resources — free tools, courses, and docs, mapped to every lesson

**Rule:** search the term below, then trust that tool's **official docs/quickstart** over
random blogs — blogs go stale and reference outdated APIs; official quickstarts don't.

Jump to a lesson: use your editor's search (`Cmd+F`) for `Lesson N` or `#lesson-N`.

---

## What costs money? (short answer: almost nothing)

Every topic in this roadmap has a 100% free tool. The *only* thing that can cost money is
LLM inference itself, and even that has two free routes:

| Topic | Free tool | Cost |
|---|---|---|
| Courses / videos | DeepLearning.AI short courses, IBM Technology (YouTube), 3Blue1Brown, DAIR.AI | Free |
| LLM inference | **Google Gemini** API free tier (AI Studio) | Free (~1,500 req/day on Gemini Flash) |
| LLM inference (offline) | Ollama (local models) | Free, no bill ever |
| Embeddings | sentence-transformers (local) | Free — or Gemini embeddings API (free tier) |
| Vector DB | Chroma | Free |
| RAG framework | LangChain / LlamaIndex | Free |
| Evaluation | RAGAS | Free (its LLM judge call is the only "cost," covered by free tier) |
| Agents | LangGraph, Google ADK, CrewAI | Free (uses an LLM under the hood) |
| Tool protocol | MCP (Model Context Protocol) | Free, open spec |
| Observability | Langfuse | Free (self-host, or free cloud tier) |
| Deployment | FastAPI + Render / Railway | Free tiers |

**Recommendation:** use the Gemini free tier as your default (simple, no card, and it maps
straight onto enterprise Vertex/Gemini stacks later). Keep Ollama as your offline fallback
for zero-cost experimentation or flaky-wifi days.

> ⚠️ **Free-tier Gemini may train on your prompts.** Use only synthetic/made-up data in
> every exercise — never real, sensitive, or confidential data of any kind. That kind of
> data belongs on a paid enterprise endpoint with a no-training guarantee (e.g. Vertex AI),
> not the free AI Studio tier.

---

## Setup — do this once

```bash
# Get a free key (no credit card): https://aistudio.google.com
export GOOGLE_API_KEY="your-key-here"      # persist it in your shell profile

uv venv
source .venv/bin/activate
uv pip install google-genai

# Corporate network note: if a call fails with CERTIFICATE_VERIFY_FAILED —
export SSL_CERT_FILE=<path-to-corp-ca.pem>
```

One-shot install for everything this roadmap uses (or install per-phase as you reach it):
```bash
uv pip install google-genai sentence-transformers chromadb langchain langchain-community \
               langchain-google-genai ragas langgraph langfuse fastapi uvicorn pydantic
```

---

## Phase 1 — LLM Foundations

#### Lesson 1 — AI, ML, Deep Learning & Generative AI
- Search: `IBM Technology what is generative AI`; `AI vs ML vs deep learning explained`.
- Video: IBM Technology (YouTube) — 5-minute explainer series, consistently accurate and jargon-free.

#### Lesson 2 — Tokens
- Search: `what are tokens in LLM`; `Gemini API count tokens`.
- Docs: Gemini API docs → "Count tokens" page (`google-genai` has a `count_tokens` call).
- Interactive: OpenAI's `tiktoken` tokenizer playground (any provider's tokenizer works to
  build intuition — the *concept* transfers even though Gemini's exact tokenizer differs).

#### Lesson 3 — Embeddings
- Search: `IBM Technology what are embeddings`; `cosine similarity explained`.
- Tool: `sentence-transformers`. Search: `sentence-transformers quickstart`. Model:
  `all-MiniLM-L6-v2` (small, fast, fully local, auto-downloads on first use).
- Setup: `uv pip install sentence-transformers`.
- *(Already done — see `embeddings_semantic_search.py`.)*

#### Lesson 4 — Positional Encoding
- Search: `positional encoding transformer explained simply`.
- Read: Jay Alammar, "The Illustrated Transformer" (jalammar.github.io) — has a dedicated,
  visual section on this.

#### Lesson 5 — Attention
- Read: Jay Alammar, **"The Illustrated Transformer"** (jalammar.github.io) — the canonical
  free visual explainer; also his "Illustrated GPT-2" for the decoder-specific view.
- Video: 3Blue1Brown's "Attention in transformers, visually explained" (YouTube) — save this
  for a relaxed weekend, it's deep but excellent.

#### Lesson 6 — Decoder & Text Generation
- Search: `Gemini API streaming Python`; `autoregressive generation explained`.
- Docs: Gemini API docs → "Generate content" → streaming section.

#### Lesson 7 — Sampling (Temperature, Top-K, Top-P)
- Search: `Gemini API generation config temperature top_p`; `LLM temperature explained`.
- Docs: Gemini API docs → `GenerationConfig` reference.

#### Lesson 8 — Context Window
- Search: `Gemini 2.x context window size`; `LLM context window explained`.
- Docs: Gemini API model overview page (lists context window per model).

#### Lesson 9 — KV Cache
- Search: `KV cache LLM inference explained`; `why does context length affect LLM latency`.
- Read: any of the several free "LLM inference explained" engineering blog posts that come
  up first for that search — cross-check 2 sources since this topic has more blog variance.

#### Lesson 10 — Hallucinations
- Search: `LLM hallucination explained`; `why do LLMs make things up`.
- Video: IBM Technology — "Why do LLMs hallucinate?"

#### Lesson 11 — Model Evaluation
- Search: `LLM as a judge evaluation explained`.
- Preview of Phase 3/5 tool: RAGAS docs (you'll install it there).

#### Lesson 12 — Fine-Tuning
- Search: `when to fine-tune vs prompt engineering vs RAG`.
- Read: Gemini API docs → "Fine-tuning" overview page (conceptual section, even if you don't
  run a job).

#### Lesson 13 — LoRA & QLoRA
- Search: `LoRA fine-tuning explained simply`; `QLoRA explained`.
- Read: Hugging Face's free PEFT (Parameter-Efficient Fine-Tuning) docs intro page.

#### Lesson 14 — RLHF
- Search: `RLHF explained simply`; `how ChatGPT was trained RLHF`.
- Video: any IBM Technology or DeepLearning.AI short explainer on RLHF.

#### Lesson 15 — Quantization
- Search: `model quantization explained`; `Ollama download`; `Ollama run llama3`.
- Setup: install the Ollama app → `ollama pull llama3` (or a smaller model: `phi`, `qwen`) →
  it exposes a local API you call exactly like a cloud one.

---

## Phase 2 — Gemini API

#### Lesson 16 — Gemini API Fundamentals
- Search: `Gemini API quickstart Python`; `Google AI Studio get API key`.
- Docs: ai.google.dev → Gemini API → Python quickstart (the canonical starting point).

#### Lesson 17 — Prompt Engineering
- Course (free): **DeepLearning.AI — "ChatGPT Prompt Engineering for Developers"** (short
  course, ~1 hour, free). Concepts transfer directly to Gemini.
- Reference: promptingguide.ai — free, well-maintained reference for few-shot/CoT patterns.

#### Lesson 18 — Structured Outputs
- Search: `Gemini API structured output JSON schema Python`; `Pydantic response model`.
- Docs: Gemini API docs → "Structured output" page; Pydantic docs → "Models" quickstart.

#### Lesson 19 — Streaming Responses
- Search: `Gemini API streaming Python generate_content_stream`.
- Docs: Gemini API docs → streaming section (same page as Lesson 6, now applied).

---

## Phase 3 — Knowledge Systems (RAG)

#### Lesson 20 — Embeddings in Applications
- Same tool as Lesson 3 (`sentence-transformers`), or `Gemini API embeddings Python` for the
  hosted alternative once you want to compare.

#### Lesson 21 — Vector Databases
- Search: `ChromaDB getting started Python`.
- Docs: Chroma docs — "Getting Started" (`uv pip install chromadb`).
- Know-it-too (for later/interviews): `pgvector tutorial`, `FAISS quickstart`.

#### Lesson 22 — RAG Fundamentals
- Search: `IBM Technology what is RAG`; `build RAG from scratch Python no framework`.
- Video: IBM Technology — "What is Retrieval-Augmented Generation (RAG)?"

#### Lesson 23 — Advanced RAG
- Course (free): **DeepLearning.AI — "LangChain: Chat with Your Data"**.
- Search: `LangChain RAG tutorial`; `LangChain PyPDFLoader`; `RAG reranking explained`.
- Setup: `uv pip install langchain langchain-community langchain-google-genai`.

---

## Phase 4 — AI Agents

#### Lesson 24 — Function Calling
- Search: `Gemini API function calling Python`.
- Docs: Gemini API docs → "Function calling" page (has a runnable Python example).

#### Lesson 25 — Tool Calling
- Same docs page as Lesson 24, extended to multiple tool definitions.

#### Lesson 26 — AI Agents (ReAct, hand-rolled)
- Search: `ReAct pattern LLM agent explained`; `build agent from scratch Python no framework`.
- Read: the original ReAct paper's abstract/intro (arXiv, free) for the Thought/Action/
  Observation framing — you don't need the full paper, just the pattern.

#### Lesson 27 — Agent Frameworks
- Course (free): **DeepLearning.AI — "AI Agents in LangGraph"**.
- Search: `LangGraph quickstart`; `Google ADK quickstart`; `CrewAI quickstart` (pick one
  primary framework — LangGraph is recommended since it maps well to enterprise Gemini stacks).
- Setup: `uv pip install langgraph`.

#### Lesson 28 — Model Context Protocol (MCP)
- Search: `Model Context Protocol quickstart Python`; `build an MCP server Python`.
- Docs: modelcontextprotocol.io — official spec + Python SDK quickstart (free, open).
- Practical: you're already using an MCP-compatible client right now (Claude Code) — build
  a server and connect it here to close the loop.

---

## Phase 5 — Production GenAI

#### Lesson 29 — FastAPI for GenAI
- Search: `FastAPI first steps`; `FastAPI streaming response`.
- Docs: fastapi.tiangolo.com — "First Steps" + "StreamingResponse" section.
- Setup: `uv pip install fastapi uvicorn`.

#### Lesson 30 — AI Application Architecture
- Search: `RAG system architecture diagram`; `production LLM app architecture`.
- Read: any 2–3 vendor engineering blogs (Anthropic, OpenAI, Google) tagged "building with
  LLMs" — cross-reference rather than trusting one source, architectures vary by use case.

#### Lesson 31 — Deployment
- Search: `deploy FastAPI free Render`; `deploy FastAPI free Railway`.
- Docs: Render or Railway's official "Deploy a FastAPI app" guide (both have free tiers).

#### Lesson 32 — Observability
- Search: `Langfuse get started Python`.
- Docs: langfuse.com — "Get Started" (self-host free, or free cloud tier).
- Setup: `uv pip install langfuse`.

#### Lesson 33 — AI Safety & Guardrails
- Search: `LLM prompt injection defenses`; `PII detection Python free`; `LLM guardrails
  open source`.
- Tool options: `guardrails-ai` (open source) or hand-rolled rule checks — either is fine for
  this exercise; the concept matters more than the specific library.

---

## Phase 6 — Portfolio Projects

No new tools — these projects recombine everything from Phases 1–5. The only new skill is
**writing them up**: a short README per project with what/why/result and, where you have
one, an eval number (see RAGAS from Lesson 23/Phase 5).

---

## General references (useful throughout, not tied to one lesson)

- **alexeygrigorev/ai-engineering-field-guide** (GitHub, free) — a practical field guide to
  the AI/GenAI engineer role; good for calibrating scope and interview prep.
- **IBM Technology** (YouTube channel) — reliable 5–10 minute explainers for any concept
  term that confuses you mid-lesson; consistently accurate, no-hype.
- **3Blue1Brown's neural network / attention series** (YouTube) — deeper visual intuition;
  save for a relaxed weekend rather than a weekday study slot.
- **DeepLearning.AI short courses** — all free, ~1 hour each, hosted on their platform;
  the three referenced above (prompt engineering, LangChain chat-with-data, LangGraph
  agents) are the ones this roadmap uses directly.
