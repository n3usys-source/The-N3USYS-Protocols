# N3USYS Execution Model Specification

**Status:** Current-generation working specification  
**Domain:** Intelligence / Execution  
**Version:** 0.1

## 1. Purpose

The execution layer provides computational capability under N3USYS control. It may include models, agents, tools, services, scripts, external systems, or other computational mechanisms.

## 2. Capability versus authority

Capability and authority are separate properties.

A component may be capable of an action without being authorized to perform it. N3USYS must preserve this distinction throughout execution.

## 3. Execution modes

The current model distinguishes:

- **Analysis** — inspect, reason, calculate, classify, transform, or simulate;
- **Proposal** — produce a recommended action or result for evaluation;
- **Authorized execution** — perform an action within established authority and constraints.

Implementations may add additional modes.

## 4. Preconditions

Before consequential execution, the control layer should establish, as applicable:

- active intent;
- authority;
- scope;
- constraints;
- required approvals;
- relevant verification state;
- execution capability;
- expected outcome.

## 5. Execution boundaries

Execution should be bounded by least necessary scope. A task should not acquire additional permissions, resources, or external effects merely because they become technically convenient.

## 6. External effects

Actions affecting external systems or persistent state require explicit treatment as actions rather than being represented as ordinary reasoning output.

## 7. Failure

If execution fails, partially succeeds, or produces an unexpected effect, the system should preserve the known state, report the condition, contain further effects where appropriate, and return control to the control/alignment cycle.

## 8. Research boundary

This specification does not mandate a particular agent framework, tool protocol, sandbox, operating system, or automation platform. Those are implementation choices subject to the current control model.
