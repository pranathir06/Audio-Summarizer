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
| . | Python | Streamlit entrypoint and project metadata |
| src/audiosummarizer | Python | Audio summarizer package root |
| src/audiosummarizer/LLMS | Python | LLM client wrappers |
| src/audiosummarizer/graph | Python | LangGraph graph construction |
| src/audiosummarizer/nodes | Python | Graph node implementations |
| src/audiosummarizer/state | Python | Graph state schema |
| src/audiosummarizer/ui | Python | Streamlit UI components and config |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit pages/widgets |
| src/audiosummarizer/utils | Python | Token usage tracking |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph, LangChain |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media Processing | moviepy, mutagen, ffmpeg |
| Env Config | python-dotenv |

## System Architecture
| Step | Component | Interaction |
|---|---|---|
| 1 | app.py | Calls load_langgraph_agenticai_app() |
| 2 | LoadStreamlitUI | Collects file upload + process click |
| 3 | AudioGraphBuilder | Builds START→audio_file→transcribe→summarize→END |
| 4 | transcribe_node | Calls ElevenLabs speech_to_text.convert() |
| 5 | summarize_node | Calls Gemini LLM with transcript prompt |
| 6 | DisplayResultStreamlit | Renders transcript, summary, chat |
| 7 | ChatInterface | Answers Q&A using Gemini and cached transcript/summary |

## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| Streamlit entrypoint | app.py | load_langgraph_agenticai_app() |
| Graph state | state/audio_state.py | audio_path, transcript, summary, audio_duration_seconds |
| Graph builder | graph/audio_graph.py | setup_graph("Audio Summarizer") |
| Env vars | LLMS/geminillm.py, nodes/transcribe_node.py | GEMINI_API_KEY, GEMINI_MODEL?, ELEVENLABS_API_KEY |
| UI config | ui/uiconfigfile.ini | PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |

## Coding Conventions
| Rule | Source |
|---|---|
| UI error handling via st.error/st.warning in try/except | AGENTS.md |
| Keep UI logic in ui/ modules | AGENTS.md |
| Keep graph logic in graph/ and nodes/ | AGENTS.md |
| Use AudioAnalysisState fields consistently | AGENTS.md |
| Avoid persistent transcript/summary storage (session_state only) | AGENTS.md |

## Test Patterns
| Aspect | Details |
|---|---|
| Test framework | None detected |
| Test command | n/a |
| Test locations | n/a |