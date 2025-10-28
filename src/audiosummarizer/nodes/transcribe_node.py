import requests
from src.audiosummarizer.state.audio_state import AudioAnalysisState
import os
from io import BytesIO
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import subprocess
import tempfile

load_dotenv()

def transcribe_node(state: AudioAnalysisState):
    """Transcribe the audio or video file using ElevenLabs with diarization (speaker labels)"""
    
    audio_path = state["audio_path"]
    
    # Check if file is a video format that needs audio extraction
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    is_video = any(audio_path.lower().endswith(ext) for ext in video_extensions)
    
    # If it's a video file, extract audio first
    if is_video:
        temp_audio_path = _extract_audio_from_video(audio_path)
        audio_path_to_process = temp_audio_path
    else:
        audio_path_to_process = audio_path
    
    elevenlabs = ElevenLabs(
       api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    # Transcribe the audio file
    with open(audio_path_to_process, "rb") as f:
        transcription = elevenlabs.speech_to_text.convert(
        file=f,
        model_id="scribe_v1",
        tag_audio_events=False,
        language_code="eng",
        diarize=True,
    )
    
    # If we created a temporary audio file, clean it up
    if is_video:
        os.unlink(temp_audio_path)
    
    state["transcript"] = transcription
    print(state["transcript"])
    return state

def _extract_audio_from_video(video_path):
    """Extract audio from video file using ffmpeg"""
    output_path = tempfile.mktemp(suffix='.wav')
    
    try:
        subprocess.run(
            ['ffmpeg', '-i', video_path, '-vn', '-acodec', 'pcm_s16le', '-ar', '16000', '-ac', '1', output_path],
            check=True,
            capture_output=True
        )
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to extract audio from video: {e}")
    except FileNotFoundError:
        raise Exception("ffmpeg not found. Please install ffmpeg to process video files.")