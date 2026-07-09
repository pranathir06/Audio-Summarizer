---
language: python
package_manager: pip
test_runner: n/a
test_command: n/a
test_file_pattern: n/a
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and project metadata |
| src/audiosummarizer | Python | App orchestration and LangGraph setup |
| src/audiosummarizer/graph | Python | LangGraph builder for audio pipeline |
| src/audiosummarizer/nodes | Python | Graph node implementations |
| src/audiosummarizer/state | Python | Typed state schema for graph |
| src/audiosummarizer/LLMS | Python | Gemini LLM wrapper |
| src/audiosummarizer/ui | Python/INI | UI config and Streamlit UI modules |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI screens and chat |
| src/audiosummarizer/utils | Python | Token usage tracking |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media processing | moviepy, mutagen, ffmpeg |
| Env config | python-dotenv |

## System Architecture
| Step | Component | Interaction |
|---|---|---|
| 1 | Streamlit UI | Upload audio/video file and trigger processing |
| 2 | AudioGraphBuilder | Builds LangGraph: audio_file → transcribe → summarize |
| 3 | transcribe_node | Calls ElevenLabs API; may extract audio from video |
| 4 | summarize_node | Calls Gemini LLM with transcript prompt |
| 5 | DisplayResultStreamlit | Shows transcript, summary, and chat |
| 6 | ChatInterface | Uses existing transcript+summary to answer questions via Gemini |
| 7 | TokenTracker | Persists ElevenLabs usage in ~/.elevenlabs_token_usage.json |

## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| AudioAnalysisState | src/audiosummarizer/state/audio_state.py | audio_path, transcript, summary, audio_duration_seconds |
| Graph builder | src/audiosummarizer/graph/audio_graph.py | audio_summarizer_build_graph(): START→audio_file→transcribe→summarize→END |
| Transcription | src/audiosummarizer/nodes/transcribe_node.py | ELEVENLABS_API_KEY required; diarization enabled |
| Summarization | src/audiosummarizer/nodes/summarize_node.py | Gemini model invoked with structured summary prompt |
| Chat Q&A | src/audiosummarizer/ui/streamlitui/chat_interface.py | Uses transcript+summary from session_state |
| Config | src/audiosummarizer/ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |
| Env vars | README.md | GEMINI_API_KEY, ELEVENLABS_API_KEY, optional GEMINI_MODEL |

## Coding Conventions
| Convention | Source |
|---|---|
| Use st.error/st.warning in UI try/except | AGENTS.md |
| Keep UI logic in ui/ and graph logic in graph/ and nodes/ | AGENTS.md |
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls | AGENTS.md, geminillm.py |
| Respect AudioAnalysisState fields | AGENTS.md |
| Persist token usage via TokenTracker JSON in user home | AGENTS.md, token_tracker.py |

## Test Pa