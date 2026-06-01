import whisper

from src.config import settings
from src.logger import logger

_model = None


def load_model():

    global _model

    if _model is None:
        logger.info(f"Loding model...")

        _model = whisper.load_model(settings.WHISPER_MODEL)
        logger.info("Whisper model loaded successfully.")

    
    return _model



def transcribe_chunk(chunk_path : str, translate : bool = False) -> str:

    model = load_model()

    task = "translate" if translate else "transcribe"

    result = model.transcribe(chunk_path, task = task)

    return result['text']



def transcribe_all(chunks : list, translate : bool = False):

    full_transcript = ""

    for i, chunk in enumerate(chunks):
        logger.info(f"Transcribing chunk {i+1}")

        text = transcribe_chunk(chunk, translate = translate)

        full_transcript += text + " "

    logger.info("Transcription completed")

    return full_transcript