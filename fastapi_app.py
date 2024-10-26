from fastapi import FastAPI
from simplifier.core import simplify_text
from pydantic import BaseModel

app = FastAPI()


class TextPayload(BaseModel):
    text: str
    leichte_sprache: bool = False


@app.post("/")
async def simplify(payload: TextPayload):
    simplified_text = simplify_text(payload.text, payload.leichte_sprache)
    return {"simplified_text": simplified_text}
