# Diagram sources and exports

Each `.json` file is the editable source: labelled nodes, edges, positions and notes. `render.py` uses only the Python standard library to produce a standalone, readable `.svg` export with the same base name. Run `python3 docs/diagrams/render.py` after editing a source, then commit both. The three diagrams are initial design views, not evidence of implemented components.

- `context.json` / `context.svg`: people, EClever boundary and external LLM provider.
- `use-cases.json` / `use-cases.svg`: Student, Teacher and Administrator journeys. Association lines connect each actor to their use cases; the [requirements](../requirements-specification.md) specify behavior.
- `components.json` / `components.svg`: nine FastAPI modules plus web, CLI, runner, database and provider. Only principal calls are drawn to keep the view readable; the full acyclic call graph is in [architecture](../architecture.md).
