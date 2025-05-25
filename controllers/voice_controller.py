from fastapi import APIRouter, UploadFile, File, HTTPException
import whisper
import tempfile



router= APIRouter()

@router.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name

        model = whisper.load_model("base")
        result = model.transcribe(tmp_path)

        return {"text": result["text"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
