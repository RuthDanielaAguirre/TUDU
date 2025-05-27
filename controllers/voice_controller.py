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
        result = model.transcribe(tmp_path, language="es")

        return {"text": result["text"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# from fastapi import APIRouter, UploadFile, File, HTTPException
# import tempfile
# import speech_recognition as sr
#
# router = APIRouter()
#
# @router.post("/transcribe")
# async def transcribe_audio(file: UploadFile = File(...)):
#     try:
#         with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
#             tmp.write(await file.read())
#             tmp_path = tmp.name
#
#         recognizer = sr.Recognizer()
#         with sr.AudioFile(tmp_path) as source:
#             audio = recognizer.record(source)
#             text = recognizer.recognize_google(audio, language="es-ES")
#
#         return {"text": text}
#
#     except sr.UnknownValueError:
#         raise HTTPException(status_code=400, detail="No se pudo entender el audio")
#     except sr.RequestError as e:
#         raise HTTPException(status_code=503, detail=f"Error al conectarse con el servicio: {e}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
