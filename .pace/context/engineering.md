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
| . | Python | Streamlit entry point and project docs |
| src | Python | Package root |
| src/audiosummarizer | Python | Audio summarizer app logic |
| src/audiosummarizer/graph | Python | LangGraph workflow builder |
| src/audiosummarizer/nodes | Python | Graph node functions |
| src/audiosummarizer/state | Python | Typed state schema |
| src/audiosummarizer/LLMS | Python | LLM client wrapper |
| src/audiosummarizer/ui | Python | UI config + Streamlit views |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit components |
| src/audiosummarizer/utils | Python | Token usage tracking |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph (langgraph) |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Audio/Video | moviepy, mutagen, ffmpeg |
| Env config | python-dotenv |

## System Architecture
| Flow | Details |
|---|---|
| Entry point | app.py -> load_langgraph_agenticai_app() |
| UI to graph | Streamlit UI collects file + triggers graph.invoke(initial_state) |
| Graph pipeline | START -> audio_file -> transcribe -> summarize -> END |
| Chat | Streamlit chat uses existing transcript/summary without graph re-run |
| Token tracking | TokenTracker stores usage in ~/.elevenlabs_token_usage.json |

## Key Interfaces & Contracts
| Interface | Location | Contract |
|---|---|---|
| Streamlit app | app.py | load_langgraph_agenticai_app() |
| Graph builder | graph/audio_graph.py | AudioGraphBuilder.setup_graph("Audio Summarizer") |
| State schema | state/audio_state.py | AudioAnalysisState: audio_path, transcript, summary, audio_duration_seconds |
| Transcription | nodes/transcribe_node.py | transcribe_node(state) requires ELEVENLABS_API_KEY |
| Summarization | nodes/summarize_node.py | summarize_node(state) requires GEMINI_API_KEY |
| Chat QA | ui/streamlitui/chat_interface.py | _get_answer_via_graph(question) uses transcript + summary |

## Coding Conventions
| Rule | Evidence |
|---|---|
| UI error handling | st.error/st.warning used in main.py and loadui.py |
| State keys | audio_path, transcript, summary, audio_duration_seconds used across nodes |
| Env vars required | GEMINI_API_KEY, ELEVENLABS_API_KEY (GeminiLLM, transcribe_node) |
| Temp files | NamedTemporaryFile for uploads; do not delete until chat complete |
| Config file | uiconfigfile.ini consumed by Config (note: Config path uses ./src/langgraphagenticai/ui/uiconfigfile.ini) |

## Test Patterns
| Item | Details |
|---|---|
| Test framework | none configured |
| Test command | n/a |
| Test files | none found |
