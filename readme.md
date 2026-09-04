# N3USYS Protocols

## Repository Status — Historical Foundation + v2 Transition

This repository contains an **early-generation implementation and documentation of the N3USYS Protocols** together with the beginning of a new v2 organizational structure.

The N3USYS framework has evolved substantially since many of the original materials in this repository were created. Therefore, historical protocols, terminology, experiments, and implementations **must not be assumed to represent the current N3USYS architecture**.

### Authority model

- `/current/` — authoritative location for the present-generation framework as it is formalized.
- `/research/` — experimental and validation evidence.
- `/implementation/` — software implementations and experimental code.
- `/knowledge/` — terminology, concepts, and reference material.
- `/publication/` — material prepared for external publication.
- `/archive/early-generation/` — historical material retained for lineage and reproducibility.

The original top-level directories remain temporarily in place during this transition so that no historical artifact is silently lost. A migration manifest records the intended disposition of each existing artifact.

## N3USYS in one sentence

N3USYS is an evolving control architecture for Human–AI Joint Agency centered on Operator Primacy, structured intent, alignment, verification, and controlled cognitive execution.

## Evolution matters

The repository should be read as a **lineage**, not as a frozen v1 specification. The early lattice/resonance work, protocol experiments, empirical-integrity work, and implementation prototypes are part of the development history from which the present architecture emerged.

See:

- [`current/README.md`](current/README.md)
- [`current/EVOLUTION.md`](current/EVOLUTION.md)
- [`research/README.md`](research/README.md)
- [`archive/early-generation/README.md`](archive/early-generation/README.md)
- [`archive/early-generation/MIGRATION-MANIFEST.md`](archive/early-generation/MIGRATION-MANIFEST.md)

## Historical note

The original README and early protocol artifacts remain important historical records. They should not be rewritten merely to make them agree with later N3USYS concepts. Where terminology or architecture has changed, the newer material should supersede the old material by explicit versioning and lineage.

## Development principle

> **Experiments may challenge the specification; they do not silently redefine it.**

N3USYS development is therefore organized around a distinction between:

1. **Normative** — what the current framework specifies.
2. **Empirical** — what experiments and validation actually demonstrate.
3. **Implementational** — what software currently implements.
4. **Historical** — what earlier generations proposed or tested.

That distinction is now part of the repository architecture.

## License

See [`LICENSE`](LICENSE).
