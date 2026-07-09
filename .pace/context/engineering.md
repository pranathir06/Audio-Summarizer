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
| / | Python | Streamlit entry point and repo config files |
| src/audiosummarizer | Python | Core audio summarizer package |
| src/audiosummarizer/LLMS | Python | Gemini LLM wrapper |
| src/audiosummarizer/graph | Python | LangGraph builder for audio workflow |
| src/audiosummarizer/nodes | Python | Graph nodes for audio file, transcription, summarization |
| src/audiosummarizer/state | Python | AudioAnalysisState schema |
| src/audiosummarizer/ui | Python | Streamlit UI components and config |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI screens and chat |
| src/audiosummarizer/utils | Python | Token tracking utilities |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| Orchestration | LangGraph (langgraph) |
| LLM | Google Gemini via langchain-google-genai |
| Transcription | ElevenLabs speech_to_text |
| Media processing | moviepy, mutagen, ffmpeg (external) |
| Env config | python-dotenv |
| LangChain | langchain, langchain_core, langchain_community |

## System Architecture
| Flow Step | Component | Details |
|---|---|---|
| UI upload | LoadStreamlitUI | Upload audio/video; collects duration and button click |
| Graph build | AudioGraphBuilder | Builds StateGraph: audio_file → transcribe → summarize |
| Transcription | transcribe_node | Uses ElevenLabs API; diarization; token check |
| Summarization | summarize_node | Gemini prompt returns structured summary |
| Results UI | DisplayResultStreamlit | Shows transcript, summary, and chat |
| Q&A | ChatInterface | Gemini answers using cached transcript/summary |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| Env vars | GEMINI_API_KEY, ELEVENLABS_API_KEY required; GEMINI_MODEL optional |
| State schema | AudioAnalysisState: audio_path, transcript, summary, audio_duration_seconds |
| Token storage | ~/.elevenlabs_token_usage.json (TokenTracker) |
| Config file | src/audiosummarizer/ui/uiconfigfile.ini (PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS) |

## Coding Conventions
| Area | Convention |
|---|---|
| UI error handling | Use st.error / st.warning with try/except in UI flows |
| State usage | Respect AudioAnalysisState fields; session_state for cached results |
| API keys | Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls |
| Storage | No persistent transcript/summary storage beyond session_state |

## Test Patterns
| Item | Details |
|---|---|
| Test runner | None detected (AGENTS.md: tests n/a) |
| Test location | n/a |
| Execution | n/a |
