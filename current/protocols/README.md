# Current N3USYS Protocols

Operational protocols that express and implement the present-generation N3USYS framework belong here.

## Protocol lifecycle

```text
Intent
  ↓
Authority Check
  ↓
Constraint / Scope Definition
  ↓
Alignment
  ↓
Intelligence Processing
  ↓
Integrity / Verification
  ↓
Authorized Action or Output
  ↓
Audit
  ↓
Feedback / Correction
  └──────────────► Alignment
```

## Required protocol properties

Every current protocol should state:

- **Status** — proposed, experimental, current, deprecated, or superseded.
- **Scope** — what the protocol governs.
- **Authority** — who or what may invoke, modify, approve, or terminate it.
- **Inputs** — information required to operate it.
- **Constraints** — boundaries that remain active during operation.
- **Decision points** — conditions requiring evaluation or intervention.
- **Failure behavior** — what happens when integrity, authority, alignment, or capability fails.
- **Audit requirements** — what must be recorded.
- **Version** — the protocol's explicit revision identity.
- **Evidence** — supporting research or validation where applicable.

## Initial current protocol families

### Alignment
Maintains consistency between operator intent, active constraints, computational interpretation, and proposed execution.

### Integrity
Prevents unsupported claims, capability misrepresentation, and silent conversion of inference into fact.

### Authority
Defines operator control, permissions, approval boundaries, intervention, termination, and escalation.

### Execution
Defines the conditions under which computational outputs or actions may proceed.

### Correction
Defines recovery when the computational state, interpretation, or output diverges from operator intent or verified reality.

### Audit
Defines the minimum record necessary to reconstruct material control decisions and outcomes.

## Historical relationship

Earlier protocols such as the original Resonance Alignment Cycle and Empirical Integrity / Operator Corrective Action materials remain valuable lineage. They should be promoted into this directory only after their current applicability and revised semantics are explicitly established.
