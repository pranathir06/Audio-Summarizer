---
language: python
package_manager: pip
test_runner: pytest
test_command: "n/a"
test_file_pattern: "n/a"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and repo metadata |
| src/audiosummarizer | Python | Audio summarizer package root |
| src/audiosummarizer/LLMS | Python | LLM client wrappers (Gemini) |
| src/audiosummarizer/graph | Python | LangGraph construction |
| src/audiosummarizer/nodes | Python | LangGraph node implementations |
| src/audiosummarizer/state | Python | Typed state schema |
| src/audiosummarizer/ui | Python | UI config and Streamlit UI package |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI components |
| src/audiosummarizer/utils | Python | Utilities (token tracking) |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph (langgraph) |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Audio/Video | moviepy, mutagen, ffmpeg (external) |
| Env Config | python-dotenv |

## System Architecture
| Step | Component | Interaction |
|---|---|---|
| 1 | app.py | Calls load_langgraph_agenticai_app() |
| 2 | LoadStreamlitUI | Collects file upload + process click; shows token usage |
| 3 | AudioGraphBuilder | Builds LangGraph: audio_file → transcribe → summarize |
| 4 | transcribe_node | Calls ElevenLabs API; extracts audio if video |
| 5 | summarize_node | Calls Gemini LLM with structured prompt |
| 6 | DisplayResultStreamlit | Renders transcript, summary, and chat |
| 7 | ChatInterface | Answers Q&A using transcript + summary via Gemini |

## Key Interfaces & Contracts
| Interface | Location | Details |
|---|---|---|
| Streamlit entry | app.py | load_langgraph_agenticai_app() |
| State schema | src/audiosummarizer/state/audio_state.py | AudioAnalysisState: audio_path, transcript, summary, audio_duration_seconds |
| Graph build | src/audiosummarizer/graph/audio_graph.py | AudioGraphBuilder.setup_graph(usecase) |
| LLM config | src/audiosummarizer/LLMS/geminillm.py | GEMINI_API_KEY, GEMINI_MODEL (default gemini-2.5-flash) |
| UI config | src/audiosummarizer/ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |
| Token tracking | src/audiosummarizer/utils/token_tracker.py | ~/.elevenlabs_token_usage.json |

## Coding Conventions
| Rule | Source |
|---|---|
| Use Streamlit error handling with try/except in UI flows | AGENTS.md |
| Keep Streamlit UI logic in ui/ modules; graph logic in graph/ and nodes/ | AGENTS.md |
| Respect AudioAnalysisState fields and names | AGENTS.md / audio_state.py |
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external APIs | AGENTS.md / geminillm.py / transcribe_node.py |

## Test Patterns
| Item | Details |
|---|---|
| Test status | No test infrastructure documented (AGENTS.md: "How to Run Tests n/a") |
| Expected command | n/a |
| Test files | n/a |
