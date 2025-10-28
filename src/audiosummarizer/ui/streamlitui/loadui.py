import streamlit as st
from src.audiosummarizer.ui.uiconfigfile import Config
from mutagen import File as File
import os

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="Customer Audio Record Summarizer", layout="wide")
        st.header("Customer Audio Record Summarizer")
        with st.sidebar:
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
                    duration = self._get_audio_duration(self.user_controls["audio_file"])
                    if duration:
                        st.info(f"⏱️ Duration: {duration}")
                except Exception as e:
                    st.warning(f"Could not determine audio duration: {e}")
            else:
                self.user_controls["process_clicked"] = False
    

        return self.user_controls
    
    def _get_audio_duration(self, audio_file):
        """Get the duration of the audio file"""
        # Save uploaded file temporarily
        temp_path = f"/tmp/{audio_file.name}"
        with open(temp_path, "wb") as f:
            f.write(audio_file.getvalue())
        
        try:
            audio = File(temp_path)
            if audio is None:
                return None
            
            if hasattr(audio, 'info') and audio.info:
                duration = audio.info.length
                if duration:
                    # Duration is in seconds
                    mins, secs = divmod(int(duration), 60)
                    if mins > 0:
                        return f"{mins} min {secs} sec"
                    else:
                        return f"{secs} sec"
            return None
        except Exception as e:
            # Return None if we can't get duration
            return None
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)