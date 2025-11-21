## Summary

| Category                 | Score | Notes                                                                 |
|--------------------------|-------|-----------------------------------------------------------------------|
| Code readability         | 7.0   | Clear module separation and docstrings; minor syntax/format issues.  |
| README quality           | 8.0   | Strong high-level overview and run instructions, aligned with task.  |
| Code cleanliness         | 7.5   | Good structure; a few config/entrypoint rough edges and small nits.  |
| Overall code quality     | 7.0   | Solid RAG design for the task; some ergonomics and polish missing.   |
| Answer accuracy (runtime)| 8.5   | 85.0% correct answers across 20 eval questions.                      |
| Page accuracy (runtime)  | 2.5   | 24.7% page-reference accuracy; relevant pages often mixed with noise.|

**Final Score (including runtime accuracy): 6.8/10**

## Parviz Pirizade – Step 1 Repository Assessment

### 1. Code readability

The codebase is generally readable, with a clear separation of responsibilities across modules and docstrings that explain most core functions in the RAG pipeline. Readability is somewhat hurt by inconsistent formatting, a few syntactic issues, and occasional mismatches between comments and actual behavior.

**Score:** 7/10

- **What's good**
  - Core RAG flow is easy to follow end-to-end: `main.py` → `pipeline.build_pipeline` → `retrieval`, `scoring`, and `utils` for table handling.
  - Most functions include short docstrings that make intent, required inputs, and outputs clear (e.g. in `extract_text.py`, `embeddings.py`, `env.py`, `retrieval.py`, and `utils.py`).

- **What's bad**
  - Inconsistent spacing, minor typos, and a few obvious syntax/structural issues (e.g. the closing parenthesis placement in `llm.py`, the non-f-string `print` in `build_vector_store.py`) break the visual flow and would prevent the code from running as-is.
  - Some docstrings or comments don’t fully match the implementation (for example, `create_llm` still mentions “DeepSeek-chat” while the code uses Gemini), which can confuse future readers.

### 2. README quality

The README clearly explains the end-to-end pipeline, pre-processing strategy (text, tables, diagrams), embedding choice, and provides concrete steps to build the vector store and run the FastAPI app. It also explicitly reflects on challenges and solutions, which aligns well with the task requirement to describe how the solution works and what trade-offs were made.

**Score:** 8/10

- **What's good**
  - Provides a high-level architecture description, including a visual diagram and a clear explanation of how preprocessing, retrieval, re-ranking, and generation fit together.
  - Setup instructions (clone, `.env`, `pip install -r requirements.txt`, `python build_vector_store.py`, and `uvicorn main:app`) are straightforward and sufficient to understand how to run the service for the given task.

### 3. Code cleanliness (structure, dead code, required files)

The project is structured cleanly into logical modules for document processing (`extract_text.py`, JSON assets), indexing (`build_vector_store.py`), retrieval/reranking (`retrieval.py`, `scoring.py`, `utils.py`, `pipeline.py`), and serving (`main.py`, `llm.py`, `env.py`, `embeddings.py`). There are a few rough edges around configuration and entrypoint expectations, but overall the repo feels like a focused MVP for the specified RAG API.

**Score:** 7.5/10

- **What's good**
  - Clear separation of concerns between offline preprocessing (PDF → JSON/tables), vector-store building, retrieval/reranking, and the FastAPI serving layer matches the task’s suggested architecture.
  - Configuration-sensitive parts (vector store path and Gemini API key) are correctly pulled from environment variables via `env.py`, keeping secrets and storage paths out of the core logic.

- **What's bad**
  - Required files check: `requirements.txt` is present and populated; `main.py` exists but is designed as a standard FastAPI module (served via `uvicorn main:app`) rather than something that runs the server when invoked with `python main.py`; `README.md` is present and detailed
  - There are a few signs of minor cleanliness issues (e.g. unused imports like `HuggingFaceEndpointEmbeddings` in `build_vector_store.py`, and hard-coded paths like `raw_documents/boeing_manual.pdf` in `extract_text.py`) that could be pulled into configuration for a more consistent style with the rest of the repo.

