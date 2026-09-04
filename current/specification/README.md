# Current N3USYS Specification

This directory contains the **normative layer** of the present-generation N3USYS framework.

## Scope

The specification defines what N3USYS is required to mean and how its control architecture is intended to behave. It does not claim that every specified capability is currently implemented or experimentally validated.

## Normative domains

### Operator Authority
The operator establishes legitimate intent, permissions, constraints, priorities, and consequential approval boundaries. N3USYS must preserve operator authority rather than replace it.

### Intent
Intent is the structured representation of what the operator is trying to accomplish, including objective, context, constraints, priorities, permissions, and success conditions where applicable.

### Control
N3USYS maintains control state between operator intent and computational execution. Control includes routing, constraint propagation, state management, intervention, and escalation.

### Alignment
Alignment is the continuing assessment that computational processing and proposed execution remain consistent with active operator intent and constraints.

### Integrity
The system must distinguish verified information, inference, uncertainty, unsupported claims, unavailable capabilities, and system error. Material uncertainty must not be represented as established fact.

### Execution
Computational intelligence may analyze, recommend, transform, or execute within explicitly defined authority and constraint boundaries. Intelligence capability does not itself confer authority.

### Correction
Operator correction has precedence over a conflicting computational interpretation, subject to explicit authority and safety constraints. Correction should cause state re-evaluation and alignment recovery.

### Audit
Material actions and decisions should be traceable to the relevant intent, authority, evidence, constraints, and resulting outcome.

## Normative status

A document belongs here only when it is intentionally established as current doctrine. Experimental observations belong in `/research/`; historical doctrine belongs in `/archive/early-generation/`.

## Current principle set

**Operator Primacy · Intent Integrity · Continuous Alignment · Explicit Uncertainty · Verified Execution · Authoritative Correction · Auditability · Controlled Escalation**
