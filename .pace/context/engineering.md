---
language: python
package_manager: pip
test_runner: none
test_command: "n/a"
test_file_pattern: "n/a"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and repo config |
| src/audiosummarizer | Python | Audio summarizer application package |
| src/audiosummarizer/graph | Python | LangGraph graph builder |
| src/audiosummarizer/nodes | Python | Graph nodes for file handling, transcription, summarization |
| src/audiosummarizer/state | Python | Typed state for graph execution |
| src/audiosummarizer/LLMS | Python | LLM client wrappers |
| src/audiosummarizer/ui | Python | UI config and Streamlit UI components |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI screens and chat |
| src/audiosummarizer/utils | Python | Token usage tracking utilities |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Orchestration | LangGraph |
| Audio/Video Processing | moviepy, mutagen, ffmpeg (external) |
| Env Config | python-dotenv |

## System Architecture
| Step | Description |
|---|---|
| 1 | app.py runs load_langgraph_agenticai_app() to start Streamlit app |
| 2 | LoadStreamlitUI collects file upload and process click |
| 3 | _process_audio_file writes temp file and builds LangGraph via AudioGraphBuilder |
| 4 | Graph executes: audio_file -> transcribe (ElevenLabs) -> summarize (Gemini) |
| 5 | DisplayResultStreamlit renders transcript, summary, and ChatInterface Q&A |

## Key Interfaces & Contracts
| Interface | Location | Details |
|---|---|---|
| Streamlit entry | app.py | Calls load_langgraph_agenticai_app() |
| Graph API | src/audiosummarizer/graph/audio_graph.py | StateGraph(AudioAnalysisState) with START->audio_file->transcribe->summarize->END |
| State schema | src/audiosummarizer/state/audio_state.py | audio_path, transcript, summary, audio_duration_seconds |
| Config file | src/audiosummarizer/ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS, GROQ_MODEL_OPTIONS |
| LangGraph config | src/audiosummarizer/langgraph.json | graph entrypoint ./main.py:graph |

## Coding Conventions
| Topic | Details |
|---|---|
| Error handling | Streamlit UI uses st.error/st.warning with try/except in processing and duration checks |
| Env vars | GEMINI_API_KEY required, ELEVENLABS_API_KEY required, GEMINI_MODEL optional |
| Token tracking | TokenTracker persists JSON file in user home |

## Test Patterns
| Item | Details |
|---|---|
| Test framework | None detected |
| Test location | n/a |
| Execution | n/a |
