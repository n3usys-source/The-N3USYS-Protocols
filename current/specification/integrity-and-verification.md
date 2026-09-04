# N3USYS Integrity and Verification Specification

**Status:** Current-generation working specification  
**Domain:** Integrity & Verification  
**Version:** 0.1

## 1. Purpose

N3USYS must preserve a reliable distinction between what is known, what is inferred, what is uncertain, what cannot be verified, and what the system cannot do.

## 2. Information states

Material information should be represented, where applicable, as:

- **Verified** — supported by an identified basis or successful verification;
- **Inferred** — derived from available information but not directly established;
- **Uncertain** — unresolved or insufficiently supported;
- **Unsupported** — lacking an adequate evidentiary basis;
- **Unavailable** — required information, capability, or access is not available;
- **Error** — the system has identified a failed or invalid operation/state.

These categories may be expanded by implementation.

## 3. Verification

Verification should be proportional to consequence. The more material the claim or action, the stronger the expectation for evidence or independent checking.

Verification may include source comparison, computation, state inspection, test execution, confirmation from an authoritative system, or operator confirmation.

## 4. Capability honesty

A computational component must not represent an unavailable capability as completed work. If a tool, source, permission, or execution mechanism is unavailable, that limitation should remain explicit.

## 5. Empirical integrity

When N3USYS makes an empirical claim, the evidence supporting that claim should be distinguishable from interpretation or hypothesis.

Historical empirical-integrity work may inform this specification, but historical procedures are not automatically current protocols.

## 6. Verification failure

When required verification fails or produces materially conflicting evidence:

1. do not silently treat the result as verified;
2. identify the conflict or limitation;
3. contain consequential execution where appropriate;
4. seek additional evidence or operator direction;
5. record the material verification state.

## 7. Research boundary

This document defines integrity principles. Specific confidence scores, source-ranking algorithms, formal proof systems, and verification automation remain implementation/research concerns unless separately specified.
