# Current N3USYS Architecture

The current architecture models N3USYS as a control plane between legitimate operator intent and computational intelligence/execution.

```text
                         OPERATOR
                            │
                 authority + intent
                            │
                            ▼
                ┌─────────────────────┐
                │  N3USYS CONTROL     │
                │  PLANE              │
                ├─────────────────────┤
                │ Authority           │
                │ Intent / Mission    │
                │ Coordination        │
                │ Alignment           │
                │ Integrity           │
                │ Constraints         │
                │ Audit / Feedback    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ INTELLIGENCE /      │
                │ EXECUTION PLANE     │
                │                     │
                │ Models • Agents     │
                │ Tools • Services    │
                │ Computation         │
                └──────────┬──────────┘
                           │
                           ▼
                    proposal / action
                           │
                           ▼
                     verify + audit
                           │
                           └──────► operator
```

## Component responsibilities

| Component | Responsibility |
|---|---|
| Operator Authority | Establishes legitimate authority and approval boundaries |
| Intent / Mission | Represents objective, desired state, constraints, priorities, permissions, success criteria |
| Coordination | Maintains control state and routes context, tasks, proposals, and feedback |
| Alignment | Detects drift between active intent, constraints, state, and computational behavior |
| Integrity | Governs evidence, uncertainty, capability boundaries, and unsupported claims |
| Constraints | Limits what may be proposed or executed within the active mission |
| Intelligence / Execution | Performs computation, analysis, recommendation, transformation, or authorized action |
| Audit / Feedback | Records material decisions, evidence, corrections, transitions, and outcomes |

## Control-plane principle

The intelligence layer is a capability provider, not the ultimate authority. N3USYS governs the conditions under which intelligence is interpreted and used.

## Architectural distinction

Conceptual components in this document are not claims about a specific software implementation. Implementations belong in `/implementation/` and should identify which architectural responsibilities they actually satisfy.
