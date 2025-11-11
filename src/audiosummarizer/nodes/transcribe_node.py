import requests
from src.audiosummarizer.state.audio_state import AudioAnalysisState
import os
from io import BytesIO
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import subprocess
import tempfile
from mutagen import File as MutagenFile
from src.audiosummarizer.utils.token_tracker import TokenTracker
from moviepy import VideoFileClip

load_dotenv()

def transcribe_node(state: AudioAnalysisState):
    """Transcribe the audio or video file using ElevenLabs with diarization (speaker labels)"""
    
    audio_path = state["audio_path"]
    
    # Get audio duration for token tracking
    duration_seconds = state.get("audio_duration_seconds")
    if duration_seconds is None:
        # Calculate duration if not provided
        duration_seconds = _get_audio_duration_seconds(audio_path)
    
    # Track token usage before transcription
    tracker = TokenTracker()
    if duration_seconds:
        if not tracker.use_tokens(duration_seconds):
            raise Exception(f"Insufficient tokens. Need {duration_seconds} seconds, but only {tracker.get_remaining_tokens()} seconds remaining.")
    
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

    # Transcribe the audio file with diarization
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
    
    # Extract and format transcript with speaker labels if diarization is enabled
    transcript_text = None
    
    # Debug: Print transcription object attributes to understand structure
    print(f"Transcription object type: {type(transcription)}")
    print(f"Transcription object attributes: {dir(transcription)}")
    
    # Check if transcription has segments (diarized response)
    # ElevenLabs may return segments in different formats
    if hasattr(transcription, 'segments') and transcription.segments:
        # Format transcript with speaker labels
        formatted_segments = []
        for segment in transcription.segments:
            speaker = getattr(segment, 'speaker', getattr(segment, 'speaker_label', 'Unknown'))
            text = getattr(segment, 'text', getattr(segment, 'transcript', str(segment)))
            start_time = getattr(segment, 'start', getattr(segment, 'start_time', None))
            
            # Format: [Time] Speaker X: text
            if start_time is not None:
                mins, secs = divmod(int(start_time), 60)
                time_str = f"[{mins:02d}:{secs:02d}]"
                formatted_segments.append(f"{time_str} Speaker {speaker}: {text}")
            else:
                formatted_segments.append(f"Speaker {speaker}: {text}")
        
        transcript_text = "\n".join(formatted_segments)
    # Check if transcription has words with speaker info (alternative format)
    elif hasattr(transcription, 'words') and transcription.words:
        # Group words by speaker
        current_speaker = None
        current_text = []
        formatted_segments = []
        
        for word in transcription.words:
            speaker = getattr(word, 'speaker', getattr(word, 'speaker_label', 'Unknown'))
            word_text = getattr(word, 'word', getattr(word, 'text', ''))
            
            if speaker != current_speaker:
                if current_speaker is not None and current_text:
                    formatted_segments.append(f"Speaker {current_speaker}: {' '.join(current_text)}")
                current_speaker = speaker
                current_text = [word_text]
            else:
                current_text.append(word_text)
        
        # Add the last segment
        if current_speaker is not None and current_text:
            formatted_segments.append(f"Speaker {current_speaker}: {' '.join(current_text)}")
        
        transcript_text = "\n".join(formatted_segments) if formatted_segments else None
    # Check if text already contains speaker labels (some APIs return formatted text)
    elif hasattr(transcription, 'text'):
        text = transcription.text
        # Check if text already has speaker labels (e.g., "Speaker 1:", "[SPEAKER_1]", etc.)
        if 'Speaker' in text or 'SPEAKER' in text or '[Speaker' in text:
            transcript_text = text  # Already formatted
        else:
            # Plain text - try to get segments if available
            if hasattr(transcription, '__dict__'):
                # Try accessing segments via dict
                trans_dict = transcription.__dict__
                if 'segments' in trans_dict and trans_dict['segments']:
                    segments = trans_dict['segments']
                    formatted = []
                    for seg in segments:
                        if isinstance(seg, dict):
                            speaker = seg.get('speaker', seg.get('speaker_label', 'Unknown'))
                            text = seg.get('text', seg.get('transcript', ''))
                            formatted.append(f"Speaker {speaker}: {text}")
                        else:
                            speaker = getattr(seg, 'speaker', 'Unknown')
                            text = getattr(seg, 'text', str(seg))
                            formatted.append(f"Speaker {speaker}: {text}")
                    transcript_text = "\n".join(formatted) if formatted else text
                else:
                    transcript_text = text
            else:
                transcript_text = text
    elif isinstance(transcription, str):
        transcript_text = transcription
    else:
        # Try to convert to string or inspect further
        transcript_text = str(transcription)
    
    state["transcript"] = transcript_text
    print(f"Transcript: {state['transcript'][:200]}...")  # Print first 200 chars
    return state

def _get_audio_duration_seconds(audio_path: str) -> float:
    """Get audio/video duration in seconds using mutagen, moviepy, or ffprobe."""
    # Check if it's a video file
    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
    is_video = any(audio_path.lower().endswith(ext) for ext in video_extensions)
    
    # For video files, try moviepy first
    if is_video:
        try:
            video = VideoFileClip(audio_path)
            duration = video.duration
            video.close()
            if duration:
                return float(duration)
        except Exception:
            pass
    
    # Try using mutagen for audio files
    try:
        audio_file = MutagenFile(audio_path)
        if audio_file is not None and hasattr(audio_file, 'info') and audio_file.info:
            duration = audio_file.info.length
            if duration:
                return float(duration)
    except Exception:
        pass
    
    # Fallback: try ffprobe if available
    try:
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_path],
            capture_output=True,
            text=True,
            check=True
        )
        duration = float(result.stdout.strip())
        return duration
    except (subprocess.CalledProcessError, ValueError, FileNotFoundError):
        # If all else fails, return None (will be handled by caller)
        return None

def _extract_audio_from_video(video_path):
    """Extract audio from video file using moviepy"""
    output_path = tempfile.mktemp(suffix='.wav')
    
    try:
        # Use moviepy to extract audio from video
        video = VideoFileClip(video_path)
        audio = video.audio
        
        # Write audio to temporary file
        # Note: moviepy will use ffmpeg under the hood
        # Use wav format with PCM codec (compatible with ElevenLabs)
        # MoviePy 2.x has different parameters - removed verbose and logger
        audio.write_audiofile(
            output_path,
            codec='pcm_s16le',  # 16-bit PCM
            fps=16000  # Sample rate (16kHz)
        )
        
        # Close the clips to free up resources
        audio.close()
        video.close()
        
        return output_path
    except Exception as e:
        error_msg = str(e)
        # Check if it's an ffmpeg-related error
        if "ffmpeg" in error_msg.lower() or "imageio_ffmpeg" in error_msg.lower():
            raise Exception(
                "❌ **ffmpeg not found**\n\n"
                "MoviePy requires ffmpeg to process video files. Please install ffmpeg:\n\n"
                "**On macOS:**\n"
                "```bash\nbrew install ffmpeg\n```\n\n"
                "**On Linux (Ubuntu/Debian):**\n"
                "```bash\nsudo apt-get update\nsudo apt-get install ffmpeg\n```\n\n"
                "**On Windows:**\n"
                "Download from https://ffmpeg.org/download.html or use:\n"
                "```bash\nchoco install ffmpeg\n```\n\n"
                "After installing, restart the application."
            )
        else:
            raise Exception(f"Failed to extract audio from video: {error_msg}")