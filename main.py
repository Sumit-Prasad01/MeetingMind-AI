from src.utils.audio_processor import process_audio
from src.core.transcriber import transcribe_all
from src.core.summarize import summarize, generate_title
from src.core.extractor import extract_action_items, extract_key_decisions, extract_questions
from src.core.rag_engine import build_rag_chain, ask_question

from src.logger import logger


def run_pipeline(source : str, language : str =  "english") -> dict:

    logger.info("Starting AI Video Assistant")

    chunks = process_audio(source)
    transcript = transcribe_all(chunks, language = language)

    logger.info(f"Raw transcription (first 300 characters) : {transcript[:300]}")

    title = generate_title(transcript)
    summary = summarize(transcript)

    action_items = extract_action_items(transcript)
    decisions = extract_key_decisions(transcript)
    questions = extract_questions(transcript)

    rag_chain = build_rag_chain(transcript)

    return {
        "title": title,
        "transcript": transcript,
        "summary": summary,
        "action_items": action_items,
        "key_decisions": decisions,
        "open_questions": questions,
        "rag_chain": rag_chain,
    }



if __name__ == "__main__":

    source = input("Enter YouTube URL or local file path: ").strip()
    language = input("Language (english/hinglish): ").strip().lower() or "english"
    result = run_pipeline(source, language)

    logger.info("\n" + "=" * 60)
    logger.info(f"📌 Title: {result['title']}")
    logger.info(f"\n📋 Summary:\n{result['summary']}")
    logger.info(f"\n✅ Action Items:\n{result['action_items']}")
    logger.info(f"\n🔑 Key Decisions:\n{result['key_decisions']}")
    logger.info(f"\n❓ Open Questions:\n{result['open_questions']}")
    logger.info("=" * 60)

    # Phase 2 — Chat with your meeting via RAG
    logger.info("\n💬 Chat with your meeting (type 'exit' to quit)\n")
    rag_chain = result["rag_chain"]
    while True:
        question = input("You: ").strip()
        if question.lower() in ["exit", "quit", "q"]:
            logger.info("👋 Goodbye!")
            break
        if not question:
            continue
        answer = ask_question(rag_chain, question)
        logger.info(f"\n🤖 Assistant: {answer}\n")