from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # デモ用。必要に応じてStreamlitのドメインに絞る
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    print("health")
    return {"ok": True}

@app.get("/echo")
def echo(q: str = "hello"):
    print(f"echo: {q}")
    return {"echo": q}

