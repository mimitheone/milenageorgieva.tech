---
date: 2026-10-13
description: "Self-improvement, self-replication, and inherited experience—what changes when agents evolve code, pass notes to successors, and how to keep evaluation and authorization separate."
---

# What Happens When Agents Evolve, Inherit and Replicate?

When I wrote about the Darwin Gödel Machine, I started with Transcendence. The idea of an agent improving its own code was fascinating enough to make me experiment with it.

Now there is another dimension to that discussion: agents passing experience to successors that may also be capable of replication.

These are distinct capabilities. Self-improvement changes how effectively an agent works. Self-replication creates another running instance. Their potential combination is where the architecture becomes particularly interesting.

DGM explores changes to an agent's code and evaluates the resulting variants against coding benchmarks. It maintains an archive from which further generations can emerge. Improvements are tested empirically; the requirement for mathematical proof belongs to the original Gödel Machine concept. [DGM research paper](https://arxiv.org/abs/2505.22954)

Anthropic's recent research examines replication capabilities. The result that caught my attention was inherited experience: across six generations, a small model's inference-setup success rose from 45% initially to 61–84% in later generations when successors inherited notes from previous attempts.

Experience can accumulate outside the model's weights.

The experimental boundaries matter. Anthropic simplified access to target machines, and the larger models used separate inference infrastructure. This was not a demonstration of a fully autonomous small-model worm spreading in the wild. [Anthropic's research](https://www.anthropic.com/research/self-replicating-ai)

For me, the connection raises an architectural question: what happens when code evolution, inherited operational knowledge and replication are combined?

That combination is a possibility to investigate, rather than a result established by these studies.

It also makes the control requirements concrete. Who validates a changed agent? Which permissions can a successor inherit? Can we trace its code and memory to an approved ancestor? Can we revoke execution across all its descendants?

I still want to see self-improving agents working in production. But the mechanism that proposes an improvement should not also have unrestricted authority to approve and propagate it.

Evolution needs an evaluation boundary. Deployment needs an authorization boundary.

[My earlier notes on the Darwin Gödel Machine](darwin-godel-machine.md)

For a video explanation of the Darwin Gödel Machine, I recommend this: [Darwin Gödel Machine Explained: Self-Improving AI Agents](https://www.youtube.com/watch?v=KptCerr9D5I).

## Related notes

- [Darwin Gödel Machine](darwin-godel-machine.md)
- [Self-Improving Agents](self-improving-agents.md)
- [Building Trustworthy AI Agents: Design Patterns, SHAP and the EU AI Act](trustworthy-ai-agents.md)
- [Fallback Architecture](fallback-architecture.md)

---

*13 October 2026.*
