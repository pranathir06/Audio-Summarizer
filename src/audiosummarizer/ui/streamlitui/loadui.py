import streamlit as st
from src.audiosummarizer.ui.uiconfigfile import Config
from mutagen import File as File
import os
from src.audiosummarizer.utils.token_tracker import TokenTracker
from moviepy import VideoFileClip

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        self.token_tracker = TokenTracker()

    def load_streamlit_ui(self):
        st.set_page_config(page_title="Customer Audio Record Summarizer", layout="wide")
        st.header("Customer Audio Record Summarizer")
        with st.sidebar:
            # Display token usage
            self._display_token_usage()
            
            st.divider()
            
            st.subheader("📁 Audio/Video File Upload")
            self.user_controls["audio_file"] = st.file_uploader(
                "Choose an audio or video file", 
                type=['mp3', 'wav', 'm4a', 'flac', 'aac', 'ogg', 'mp4', 'mov', 'avi', 'mkv'], 
                help="Upload an audio or video file to summarize")
            self.user_controls["process_clicked"] = st.button(
                    "🚀 Process Audio File",
                    
                    type="primary",
                    help="Click to start processing the uploaded audio file"
                )
            if self.user_controls["audio_file"] is not None:
                st.success(f"✅ File uploaded: {self.user_controls['audio_file'].name}")
                st.info(f"📊 File size: {self.user_controls['audio_file'].size} bytes")
                
                # Get audio duration
                try:
                    duration_str, duration_seconds = self._get_audio_duration(self.user_controls["audio_file"])
                    if duration_str:
                        st.info(f"⏱️ Duration: {duration_str}")
                        # Store duration in seconds for token tracking
                        self.user_controls["audio_duration_seconds"] = duration_seconds
                        
                        # Check if user has enough tokens
                        if duration_seconds:
                            remaining = self.token_tracker.get_remaining_tokens()
                            if duration_seconds > remaining:
                                st.error(f"❌ Insufficient tokens! Need {int(duration_seconds)} sec, but only {remaining} sec remaining.")
                            else:
                                st.success(f"✅ Sufficient tokens available")
                except Exception as e:
                    error_msg = str(e)
                    # Check if it's a video file and ffmpeg is missing
                    video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
                    is_video = any(self.user_controls["audio_file"].name.lower().endswith(ext) for ext in video_extensions)
                    if is_video and ("ffmpeg" in error_msg.lower() or "imageio_ffmpeg" in error_msg.lower()):
                        st.error("❌ **Cannot process video file**")
                        st.warning("""
                        **ffmpeg not found**
                        
                        MoviePy requires ffmpeg to process video files. Install ffmpeg:
                        
                        **macOS:**
                        ```bash
                        brew install ffmpeg
                        ```
                        
                        **Linux:**
                        ```bash
                        sudo apt-get install ffmpeg
                        ```
                        
                        **Windows:**
                        Download from https://ffmpeg.org/download.html
                        
                        Then restart the application.
                        """)
                    else:
                        st.warning(f"Could not determine audio duration: {error_msg}")
            else:
                self.user_controls["process_clicked"] = False
    

        return self.user_controls
    
    def _display_token_usage(self):
        """Display remaining ElevenLabs token usage in the sidebar."""
        remaining = self.token_tracker.get_remaining_tokens()
        used = self.token_tracker.get_used_tokens()
        total = self.token_tracker.total_tokens
        usage_percent = self.token_tracker.get_usage_percentage()
        
        st.subheader("⏱️ ElevenLabs Usage")
        
        # Explanation for new users
        with st.expander("ℹ️ What is this?", expanded=False):
            st.markdown("""
            **ElevenLabs Transcription Credits**
            
            This shows your remaining transcription time for the ElevenLabs API.
            
            - **Monthly Plan**: 10,000 seconds (≈166 minutes) per month
            - **Usage**: Each audio/video file you transcribe uses tokens equal to its duration
            - **Tracking**: Your usage is tracked across sessions and persists between visits
            - **Reset**: Credits reset monthly with your ElevenLabs subscription
            
            The time shown is your remaining balance for this month.
            """)
        
        # Format remaining time
        remaining_time = self.token_tracker.format_remaining_time()
        
        # Display remaining time with color coding
        if remaining < total * 0.1:  # Less than 10% remaining
            st.error(f"⚠️ **{remaining_time}** remaining")
        elif remaining < total * 0.3:  # Less than 30% remaining
            st.warning(f"⚠️ **{remaining_time}** remaining")
        else:
            st.success(f"✅ **{remaining_time}** remaining")
        
        # Progress bar
        st.progress(usage_percent / 100)
        st.caption(f"Used: {used:,} sec / {total:,} sec ({usage_percent:.1f}%)")
    
    def _get_audio_duration(self, audio_file):
        """Get the duration of the audio or video file in formatted string and seconds"""
        # Save uploaded file temporarily
        temp_path = f"/tmp/{audio_file.name}"
        with open(temp_path, "wb") as f:
            f.write(audio_file.getvalue())
        
        # Check if it's a video file
        video_extensions = ['.mp4', '.mov', '.avi', '.mkv']
        is_video = any(audio_file.name.lower().endswith(ext) for ext in video_extensions)
        
        try:
            # For video files, use moviepy
            if is_video:
                try:
                    video = VideoFileClip(temp_path)
                    duration_seconds = float(video.duration)
                    video.close()
                    mins, secs = divmod(int(duration_seconds), 60)
                    formatted = f"{mins} min {secs} sec" if mins > 0 else f"{secs} sec"
                    return formatted, duration_seconds
                except Exception as e:
                    # If moviepy fails, it's likely because ffmpeg is missing
                    error_msg = str(e).lower()
                    if "ffmpeg" in error_msg or "imageio_ffmpeg" in error_msg:
                        # Return None but the error will be caught and displayed
                        return None, None
                    return None, None
            
            # For audio files, use mutagen
            audio = File(temp_path)
            if audio is None:
                return None, None
            
            if hasattr(audio, 'info') and audio.info:
                duration = audio.info.length
                if duration:
                    # Store duration in seconds for token tracking
                    duration_seconds = float(duration)
                    # Format for display
                    mins, secs = divmod(int(duration), 60)
                    formatted = f"{mins} min {secs} sec" if mins > 0 else f"{secs} sec"
                    return formatted, duration_seconds
            return None, None
        except Exception as e:
            # Return None if we can't get duration
            return None, None
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)