---
language: python
package_manager: pip
test_runner: none
test_command: n/a
test_file_pattern: ""
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| . | Python | Streamlit entry point and repo docs |
| src | Python | Application package root |
| src/audiosummarizer | Python | Audio summarizer app logic |
| src/audiosummarizer/LLMS | Python | LLM client wrappers |
| src/audiosummarizer/graph | Python | LangGraph builder |
| src/audiosummarizer/nodes | Python | Graph node implementations |
| src/audiosummarizer/state | Python | State schema for graph |
| src/audiosummarizer/ui | Python | UI configuration |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI components |
| src/audiosummarizer/utils | Python | Token tracking utilities |
| .devcontainer | JSON | Devcontainer setup |

## Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| UI | Streamlit |
| Orchestration | LangGraph |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media | moviepy, mutagen, ffmpeg |
| Env config | python-dotenv |

## System Architecture
| Step | Interaction |
|---|---|
| UI upload | Streamlit file uploader -> temp file on disk |
| Graph build | AudioGraphBuilder -> StateGraph(AudioAnalysisState) |
| Transcription | transcribe_node -> ElevenLabs API |
| Summarization | summarize_node -> Gemini LLM |
| Display | DisplayResultStreamlit -> transcript + summary + chat |
| Chat Q&A | ChatInterface -> Gemini LLM with transcript/summary context |
| Token tracking | TokenTracker -> ~/.elevenlabs_token_usage.json |

## Key Interfaces & Contracts
| Interface | Definition |
|---|---|
| Env vars | GEMINI_API_KEY, ELEVENLABS_API_KEY, GEMINI_MODEL (optional) |
| State schema | AudioAnalysisState: audio_path, transcript, summary, audio_duration_seconds |
| Graph flow | START -> audio_file -> transcribe -> summarize -> END |
| UI config | src/audiosummarizer/ui/uiconfigfile.ini |
| Entry point | app.py -> load_langgraph_agenticai_app() |

## Coding Conventions
| Area | Convention |
|---|---|
| UI errors | Use st.error/st.warning with try/except in UI flows |
| State fields | Respect AudioAnalysisState keys (audio_path, transcript, summary, audio_duration_seconds) |
| API keys | Require GEMINI_API_KEY and ELEVENLABS_API_KEY before external calls |
| Storage | No persistent transcript/summary storage (session_state only) |
| UI separation | Streamlit UI in ui/; graph logic in graph/ and nodes/ |

## Test Patterns
| Item | Details |
|---|---|
| Tests present | No |
| Test command | n/a |
