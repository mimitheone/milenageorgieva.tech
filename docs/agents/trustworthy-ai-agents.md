---
date: 2026-09-22
description: "Reflection, planning, multi-agent workflows, SHAP explainability, and the EU AI Act—connecting design patterns to assessable, accountable agent systems."
---

# Building Trustworthy AI Agents: Design Patterns, SHAP and the EU AI Act

As their responsibilities grow, architecture becomes a question of both capability and accountability.

AI agents are increasingly being designed to research information, analyse data, recommend decisions and take actions across business systems.

How does an agent organise its work? How are mistakes detected? What can a person inspect before approving an action? What evidence does an organisation need to assess whether the system meets applicable regulatory requirements?

Reflection, planning and multi-agent workflows offer useful ways to structure agent behaviour. Explainability methods such as SHAP can help people interpret predictive models used within these workflows. Trustworthy AI principles and the EU AI Act provide a broader context for deciding which controls the complete system needs.

These concepts are connected, but they serve different purposes. Understanding those differences helps us build systems that are easier to evaluate, supervise and improve.

## 1. What do we mean by an AI agent?

For this article, an AI agent is a software system that uses an AI model to pursue a goal through a sequence of decisions and actions within defined permissions.

A typical agent may:

- interpret a request;
- retrieve information or select a tool;
- use the result to determine its next step;
- produce a recommendation or perform an authorised action; and
- stop, request clarification or escalate when necessary.

Consider the difference between generating a paragraph about overdue invoices and handling an invoice investigation.

An invoice agent might retrieve purchase orders, compare payment records, identify discrepancies, draft a response and request approval before contacting a supplier.

The model is only one component of that system. Its behaviour also depends on tools, data access, memory, orchestration, permissions and the surrounding business process.

This distinction matters when we evaluate an agent. A model can produce a sensible answer whilst the wider system retrieves the wrong customer record or performs an action without the required authorisation.

The unit we need to assess is the complete workflow.

## 2. Reflection: creating a structured feedback loop

**Reflection is a pattern in which an agent evaluates an output or attempted action and uses feedback to revise its subsequent response or behaviour.**

A simple workflow is:

**Draft → evaluate → revise → validate**

Evaluation may take place within the same agent or through a separate critic agent.

A critic agent is given a specific review role. It might check whether a recommendation is supported by evidence, whether a calculation is consistent with the source data or whether required information is missing.