### 4. Overall code quality (for this RAG API MVP)

For the scope of this test task, the overall design is sound: preprocessing is clearly separated from retrieval, the retrieval stack uses a local MPNet-based Chroma store, and the pipeline composes retrieval, a custom title-based re-ranker, and table-to-HTML enrichment before hitting the LLM. A few correctness and ergonomics gaps (syntax issues in `llm.py`, lack of `.env.example`, and the mismatch with the “python main.py” requirement) keep it from feeling completely production-ready, but as an MVP it aligns well with the original problem.

**Score:** 7/10

- **What's good**
  - The RAG pipeline is thoughtfully constructed: similarity search, custom title-weighted reranking, and HTML conversion for tables are combined in `pipeline.build_pipeline` to better ground answers in the Boeing manual.
  - FastAPI models and response shape (`answer` + `pages`) directly match the task specification, and the page-number extraction logic in `main.py` correctly deduplicates and sorts referenced pages from document metadata.
  - Using a local `sentence-transformers/all-mpnet-base-v2` embedding model with Chroma and a Gemini LLM backend is a reasonable, clearly justified stack for this use case.

- **What's bad**
  - Obvious syntactic issues (notably in `llm.py`) and the lack of a `python main.py` server entrypoint mean the repo does not fully satisfy the “runs via python main.py” requirement without small but non-trivial fixes.
  - Some configuration and logging details (e.g. correct f-strings, clearer startup diagnostics, and a checked-in `.env.example`) are missing, which slightly reduces robustness and developer experience for this otherwise well-structured MVP.

---

**Model used for this assessment:** GPT-5.1

End Point Activated + 2025-11-21



## Step 3 – Retrieval & Answer Evaluation

Evaluated 20 questions; answer correctness=17/20 (85.0% YES), avg page correctness=2.47/10 (24.7% accuracy)

### Question-level summary

| Q | Question (abridged) | Answer correct | Page score |
|---|----------------------|----------------|------------|
| 1 | I'm calculating our takeoff weight for a dry runway. We'r... | YES | 2.50 |
| 2 | We're doing a Flaps 15 takeoff. Remind me, what is the fi... | YES | 1.67 |
| 3 | We're planning a Flaps 40 landing on a wet runway at a 1,... | YES | 1.67 |
| 4 | Reviewing the standard takeoff profile: After we're airbo... | YES | 5.00 |
| 5 | Looking at the panel scan responsibilities for when the a... | NO | 5.00 |
| 6 | For a standard visual pattern, what three actions must be... | YES | 2.00 |
| 7 | When the Pilot Not Flying (PNF) makes CDU entries during ... | YES | 1.67 |
| 8 | I see an amber "STAIRS OPER" light illuminated on the for... | YES | 2.00 |
| 9 | We've just completed the engine start. What is the correc... | YES | 2.00 |
| 10 | During the Descent and Approach procedure, what action is... | YES | 6.67 |
| 11 | We need to hold at 10,000 feet, and our weight is 60,000 ... | NO | 2.50 |
| 12 | I'm looking at the exterior light switches on the overhea... | YES | 1.67 |
| 13 | where exactly are the Logo Lights located on the airframe? | YES | 0.00 |
| 14 | I'm preparing for a Flaps 15 go-around. If our weight-adj... | YES | 2.00 |
| 15 | I'm holding the BCF (Halon) fire extinguisher. After I pu... | YES | 0.00 |
| 16 | I'm calculating my takeoff performance. The available run... | NO | 2.00 |
| 17 | I need to check the crew oxygen. There are 3 of us, and t... | YES | 2.00 |
| 18 | We're on an ILS approach. What three actions should I ini... | YES | 5.00 |
| 19 | What are the three available settings on the POSITION lig... | YES | 2.00 |
| 20 | Looking at the components of the passenger entry door, wh... | YES | 2.00 |
