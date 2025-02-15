from fastapi import FastAPI, File, UploadFile
import shutil
import os
from services.caption_generator import generate_caption

app = FastAPI()

@app.post("/generate-caption/")
async def generate_image_caption():
    caption = generate_caption()
    return {"caption": caption}



UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_image(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "message": "Image uploaded successfully!"}
    # http://127.0.0.1:8000/docs



@app.get("/")
def read_root():
    return {"message": "Welcome to PromoEase AI API"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
    # uvicorn main:app --reload
    # http://127.0.0.1:8000
