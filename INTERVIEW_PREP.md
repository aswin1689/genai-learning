# Interview Prep — GenAI Engineer

Three tracks: **concept fluency** (can you explain it cleanly, out loud, without notes),
**system design** (can you architect something), and **portfolio narrative** (can you talk
about what you built like an engineer, not a tutorial-follower). Work through these *after*
you've built the corresponding lesson — reciting a concept you haven't coded is memorization,
not fluency.

---

## Track 1 — Concept fluency

Practice answering these **out loud, in under 90 seconds each**, without reading a script.
If you can't, that's a signal to revisit the lesson, not to write a better answer to memorize.

### Foundations (Phase 1)
- What's the difference between an ML Engineer and a GenAI Engineer? Which are you, and why?
- Explain what a token is, and why pricing/context limits are measured in tokens, not words.
- Explain embeddings without using the word "vector."
- Walk me through what happens, mechanically, between you sending a prompt and the first
  word of the response appearing.
- Why do LLMs hallucinate? Why can't you just "turn hallucination off"?
- What is temperature, and when would you set it to 0 vs. 1?
- What is a context window, and what happens when you exceed it?
- Explain the KV cache and why longer conversations get slower/more expensive.
- When would you choose fine-tuning over RAG, and vice versa? Give a concrete example of each.

### Gemini API / prompting (Phase 2)
- What makes a prompt "well-engineered" vs. just "a question"? Give the 4-part anatomy.
- What's the difference between zero-shot and few-shot prompting, and when do you reach for
  few-shot?
- Why would you force structured (JSON/schema) output instead of parsing free text? What
  breaks if you don't?
- What's the practical difference between a streaming and a non-streaming API call, from a
  user's perspective?

### RAG (Phase 3)
- Explain RAG end to end: what happens at index time vs. query time?
- Why does RAG reduce hallucination? What does it *not* fix?
- What's a bad outcome from picking too small a chunk size? Too large?
- How would you make a RAG system's answers verifiable to the end user?
- What's reranking, and why isn't top-k cosine similarity alone always enough?

### Agents (Phase 4)
- What's the actual difference between "calling an LLM" and "an AI agent"?
- Explain the ReAct loop (Thought → Action → Observation) using an example task.
- What's the risk of an agent with no `max_steps` or budget guard? How have you seen (or
  built) that fail?
- What does a framework like LangGraph give you that a hand-rolled loop doesn't?
- What is MCP, and what problem does it solve that "just writing tool-calling code" doesn't?
- How do you evaluate agent performance specifically — not just the final answer, but tool
  selection quality, task completion, and context adherence (did it stay grounded in what
  its tools actually returned)?
- How do you handle a tool call that fails? What makes a tool call safe to retry
  (idempotent) vs. unsafe (e.g. a "send email" tool)?
- When is an agent the wrong solution to a problem?

### Production (Phase 5)
- How do you evaluate whether an LLM app "works" — walk through your eval approach on your
  own project, with actual numbers if you have them.
- What would you trace/log in a production LLM app, and why?
- Name two concrete guardrails you'd put in front of a customer-facing LLM app, and what
  each protects against.
- How do you reason about cost in an LLM application in production? What levers do you have?
- How would you test a new model version before rolling it out fully — what's your
  equivalent of a canary release for an LLM swap?
- Your app is Dockerized with a CI eval gate — walk through what happens from a prompt
  change being committed to it reaching production, and where a regression gets caught.

---

## Track 2 — System design prompts

Practice these **out loud**, sketching an architecture as you talk (diagram tool, whiteboard,
or just narrate the boxes/arrows). Aim for 5–10 minutes each, covering: components, data
flow, failure modes, and one scaling/cost tradeoff you'd flag proactively.

- "Design a Q&A system over 10 million internal documents." (Cover: chunking strategy,
  vector DB choice at that scale, retrieval latency, freshness/reindexing, evaluation.)
- "Design a customer support agent that can look up order status and issue refunds."
  (Cover: tool design, guardrails on the refund action specifically, escalation to a human,
  logging for audit.)
- "A production RAG app's answers got worse after a content migration. How do you debug it?"
  (Cover: is it retrieval or generation, chunking regression, eval regression testing,
  reindex verification.)
- "How would you reduce the latency and cost of an LLM app that's too slow/expensive in
  production?" (Cover: smaller model for simple sub-tasks, caching, prompt trimming,
  streaming for perceived latency, batching where applicable.)
- "Design an internal 'ask the codebase' assistant for engineers." (Cover: code-aware
  chunking, function-level retrieval vs. file-level, staying current with commits, and how
  this differs from prose-document RAG.)

---

## Track 3 — Portfolio narrative

For each Phase 6 project you finish, be ready to answer, unscripted:

1. **What did you build, in one sentence?**
2. **Why does it exist — what problem does it solve?**
3. **What was the hardest part, and how did you solve it?** (This is the question that
   separates "I followed a tutorial" from "I engineered something." Have a real answer —
   a retrieval bug, a prompt that kept failing, a cost problem you fixed.)
4. **What's the eval number, before and after your best improvement?** (e.g. "faithfulness
   0.82 → 0.91 after adding reranking.") If you don't have one yet, that's your next step
   before calling the project portfolio-ready — see Lesson 11/23's eval work.
5. **What would you do differently, or add next, with more time?** (Shows judgment, not
   just completion.)

---

## Track 4 — Framing your background as an asset (not a gap)

You're coming from senior software engineering, not an ML background. In interviews, that's
a strength if you frame it — most people going for GenAI Engineer roles from an ML/research
background haven't shipped production software; you have. Concretely:

- You already know **testing, observability, deployment, and operating systems in
  production** — most of Phase 5 is you applying skills you already have to a new kind of
  component (an LLM call), not learning them from zero.
- You can talk about **evals like you'd talk about test coverage** — a familiar engineering
  frame that a lot of GenAI-only candidates lack.
- Be honest that you're new to the ML *theory* (Phase 1's deeper topics — attention math,
  RLHF internals) but fluent in *using* models in systems — that's precisely the GenAI
  Engineer job description, not the ML Engineer one. Don't overclaim training/fine-tuning
  depth you don't have; you don't need it for this role.

---

## Light DSA (don't skip, don't over-invest)

GenAI Engineer interviews are lighter on algorithmic depth than pure SWE roles, but rarely
zero. 20–30 min/day is enough:
- Focus: arrays, strings, hashmaps — the categories that show up in "parse/process this
  data" style questions, which is most of what a GenAI engineer's non-LLM code looks like.
- Free resource: LeetCode Easy/Medium filtered to those tags.
- Don't grind graph/DP-heavy problems for this track unless the specific company's loop
  is known to include them — check the job description/recruiter screen first.

---

## A realistic bar for "interview ready"

You're ready when you can, without notes:
- Explain every Phase 1–4 concept above in under 90 seconds, correctly, in your own words.
- Walk through one system design prompt end to end, unscripted, catching your own gaps.
- Talk through 2 portfolio projects with a real "hardest part" story and a real eval number.
- Answer "why GenAI Engineer and not ML Engineer" in a way that sounds like a decision, not
  a default.

That's the finish line this whole roadmap is built to hit.
