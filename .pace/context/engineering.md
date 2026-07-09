---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest"
test_file_pattern: "**/*test*.py"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and project docs |
| src/audiosummarizer | Python | App composition, graph wiring |
| src/audiosummarizer/graph | Python | LangGraph graph builder |
| src/audiosummarizer/nodes | Python | Graph node implementations |
| src/audiosummarizer/state | Python | Typed state schema |
| src/audiosummarizer/ui | Python/INI | Streamlit UI config |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI components |
| src/audiosummarizer/LLMS | Python | LLM client wrapper |
| src/audiosummarizer/utils | Python | Token tracking utilities |
| .devcontainer | JSON | Devcontainer setup |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Audio/Video | moviepy, mutagen, ffmpeg |
| Env Config | python-dotenv |

## System Architecture
| Flow | Components | Notes |
|---|---|---|
| UI input | LoadStreamlitUI → st.file_uploader | Collects audio/video file, token usage |
| Processing | AudioGraphBuilder → nodes | audio_file → transcribe → summarize |
| Transcription | transcribe_node → ElevenLabs | Requires ELEVENLABS_API_KEY |
| Summarization | summarize_node → GeminiLLM | Requires GEMINI_API_KEY |
| Q&A | ChatInterface → GeminiLLM | Uses cached transcript/summary in session_state |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| AudioAnalysisState | audio_path:str, transcript:Optional[str], summary:Optional[str], audio_duration_seconds:Optional[float] |
| Env Vars | GEMINI_API_KEY, ELEVENLABS_API_KEY, GEMINI_MODEL (optional) |
| UI Config | src/audiosummarizer/ui/uiconfigfile.ini: PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |
| Entry Point | app.py → load_langgraph_agenticai_app() |

## Coding Conventions
| Area | Convention |
|---|---|
| UI error handling | Use st.error/st.warning with try/except in UI flows |
| State usage | Keep transcript/summary in st.session_state only |
| Separation | UI logic in ui/, graph logic in graph/ and nodes/ |
| Token tracking | Persist ElevenLabs usage in ~/.elevenlabs_token_usage.json via TokenTracker |
| API keys | Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls |

## Test Patterns
| Item | Details |
|---|---|
| Test infra | None detected (no tests configured) |
| Suggested runner | pytest (not configured) |