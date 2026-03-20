from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, FileResponse
import os

app = FastAPI()

FREE_DIR = os.path.join(os.path.dirname(__file__), "..", "free")

@app.get("/free/{filename}")
async def serve_free_file(filename: str):
    file_path = os.path.join(FREE_DIR, filename)
    if not os.path.exists(file_path):
        return PlainTextResponse("Not found", status_code=404)
    return FileResponse(file_path, media_type="text/plain")
