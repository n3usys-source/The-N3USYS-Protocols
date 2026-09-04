# Early-Generation Migration Manifest

This manifest maps the original repository layout to the v2 architecture. The first pass is intentionally conservative: historical material is preserved rather than rewritten.

| Existing artifact area | Intended v2 home | Treatment |
|---|---|---|
| `core/` conceptual framework summary | `archive/early-generation/documentation/` | Preserve as historical framework record; evaluate later for current concepts |
| `core/*.py` | `implementation/src/` or `archive/early-generation/implementations/` | Review code maturity and lineage before promotion |
| root `aurora_core.py` | `implementation/` or archive | Resolve relationship to `core/aurora_core.py` before consolidation |
| `assets/` | `implementation/prototypes/`, `diagrams/`, or `media/` | Classify individually by function |
| `docs/` | `current/`, `knowledge/`, `publication/`, or archive | Classify by normative status rather than filename |
| `knowledgebase/` | `knowledge/` | Preserve placeholders until content is reviewed |
| `logs/` | `research/logs/` | Historical experimental record |
| `tests/` | `research/validation/` and `research/experiments/` | These are protocol validation experiments, not ordinary unit tests |
| `whitepaper/` | `publication/whitepaper/` | Preserve generation and manuscript lineage |
| `wp/` | `archive/early-generation/legacy/` | Temporary/legacy material |
| `archive/` | `archive/early-generation/` | Preserve historical artifacts |
| `n3usys_protocols` | `knowledge/` or `current/terminology/` | Treat as an early index/glossary pending review |

## Migration policy

1. Preserve first.
2. Classify second.
3. Promote only after review.
4. Delete only when lineage is preserved elsewhere and the removal is intentional.
5. Never infer that a historical artifact is current merely because it has a descriptive or authoritative-sounding filename.