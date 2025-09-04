from fastapi import FastAPI
from pydantic import BaseModel
from agent.agentic_workflow import GraphBuilder
from fastapi.responses import JSONResponse
import os

app = FastAPI()


class QueryRequest(BaseModel):
    query: str

@app.post("/query")

async def query_travel_agent(query:QueryRequest):
    try:
        print(query)
        graph=GraphBuilder(model="groq")
        react_app=graph()

        png_graph=react_app.get_graph().draw_mermaid_png()
        with open ("my_graph.png",'wb')as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")
        
        # Assuming request is pydantic object.

        messages={"messages":[query.question]}
        output=react_app.invoke(messages)

        #if the result in dict with message:

        if isinstance(output,dict) and 'messages'is output:
            final_output=output['messages'][-1].content # last AI response

        else:
            final_output=str(output)
            