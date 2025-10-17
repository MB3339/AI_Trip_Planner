# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # WHY: allow UI (e.g., Streamlit) to call API
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
import logging
import os

app = FastAPI(title="AI Trip Planner API")

# CORS (WHY: your Streamlit app on :8501 can hit this backend on :8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],          # tighten in prod (list exact origins)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/response models (WHY: validate input & document output)
class QueryRequest(BaseModel):
    query: str                    # keep the field name 'query'

class QueryResponse(BaseModel):
    answer: str

# Logging (WHY: better than print for real apps)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("trip_planner_api")

@app.post("/query", response_model=QueryResponse)
async def query_travel_agent(payload: QueryRequest):   # rename param to avoid query.query
    try:
        logger.info("Received question: %s", payload.query)

        # Build your agent graph
        graph = GraphBuilder(model="groq")
        agent_app = graph()

        # Optional: export the graph image (non-fatal if it fails)
        try:
            png_graph = agent_app.get_graph().draw_mermaid_png()
            with open("my_graph.png", "wb") as f:
                f.write(png_graph)
            logger.info("Graph saved as 'my_graph.png' in %s", os.getcwd())
        except Exception as e:
            logger.warning("Could not save graph PNG: %s", e)

        # Invoke the agent (WHY: use the validated payload field)
        messages = {"messages": [payload.query]}
        output = agent_app.invoke(messages)

        # Normalize output (WHY: handle dict vs str return shapes)
        if isinstance(output, dict) and "messages" in output:   # FIX: 'in', not 'is'
            msgs = output["messages"]
            final_output = msgs[-1].content if msgs else ""
        else:
            final_output = str(output)

        # Return JSON (WHY: FastAPI serializes pydantic model)
        return QueryResponse(answer=final_output)

    except Exception as e:
        logger.exception("Unhandled error in /query")
        raise HTTPException(status_code=500, detail=str(e))  # FIX: closes the try/except

# Optional local runner (WHY: lets you 'python main.py' during dev)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
