# Systems Architecture

Notes on AI system design — component boundaries, responsibility separation, orchestration, and what turns models into production systems.

## In this section

- [Single Responsibility Principle](single-responsibility-principle.md) — reasons for change, not counting methods
- [Agent Contracts](agent-contracts.md) — from prompt-first to contract-first design
- [Interface Segregation Principle](interface-segregation-principle.md) — the smallest useful boundary for agent capabilities
- [Components and Skills](components-and-skills.md) — skills as libraries; components as business capabilities
- [Reuse/Release Equivalence Principle](reuse-release-equivalence-principle.md) — version business capabilities, not loose prompts
- [Acyclic Dependency Principle](acyclic-dependency-principle.md) — no dependency cycles; return results, don't invoke back
- [Stable Dependencies Principle](stable-dependencies-principle.md) — depend toward stability; contracts, not the Planner
- [The Architecture of AI Systems](ai-systems-architecture.md) — from reasoning to action, and why architecture beats the model choice
