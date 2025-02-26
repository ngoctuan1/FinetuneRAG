import json
from fastapi import FastAPI
from pydantic import BaseModel
from ragatouille import RAGPretrainedModel

app = FastAPI()

class MessageRequest(BaseModel):
    content: str

class MessageReponse(BaseModel):
    content: str
    source: str
    page: str

RAG = RAGPretrainedModel.from_index("/home/anga/Tuannn55/github/Data_Agent_Example/.ragatouille/colbert/indexes/index_for_full_doc")

@app.post("/chat")
async def chat(message: MessageRequest):
    results = RAG.search(message.content)
    json.dump(results, open("results.json", "w"), indent=4, ensure_ascii=False)
    top_1 = results[0]
    document = top_1['document_id'].split("_")
    response = MessageReponse(content=top_1['content'], source = document[0], page=document[1] if len(document) > 1 else "0")
    return response
