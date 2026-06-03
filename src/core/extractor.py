from src.config import settings

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_llm():

    return ChatMistralAI(
        model_name = "mistral-small-latest",
        api_key = settings.MISTRAL_API_KEY,
        temperature = 0.3
    )


def split_transcript(transcript: str) -> list:

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=3000,
        chunk_overlap=200
    )

    return splitter.split_text(transcript)



def build_chain(system_prompt : str):

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{text}"),
        ]
    )

    return (
        RunnablePassthrough                     |
        RunnableLambda(lambda x : {"text" : x}) |
        prompt                                  |
        llm                                     |
        StrOutputParser()
    )



def extract_action_items(transcript: str) -> str:

    # Map chain
    extraction_chain = build_chain(
        "You are an expert meeting analyst. From the meeting transcript, "
        "extract all action items. For each provide:\n"
        "- Task description\n"
        "- Owner (who is responsible)\n"
        "- Deadline (if mentioned, else write 'Not specified')\n\n"
        "Format as a numbered list. If none found say 'No action items found.'"
    )

    chunks = split_transcript(transcript)

    partial_results = [
        extraction_chain.invoke(chunk)
        for chunk in chunks
    ]

    combined_results = "\n\n".join(partial_results)

    # Reduce chain
    merge_chain = build_chain(
        "You are an expert meeting analyst. "
        "Combine action items extracted from multiple transcript chunks. "
        "Remove duplicates, merge similar tasks, and keep the most complete "
        "owner/deadline information. Return a final numbered list. "
        "If no valid action items exist, return 'No action items found.'"
    )

    return merge_chain.invoke(combined_results)




def extract_key_decisions(transcript: str) -> str:

    extraction_chain = build_chain(
        "You are an expert meeting analyst. From the meeting transcript, "
        "extract all key decisions made. Format as a numbered list. "
        "If none found say 'No key decisions found.'"
    )

    chunks = split_transcript(transcript)

    partial_results = [
        extraction_chain.invoke(chunk)
        for chunk in chunks
    ]

    combined_results = "\n\n".join(partial_results)

    merge_chain = build_chain(
        "You are an expert meeting analyst. "
        "Combine key decisions extracted from multiple transcript chunks. "
        "Remove duplicates, merge similar decisions, and return a final "
        "numbered list. If no valid decisions exist, return "
        "'No key decisions found.'"
    )

    return merge_chain.invoke(combined_results)




def extract_questions(transcript: str) -> str:

    extraction_chain = build_chain(
        "From the meeting transcript, extract all unresolved questions "
        "or topics needing follow-up. Format as a numbered list. "
        "If none found say 'No open questions found.'"
    )

    chunks = split_transcript(transcript)

    partial_results = [
        extraction_chain.invoke(chunk)
        for chunk in chunks
    ]

    combined_results = "\n\n".join(partial_results)

    merge_chain = build_chain(
        "You are an expert meeting analyst. "
        "Combine unresolved questions and follow-up topics extracted "
        "from multiple transcript chunks. Remove duplicates, merge "
        "similar questions, and return a final numbered list. "
        "If no valid questions exist, return "
        "'No open questions found.'"
    )

    return merge_chain.invoke(combined_results)