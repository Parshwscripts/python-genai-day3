from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    response = client.chat.completions.create(
       model="llama-3.3-70b-versatile",

        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI assistant."
            },

            {
                "role": "user",
                "content": request.message
            }
        ]
    )

    ai_response = response.choices[0].message.content

    return {
        "response": ai_response
    }