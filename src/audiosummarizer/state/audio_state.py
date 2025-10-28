from typing_extensions import TypedDict,Optional,List
from langgraph.graph.message import add_messages
from typing import Annotated



class AudioAnalysisState(TypedDict):
    audio_path: str
    transcript: Optional[str]
    summary: Optional[str]