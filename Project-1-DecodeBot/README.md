# DecodeBot - Deterministic Rule-Based AI Assistant

DecodeBot is a demonstration project built for DecodeLabs AI Internship Project 1. It showcases a purely deterministic "Rule-Based Logic Engine" without using generative AI or machine learning models.

## Concept Overview
- **Deterministic AI:** Given the exact same input, DecodeBot guarantees the exact same output. There is zero hallucination or probabilistic guessing.
- **White-Box System:** DecodeBot features a built-in Logic Trace. Users can trace exactly why a specific output was produced from a specific input.
- **INPUT → LOGIC → OUTPUT:** The pipeline intercepts the user input, validates it against guardrails, normalizes it, scores it against predefined keyword rules, and returns a predefined response.

## Features
- **Logic Trace UI:** Visually explains the backend routing and keyword match prioritization.
- **Rule-Based Guardrails:** Intercepts excessively long, empty, or blocked inputs before they reach the logic engine.
- **50+ Predefined Topics:** Detailed knowledge base covering programming, frameworks, tools, and computer science concepts.
- **Premium Tech UI:** Dark charcoal, cyan, and teal aesthetics implemented via Tailwind CSS.

## Tech Stack
- **Frontend:** React, Vite, Tailwind CSS, Framer Motion
- **Backend:** Python, Flask

## Running Locally

### Backend
1. `cd backend`
2. `python -m venv venv`
3. `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. `pip install -r requirements.txt`
5. `python app.py` (Runs on `http://localhost:5000`)

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev` (Runs on `http://localhost:5173`)

## Testing
Run the deterministic test suite:
```bash
cd tests
pytest test_engine.py
```

## Future Scope
This Rule Engine could serve as a deterministic guardrail layer *wrapping* a probabilistic LLM (like GPT-4). The rule engine would handle predictable, high-risk queries safely, falling back to the LLM for creative/generative requests.
