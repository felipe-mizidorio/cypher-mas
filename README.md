# cypher-mas

cypher-mas is a hierarchical multi-agent system for collaborative defect diagnosis in industrial assembly lines. Agents are organized in three layers — Point, Station, and Inter-Station — each powered by an LLM that reasons over statistical tool outputs to produce interpretable, natural-language diagnostic reports.

Built with [LangGraph](https://github.com/langchain-ai/langgraph) and designed to be domain-agnostic.

---

## Dependencies

| Package | Role |
|---|---|
| `langgraph` | Agent orchestration and graph execution |
| `langchain-anthropic` | Claude LLM integration |
| `pydantic` | Data validation and state schemas |
| `python-dotenv` | Environment variable loading |

Dev dependencies: `ruff`, `pyright`, `pytest`, `pytest-asyncio`, `pre-commit`.

Requires **Python 3.12+** and [uv](https://github.com/astral-sh/uv).

---

## Installation

```bash
# Clone the repo
git clone https://github.com/felipemerenda1/cypher-mas.git
cd cypher-mas

# Install dependencies
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY
```

---

## Project Structure

```
cypher-mas/
├── src/
│   └── cypher_mas/
│       ├── agents/       # Point, Station, and Inter-Station agent definitions
│       ├── graph/        # LangGraph graph construction and execution logic
│       ├── models/       # Pydantic state and data models
│       ├── tools/        # Statistical diagnostic tools used by agents
│       ├── config.py     # Configuration and environment loading
│       └── __init__.py
├── .env.example
├── pyproject.toml
└── README.md
```
