from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

data = [
    {"name": "a", "marks": 97},
    {"name": "Y", "marks": 89},
    {"name": "X", "marks": 10}
]

@app.get("/api")
def get_marks(name: list[str] = []):
    name_to_marks = {item["name"]: item["marks"] for item in data}
    result = [name_to_marks.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})