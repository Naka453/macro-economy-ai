\# Macro Economy AI Agent



AI assistant for Mongolia's macroeconomic analysis powered by GPT-5.5 and OpenAI Vector Store.



\## Features



\- GPT-5.5 Responses API

\- OpenAI Vector Store

\- FastAPI

\- Production Prompt Architecture

\- Retrieval-Augmented Generation (RAG)



\## Tech Stack



\- Python

\- FastAPI

\- OpenAI SDK

\- Uvicorn



\## Installation



```bash

pip install -r requirements.txt

```



Create a `.env` file:



```env

OPENAI\_API\_KEY=your\_api\_key

VECTOR\_STORE\_ID=your\_vector\_store\_id

```



Run:



```bash

uvicorn app.main:app --reload

```

