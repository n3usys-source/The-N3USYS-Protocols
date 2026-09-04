# N3USYS — Current Architecture

**Status:** Current-generation working architecture  
**Authority:** This directory defines the present-generation N3USYS framework.  
**Historical material:** Earlier generations remain preserved outside `/current/`.

## Purpose

N3USYS is a control architecture for Human–AI Joint Agency. It structures the relationship between operator intent, computational intelligence, constraints, verification, execution, correction, and audit.

N3USYS is not itself a language model, application UI, or single autonomous agent. It is an architectural/control layer governing how intelligence is directed, constrained, evaluated, corrected, and kept subordinate to legitimate operator authority.

## Core doctrine

1. **Operator Primacy** — the operator remains the authoritative source of mission intent and retains final authority over consequential action.
2. **Intent before execution** — objectives, constraints, permissions, and success conditions are established before execution where practical.
3. **Continuous alignment** — alignment is maintained throughout a session or operation rather than assumed from initialization.
4. **Verification where material** — consequential claims, state, assumptions, and actions are checked against available evidence and capability boundaries.
5. **Explicit uncertainty** — verified fact, inference, uncertainty, unavailable capability, and speculation are not silently conflated.
6. **Authoritative correction** — operator correction causes re-evaluation and re-alignment rather than defensive persistence of an erroneous state.
7. **Auditability** — material decisions, transitions, violations, corrections, evidence, and outcomes should be reconstructible.
8. **Containment before escalation** — when authority, integrity, or alignment is uncertain, reduce scope and seek clarification rather than silently expanding action.

## Architectural flow

```text
                       OPERATOR
                          │
                          ▼
                ┌──────────────────┐
                │ AUTHORITY +      │
                │ INTENT           │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ N3USYS CONTROL   │
                │ / COORDINATION   │
                └────────┬─────────┘
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
         ALIGNMENT   INTEGRITY   CONSTRAINTS
              │          │          │
              └──────────┼──────────┘
                         ▼
                ┌──────────────────┐
                │ INTELLIGENCE /   │
                │ EXECUTION        │
                └────────┬─────────┘
                         │
                         ▼
                    OUTPUT/ACTION
                         │
                         ▼
                   VERIFY + AUDIT
                         │
                         └──────────► OPERATOR
```

## Current subsystem model

### 1. Operator Authority Layer
Defines authority, permissions, approval boundaries, escalation rights, and termination/redirect authority.

### 2. Intent & Mission Layer
Represents the operator's objective, desired state, constraints, priorities, permissions, and success conditions.

### 3. Coordination / Control Layer
Maintains active control state and routes intent, context, constraints, tasks, proposals, and feedback among the operator and computational components.

### 4. Alignment Layer
Continuously evaluates whether processing and proposed execution remain consistent with operator intent, constraints, and known state.

### 5. Integrity & Verification Layer
Separates verified information from inference, uncertainty, unavailable capability, and unsupported claims. It provides correction and empirical-integrity mechanisms.

### 6. Intelligence / Execution Layer
The model, agent, toolchain, or other computational capability performing analysis or proposing/performing actions. This layer operates within N3USYS control boundaries.

### 7. Audit / Feedback Layer
Records material decisions, evidence, state transitions, violations, corrections, and outcomes to support accountability and iterative improvement.

## Relationship to earlier N3USYS concepts

Earlier generations used terms including **Intent Lattice**, **Resonance Engine**, **Resonance Alignment Cycle (RAC)**, **Operator Primacy Enforcement (OPE)**, and **Cognitive Execution Layer (CEL)**. Those concepts remain part of the historical lineage and may inform current research, but their historical definitions are not automatically authoritative for the present architecture.

The current architecture deliberately separates enduring principles from implementation-specific vocabulary developed during earlier iterations.

## Research posture

This is a **working research architecture**. It is not a claim that every component is experimentally validated, production-ready, or implemented in software. Normative doctrine, empirical evidence, and implementation status must remain distinguishable.

## Related systems

N3USYS is intended to provide architectural foundations for later systems and research programs, including Sentinel-oriented command/control work such as **SSC-01**, and other N3USYS Institute projects.

## Directory map

- `specification/` — normative framework definitions
- `protocols/` — operational protocols and required behaviors
- `architecture/` — component and interaction models
- `terminology/` — controlled vocabulary and versioned meanings
- `EVOLUTION.md` — architectural lineage and transition history
