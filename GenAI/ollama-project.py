from fastapi import FastAPI, Body
from ollama import Client
app = FastAPI()
client = Client(
    host = "http://localhost:11434"
)
@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.post("/chat")
def chat(
        message : str = Body(..., description="The Message")
):
    response = client.chat(model = "qwen2.5-coder:3b", messages = [
        {"role" : "user", "content" : message}
    ])
    return {"response" : response.message.content}