The research framework *Reflexion*, introduced by Shinn and colleagues, explores agents that use linguistic feedback and retain reflective text in memory to improve subsequent attempts without updating model weights. This is one implementation of the broader reflection pattern. [Shinn et al., *Reflexion: Language Agents with Verbal Reinforcement Learning*](https://arxiv.org/abs/2303.11366)

### Example: reviewing a supplier assessment

A procurement agent prepares a supplier assessment using delivery records and internal reports.

A critic reviews it against explicit criteria:

- Are the factual claims supported by the retrieved records?
- Do the figures match the underlying data?
- Are conflicting reports acknowledged?
- Is the recommendation within the agent's assigned authority?

Suppose the draft states that a supplier 'consistently misses deadlines', but the records show two delayed deliveries out of twenty.

The critic can flag that the language overstates the evidence. The drafting agent can then revise the assessment to report the observed delivery rate and describe the relevant incidents accurately.

The review is useful because the critic has a defined standard and access to evidence.

### Where reflection can fail

A second model response is not an independent source of truth. A critic may repeat the original error, accept a fabricated citation or persuade the drafting agent to change a correct answer.

Huang and colleagues investigated intrinsic self-correction in reasoning tasks. In the settings they studied, models struggled to correct answers without external feedback, and their performance sometimes deteriorated. These findings should be understood within their experimental scope rather than treated as a permanent conclusion about every model. [Huang et al., *Large Language Models Cannot Self-Correct Reasoning Yet*](https://arxiv.org/abs/2310.01798)

A practical response is to combine critique with external checks: source documents, calculations, business rules, executable tests or qualified human review.

Reflection also needs a stopping rule. Repeated revisions can increase cost and delay without improving the result.

A critic can support governance by identifying problems and assembling evidence for review. Responsibility for accepting the final result must still have a named owner.

## 3. Planning: turning a goal into controlled steps

**Planning is the process of decomposing a goal into steps, identifying dependencies and deciding how to execute and adapt those steps.**

A useful agent plan should describe both the work and the conditions under which it may proceed.

This includes the data required, the tools permitted, the decisions that require approval and the response to missing information.

Two research approaches illustrate different aspects of this idea.

*Plan-and-Solve Prompting* asks a model to devise a plan that divides a task into smaller subtasks before solving them. It studies a prompting strategy for reasoning tasks rather than a complete production control architecture. [Wang et al., *Plan-and-Solve Prompting*](https://arxiv.org/abs/2305.04091)

*ReAct* explores the interleaving of reasoning and actions, allowing information obtained from the environment to inform subsequent steps. [Yao et al., *ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629)

### Example: a customer refund workflow

A customer requests a refund. An agent's plan might be:

1. Retrieve the relevant order and payment record.
2. Check the applicable refund policy.
3. Determine whether the request meets the policy conditions.
4. Prepare a recommendation with supporting evidence.
5. Route exceptions or amounts above a defined threshold to an authorised employee.
6. Execute the refund only when the required authorisation is present.
7. Record the outcome.

If the payment record is unavailable, the plan should specify a safe response. The agent should pause or escalate rather than fill the gap with an assumption.

The plan can also change when new information becomes available. A previously refunded order requires a different response from an unpaid order.

### A plan needs enforcement

An instruction in a prompt to 'ask for approval before issuing a refund' is a weak control if the agent still has unrestricted access to the payment tool.

A stronger implementation places the authorisation check within the execution system. The tool verifies that suitable approval exists before performing the transaction.

This separates the agent's proposal from the system's authority to act.

Planning can make governance controls visible, but its value depends on whether those controls are technically enforced.

## 4. Multi-agent workflows: specialisation with clear responsibility

**A multi-agent workflow co-ordinates several agents with distinct responsibilities to accomplish a shared task.**

Common arrangements include sequential handovers, parallel analysis, a co-ordinator delegating work and a generator paired with a reviewer.

The *AutoGen* paper describes infrastructure for building applications through conversations between customisable agents, including combinations of models, tools and human input. It provides a useful research reference for organising these interactions. [Wu et al., *AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*](https://arxiv.org/abs/2308.08155)

### Example: preparing an operational incident report

An organisation could assign:

- an evidence agent to retrieve incident records;
- an analysis agent to reconstruct the timeline;
- a drafting agent to prepare the report; and
- a review agent to check claims against the evidence.

A human incident owner reviews the final report and authorises its release.

Each handover should communicate more than a paragraph of text. It should identify the task, the evidence used, unresolved questions and the status of the work.

For example, the evidence agent might report that logs are missing for a particular period. The analysis agent should carry that limitation into the timeline rather than silently treating the record as complete.

### More agents introduce more co-ordination

Several agents can share the same blind spots. They may agree because they use similar models or received the same misleading evidence.

Co-ordination can also introduce duplicated work, inconsistent assumptions, lost context and unclear completion criteria.

A useful design gives each agent a bounded role, appropriate permissions and a clear output contract.

The organisation must still know who owns the complete process. Distributing tasks amongst agents does not remove human or organisational responsibility.

## 5. Trustworthy AI: the principles surrounding the workflow

**Trustworthy AI is a broader framework for evaluating whether an AI system is lawful, ethical and robust.**

The European Commission's expert guidelines identify seven requirements:

- human agency and oversight;
- technical robustness and safety;
- privacy and data governance;
- transparency;
- diversity, non-discrimination and fairness;
- societal and environmental well-being; and
- accountability.

These are ethical guidelines, distinct from the binding legal obligations of the AI Act. [European Commission, *Ethics Guidelines for Trustworthy AI*](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai)

For agent builders, the principles lead to practical questions.

Can a person interrupt an active workflow? Can the agent access information beyond its purpose? Do reviewers understand the limitations of its recommendations? Are errors measured across relevant groups? Can the organisation investigate an incident and correct the system?

A polished explanation addresses only part of these questions. Data practices, operational safeguards, evaluation and ownership also matter.

This is where explainability tools can make a useful contribution.

## 6. SHAP: explaining model predictions within an agent workflow

**SHAP—SHapley Additive exPlanations—is a framework for attributing a model output to its input features.**

It draws on Shapley values from co-operative game theory. Features receive contributions that account for the difference between a reference output and the output being explained.

Lundberg and Lee introduced SHAP as a unified approach to feature attribution for individual predictions. [Lundberg and Lee, *A Unified Approach to Interpreting Model Predictions*](https://arxiv.org/abs/1705.07874)

Two distinctions are useful:

**Local explanation:** Which features contributed to this particular prediction?

**Global summary:** Across a collection of predictions, which features tend to make larger contributions?

The reference data, explainer, assumptions and output scale all affect interpretation. SHAP values may be expressed in model-score units or log odds, for example, rather than percentage points of probability. These details should be recorded with the explanation. [SHAP documentation, *An Introduction to Explainable AI with Shapley Values*](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)

### Example: a customer retention agent

Imagine an agent that uses a predictive model to identify customers who may leave a service.

For a particular customer, a SHAP explanation might show that declining product usage and unresolved support issues contributed to a higher predicted churn score.

An explanation component can attach these results to the agent's recommendation. A critic can then check whether the written recommendation accurately reflects the model output and the customer records:

**Customer data → predictive model → SHAP explanation → proposed response → review → authorised action**

The agent might recommend a service follow-up because unresolved support issues appear in both the records and the explanation.

The explanation does not establish that a particular intervention will prevent churn.

SHAP explains how the predictive model uses information. Establishing the effect of a proposed action requires additional evidence, such as an experiment or suitable causal analysis. The SHAP documentation explicitly discusses this distinction. [Dillon et al., *Be Careful When Interpreting Predictive Models in Search of Causal Insights*](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/Be%20careful%20when%20interpreting%20predictive%20models%20in%20search%20of%20causal%20insights.html)

### What SHAP contributes—and what remains to be explained

SHAP can support model debugging and help reviewers interpret a prediction.

It does not explain the entire agent workflow: why a particular tool was selected, whether the retrieved information was reliable or whether an action was authorised.

It also does not establish that a model is accurate, fair, secure or legally compliant.

A useful architecture therefore preserves model-level explanations alongside workflow-level records.

## 7. Connecting these approaches to the EU AI Act

**The EU AI Act establishes obligations that depend on factors including a system's intended purpose, risk classification and the organisation's role.**

An application does not become high risk simply because it uses agents, several models or autonomous planning.

Classification requires an assessment of what the system is intended to do and how it falls within the Act's rules. [AI Act, Article 6](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-6)

For high-risk systems, the requirements cover several areas that agent architecture can help address:

| Area | Relevant provision | Possible architectural contribution |
|---|---|---|
| Risk management | Article 9 | Define failure scenarios, escalation conditions and testing criteria. |
| Data and data governance | Article 10 | Control data provenance, quality, suitability and relevant bias checks. |
| Technical documentation | Article 11 | Document components, intended purpose, limitations and evaluations. |
| Record-keeping | Article 12 | Generate relevant records of system operation. |
| Transparency | Article 13 | Help deployers interpret outputs and understand limitations. |
| Human oversight | Article 14 | Provide effective review, override, intervention and stopping mechanisms. |
| Accuracy, robustness and cybersecurity | Article 15 | Test the system and enforce operational safeguards. |

These architectural measures are possible implementation choices rather than solutions prescribed by the Act. [AI Act, requirements for high-risk systems](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9)

The connection to SHAP is particularly relevant to output interpretation. Article 13 addresses sufficient transparency to enable deployers to interpret the output of a high-risk system and use it appropriately. SHAP may help with a predictive component for which feature attribution is suitable, but the Act does not require SHAP. [AI Act, Article 13](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-13)

Likewise, adding an approval button does not necessarily provide effective human oversight. Reviewers need the competence, information, authority and practical ability to intervene, including an awareness of possible over-reliance on automated outputs. [AI Act, Article 14](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-14)

Compliance extends beyond architecture to applicable organisational duties, assessment processes and monitoring. These design patterns can support that work, but they do not amount to a complete compliance determination.

## 8. A higher-stakes example: creditworthiness assessment

Consider an agent that supports the assessment of a natural person's creditworthiness.

This use appears in Annex III amongst the high-risk categories, with an exception for systems used to detect financial fraud. The detailed classification rules and actual intended purpose still need to be assessed. [AI Act, Annex III](https://ai-act-service-desk.ec.europa.eu/en/ai-act/annex-3)

An illustrative architecture could include:

- **Planning component:** identifies the required records and permitted analysis steps.
- **Data-validation component:** flags missing, inconsistent or outdated information.
- **Predictive component:** produces a creditworthiness score within its defined scope.
- **Explanation component:** uses SHAP, where appropriate, to describe feature contributions.
- **Critic component:** checks that the proposed report matches the verified inputs and computed explanation.
- **Human oversight interface:** presents the result, limitations, unresolved issues and available intervention options.
- **Execution controls:** enforce who can authorise a consequential action.
- **Monitoring:** tracks failures, model performance and operational incidents.

Suppose the report attributes a negative contribution to income, but the source record contains an outdated figure. An explanation alone cannot resolve that problem. The data must be corrected and the result reassessed.

Similarly, excluding a protected characteristic from a model's direct inputs does not establish fairness. Relevant proxy effects and outcomes across groups require separate evaluation.

Explainability must therefore sit within a wider system of data validation, evaluation, oversight and accountability.

## 9. Turning design intentions into evidence

A practical development method is to connect each intended control to observable evidence.

| Design intention | Evidence to inspect |
|---|---|
| Consequential actions require approval. | Attempts without approval are blocked and recorded. |
| Recommendations are supported by sources. | Reviewers can inspect the supporting records and identify unsupported claims. |
| Critique improves output quality. | Evaluation shows fewer relevant errors after review, including checks for harmful revisions. |
| SHAP explanations are presented accurately. | Reports match the computed values, output scale and recorded explainer configuration. |
| Humans can intervene. | Exercises demonstrate that authorised reviewers can pause, override or stop the workflow. |
| The system handles tool failure safely. | Simulated failures produce the defined fallback or escalation behaviour. |

This provides a more concrete basis for evaluation than asking whether an agent 'seems trustworthy'.

It also encourages proportionate complexity. A simple workflow with a reliable calculation and one approval point may serve a task better than several agents debating the same evidence.

Additional agents, explanations and review loops should earn their place through measurable value.

## 10. Building useful autonomy with accountable operation

Reflection can create opportunities to detect mistakes.

Planning can expose dependencies and control points.

Multi-agent workflows can separate responsibilities and specialist tasks.

SHAP can help people interpret predictions made by suitable models within those workflows.

Trustworthy AI principles help define broader expectations, whilst the EU AI Act establishes applicable legal obligations.

The engineering challenge is to connect these ideas in a system whose behaviour can be assessed in practice.

Can we identify the evidence behind a recommendation? Can we determine which model produced a score? Can a reviewer understand the limitations of the explanation? Can the organisation prevent an unauthorised action, investigate a failure and improve the process?

These questions should influence the architecture from the beginning.

As agents take on more consequential work, their useful autonomy will depend on the quality of the controls and evidence around them.

**Which part of your agent workflow is currently the most difficult to evaluate: the prediction, the plan, the handover or the action?**

## Selected publications and sources

- Shinn et al. (2023). [*Reflexion: Language Agents with Verbal Reinforcement Learning*](https://arxiv.org/abs/2303.11366).
- Yao et al. (2022; ICLR 2023). [*ReAct: Synergizing Reasoning and Acting in Language Models*](https://arxiv.org/abs/2210.03629).
- Wang et al. (2023). [*Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models*](https://arxiv.org/abs/2305.04091).
- Wu et al. (2023). [*AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation*](https://arxiv.org/abs/2308.08155).
- Huang et al. (2023; ICLR 2024). [*Large Language Models Cannot Self-Correct Reasoning Yet*](https://arxiv.org/abs/2310.01798).
- Lundberg and Lee (2017). [*A Unified Approach to Interpreting Model Predictions*](https://arxiv.org/abs/1705.07874).
- European Commission High-Level Expert Group on AI (2019). [*Ethics Guidelines for Trustworthy AI*](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai).
- European Union (2024). [*Regulation (EU) 2024/1689—the Artificial Intelligence Act*](https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng).

## Related notes

- [SHAP](../machine-learning/shap.md)
- [High-risk AI systems](../ai-act/high-risk-ai-systems.md)
- [Core design principles](core-design-principles.md)
- [Building resilient multi-agent systems](architecture-wars.md)

---

*22 September 2026.*
