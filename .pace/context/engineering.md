---
language: python
package_manager: pip
test_runner: pytest
test_command: "pytest"
test_file_pattern: "tests/**/*.py"
require_tests: false
---
## Module Map
| Directory | Language | Purpose |
|---|---|---|
| app.py | Python | Streamlit entry point invoking load_langgraph_agenticai_app |
| src/audiosummarizer | Python | Core audio summarization package |
| src/audiosummarizer/LLMS | Python | Gemini LLM client setup |
| src/audiosummarizer/graph | Python | LangGraph builder for audio flow |
| src/audiosummarizer/nodes | Python | Graph node implementations (file, transcribe, summarize) |
| src/audiosummarizer/state | Python | Typed state schema for graph |
| src/audiosummarizer/ui | Python | UI config and wrappers |
| src/audiosummarizer/ui/streamlitui | Python | Streamlit UI components |
| src/audiosummarizer/utils | Python | Token usage tracking |

## Tech Stack
| Component | Technology |
|---|---|
| UI | Streamlit |
| LLM Orchestration | LangGraph, LangChain |
| LLM Provider | Google Gemini (langchain-google-genai) |
| Transcription | ElevenLabs speech_to_text |
| Media Processing | moviepy, mutagen, ffmpeg (external) |
| Config/Env | python-dotenv |

## System Architecture
| Flow | Details |
|---|---|
| UI → Processing | LoadStreamlitUI collects file + click; main._process_audio_file runs graph |
| Graph | START → audio_file → transcribe → summarize → END |
| Transcription | transcribe_node calls ElevenLabs; diarization formatted into transcript string |
| Summarization | summarize_node prompts Gemini to generate structured summary |
| Chat | ChatInterface uses stored transcript/summary to answer questions via Gemini |
| State | AudioAnalysisState: audio_path, transcript, summary, audio_duration_seconds |

## Key Interfaces & Contracts
| Interface | Contract |
|---|---|
| Entry point | app.py → load_langgraph_agenticai_app() |
| Env Vars | GEMINI_API_KEY, GEMINI_MODEL (optional), ELEVENLABS_API_KEY |
| Graph State | AudioAnalysisState TypedDict fields must exist |
| Token Tracking | ~/.elevenlabs_token_usage.json stores used/remaining seconds |
| UI Config | ui/uiconfigfile.ini with PAGE_TITLE, LLM_OPTIONS, USECASE_OPTIONS |

## Coding Conventions
| Rule | Source |
|---|---|
| Keep UI logic in ui/; graph logic in graph/ and nodes/ | AGENTS.md |
| Use AudioAnalysisState fields exactly as defined | AGENTS.md |
| Add try/except error handling in UI flows | AGENTS.md |
| Require GEMINI_API_KEY and ELEVENLABS_API_KEY before API calls | AGENTS.md |
| Store transcripts/summaries only in st.session_state | AGENTS.md |

## Test Patterns
| Item | Details |
|---|---|
| Tests Present | No test files found |
| Runner | pytest (not configured) |
| Guidance | Add tests before enabling require_tests true |