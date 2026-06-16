# 🎙️ MeetingMind AI

An end-to-end AI-powered meeting intelligence platform that automatically transcribes, summarizes, analyzes, and enables conversational search over meeting recordings.

## 🚀 Overview

MeetingMind AI transforms raw meeting recordings into actionable insights using Speech-to-Text, Large Language Models, Retrieval-Augmented Generation (RAG), and Vector Databases.

The system supports:

- 🎥 YouTube meeting recordings
- 🎧 Audio files (MP3, WAV, M4A)
- 🎬 Video files (MP4, MKV, AVI)

Users can upload a meeting recording or provide a YouTube URL and instantly receive:

- Accurate meeting transcripts
- AI-generated summaries
- Action items
- Key decisions
- Open questions
- Interactive chat with meeting content
- Exportable reports

---

## ✨ Features

### 🎤 Intelligent Transcription

#### English Meetings
- Uses OpenAI Whisper locally
- Completely free and offline
- High-quality speech recognition

#### Hindi & Hinglish Meetings
- Uses Sarvam AI Speech-to-Text
- Better support for Indian languages
- Handles code-switching conversations

---

### 📝 Meeting Summarization

Generates concise bullet-point summaries covering:

- Main discussion points
- Important updates
- Project progress
- Stakeholder inputs

---

### ✅ Action Item Extraction

Automatically identifies:

- Tasks assigned
- Responsible owners
- Deadlines (if mentioned)

Example:

| Task | Owner | Deadline |
|--------|--------|----------|
| Prepare project report | Rahul | Friday |
| Deploy API | Priya | Next Week |

---

### 🏛️ Key Decision Detection

Extracts important decisions made during meetings.

Example:

- Switch from MongoDB to PostgreSQL
- Use Docker for deployment
- Release MVP by end of month

---

### ❓ Open Questions & Follow-Ups

Identifies:

- Unresolved issues
- Pending discussions
- Required follow-ups

---

### 💬 Chat With Your Meeting

Powered by:

- LangChain LCEL
- ChromaDB
- HuggingFace Embeddings
- Mistral AI

Ask questions such as:

- What decisions were made?
- Who owns the deployment task?
- What is the project deadline?
- Summarize discussion about the API.

---

### 📄 Report Export

Generate downloadable:

- PDF Reports
- TXT Reports

Containing:

- Transcript
- Summary
- Action Items
- Decisions
- Open Questions

---

## 🛠️ Tech Stack

### Core Technologies

- Python

### Speech-to-Text

- OpenAI Whisper (Local)
- Sarvam AI

### LLM & AI

- Mistral AI
- LangChain LCEL

### RAG Pipeline

- ChromaDB
- HuggingFace Embeddings

### Frontend

- Streamlit

---

## 🏗️ Project Architecture

```text
Input Source
    │
    ├── YouTube URL
    └── Audio/Video File
              │
              ▼
      Audio Extraction
              │
              ▼
        Transcription
      ├── Whisper
      └── Sarvam AI
              │
              ▼
         Transcript
              │
              ▼
     AI Summarization
              │
              ▼
  Action Items / Decisions
              │
              ▼
      Vector Embeddings
              │
              ▼
         ChromaDB
              │
              ▼
       RAG Chat Engine
              │
              ▼
        User Queries
```

---

## 📂 Project Structure

```text
MeetingMind-AI/
│
├── app/
│   ├── app.py
│   ├── styles.py
│   └── __init__.py
│
├── src/
│   ├── core/
│   │   ├── extractor.py
│   │   ├── transcriber.py
│   │   ├── summarize.py
│   │   ├── rag_engine.py
│   │   └── vector_store.py
│   │
│   └── utils/
│       ├── audio_processor.py
│       ├── logger.py
│       ├── constants.py
│       └── config.py
│
├── downloads/
├── logs/
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Sumit-Prasad01/MeetingMind-AI.git
cd MeetingMind-AI
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SARVAM_API_KEY=your_key
MISTRAL_API_KEY=your_key
HF_TOKEN=your_key
HUGGINFACEHUB_API_TOKEN=your_token
```

---

## ▶️ Run Application

```bash
streamlit run app/app.py
```

---

## 💡 Example Workflow

1. Enter a YouTube URL or upload a meeting recording.
2. Choose language:
   - English
   - Hindi
   - Hinglish
3. Generate transcript.
4. View AI summary.
5. Extract action items and decisions.
6. Chat with meeting content.
7. Export report.

---

## 🎯 Use Cases

- Corporate Meetings
- Standups
- Client Calls
- Product Discussions
- Interview Recordings
- Academic Lectures
- Team Retrospectives

---

## 🔮 Future Enhancements

- Speaker Diarization
- Multi-Language Translation
- Meeting Analytics Dashboard
- Calendar Integration
- Slack Integration
- Email Summary Automation
- Cloud Deployment

---


