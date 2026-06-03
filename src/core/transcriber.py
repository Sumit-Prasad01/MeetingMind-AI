import os
import whisper
from pydub import AudioSegment

from src.config import settings
from src.logger import logger
from src.constants import SARVAM_PIECE_SECONDS

_model = None


def load_model():

    global _model

    if _model is None:
        logger.info(f"Loding model: {settings.WHISPER_MODEL} ...")

        _model = whisper.load_model(settings.WHISPER_MODEL)
        logger.info("Whisper model loaded successfully.")

    
    return _model



def transcribe_chunk_whisper(chunk_path : str) -> str:

    model = load_model()
    result = model.transcribe(chunk_path, task = "transcribe")

    return result["text"]



def _send_to_sarvam(piece_path : str) -> str:
    """Send one ≤30s WAV file to Sarvam and return the English transcript."""

    headers = {
        "api-subscription-key" : settings.SARVAM_API_KEY
    }

    with open(piece_path, "rb") as f:
        files = {
            "file" : (os.path.basename(piece_path), f, "audio/wav")
        }

        data = {
            "model" : settings.SARVAM_STT_MODEL,
            "with_diarization" : False
        }
        
        response = response.post(
            settings.SARVAM_STT_TRANSLATE_URL,
            headers = headers,
            files = files,
            data = data,
            timeout = 120
        )

        if not response.ok:
            logger.info(f"\n Sarvam returned {response.status_code}")
            logger.info(f"Response body: {response.text}\n")

            response.raise_for_status()

        return response.json().get("transcript", "")



def transcribe_chunk_sarvam(chunk_path : str) -> str:
    """
    Sarvam sync API only accepts ≤30s audio. We split this chunk into
    25-second pieces, send each seperatly, and join the transcripts.
    """

    if not settings.SARVAM_API_KEY:
        logger.error("SARVAM API KEY not found!")

        raise RuntimeError("SARVAM_API_KEY is not set in environment / .env")
    

    audio = AudioSegment.from_wav(chunk_path)
    piece_ms = SARVAM_PIECE_SECONDS * 1000

    full_text = ""
    total_pieces = (len(audio) + piece_ms - 1) // piece_ms

    for i, start in enumerate(range(0, len(audio), piece_ms)):
        piece = audio[start: start + piece_ms]
        piece_path = f"{chunk_path}_sv_{i}.wav"
        piece.export(piece_path, format = "wav")

        try:
            logger.info(f" → Sarvam piece {i+1}/{total_pieces} ...")
            full_text += _send_to_sarvam(piece_path) + " "

        finally:
            if os.path.exists(piece_path):
                os.remove(piece_path)


    return full_text.strip()




def transcribe_chunk(chunk_path : str, language : str = "english") -> str:
    """
    Route one chunk to Whisper or Sarvam depending on language choice.
    - english  → Whisper (local model)
    - hinglish → Sarvam (translates to English while transcribing)
    """

    if language.lower() == "hinglish":
        return transcribe_chunk_sarvam(chunk_path)
    
    return transcribe_chunk_whisper(chunk_path)




def transcribe_all(chunks : list, language : str = "english") -> str:

    full_transcript = ""

    engine = "Sarvam AI" if language.lower() == "hinglish" else "Whisper"
    logger.info(f"Using {engine} for transcriptions.")

    for i, chunk in enumerate(chunks):

        logger.info(f"Transcribing chunk {i+1/len(chunks)} ...")

        text = transcribe_chunk(chunk, language = language)

        full_transcript += text + " "

    
    logger.info("Transcription complete")

    return full_transcript.strip()