"""
Token usage tracker for ElevenLabs API.
Tracks remaining tokens (in seconds) persistently across sessions.
"""
import json
import os
from pathlib import Path
from typing import Optional

# Default total tokens: 10,000 seconds (10k tokens)
DEFAULT_TOTAL_TOKENS = 10000

# Path to store token usage data
TOKEN_DATA_FILE = Path.home() / ".elevenlabs_token_usage.json"


class TokenTracker:
    """Manages ElevenLabs token usage tracking with persistent storage."""
    
    def __init__(self, total_tokens: int = DEFAULT_TOTAL_TOKENS):
        """
        Initialize token tracker.
        
        Args:
            total_tokens: Total available tokens in seconds (default: 10000)
        """
        self.total_tokens = total_tokens
        self.data_file = TOKEN_DATA_FILE
        self._ensure_data_file()
    
    def _ensure_data_file(self):
        """Ensure the data file exists with initial values."""
        if not self.data_file.exists():
            self._save_data({
                "total_tokens": self.total_tokens,
                "used_tokens": 0,
                "remaining_tokens": self.total_tokens
            })
    
    def _load_data(self) -> dict:
        """Load token usage data from file."""
        try:
            if self.data_file.exists():
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    # Ensure total_tokens matches current setting
                    if data.get("total_tokens") != self.total_tokens:
                        # Reset if total changed
                        data["total_tokens"] = self.total_tokens
                        data["used_tokens"] = 0
                        data["remaining_tokens"] = self.total_tokens
                    return data
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading token data: {e}")
        
        # Return default data if file doesn't exist or is corrupted
        return {
            "total_tokens": self.total_tokens,
            "used_tokens": 0,
            "remaining_tokens": self.total_tokens
        }
    
    def _save_data(self, data: dict):
        """Save token usage data to file."""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except IOError as e:
            print(f"Error saving token data: {e}")
    
    def get_remaining_tokens(self) -> int:
        """Get remaining tokens in seconds."""
        data = self._load_data()
        return max(0, data.get("remaining_tokens", self.total_tokens))
    
    def get_used_tokens(self) -> int:
        """Get used tokens in seconds."""
        data = self._load_data()
        return data.get("used_tokens", 0)
    
    def use_tokens(self, seconds: float) -> bool:
        """
        Deduct tokens for audio duration.
        
        Args:
            seconds: Duration of audio in seconds
            
        Returns:
            True if tokens were successfully deducted, False if insufficient tokens
        """
        data = self._load_data()
        remaining = data.get("remaining_tokens", self.total_tokens)
        used = data.get("used_tokens", 0)
        
        seconds_int = int(round(seconds))
        
        if seconds_int > remaining:
            return False  # Insufficient tokens
        
        # Update usage
        new_remaining = remaining - seconds_int
        new_used = used + seconds_int
        
        data["remaining_tokens"] = new_remaining
        data["used_tokens"] = new_used
        
        self._save_data(data)
        return True
    
    def reset_tokens(self):
        """Reset token usage (useful for new monthly cycle)."""
        self._save_data({
            "total_tokens": self.total_tokens,
            "used_tokens": 0,
            "remaining_tokens": self.total_tokens
        })
    
    def format_remaining_time(self) -> str:
        """
        Format remaining tokens as human-readable time string.
        
        Returns:
            Formatted string like "166 min 40 sec" or "40 sec"
        """
        remaining = self.get_remaining_tokens()
        hours, remainder = divmod(remaining, 3600)
        mins, secs = divmod(remainder, 60)
        
        parts = []
        if hours > 0:
            parts.append(f"{hours} hour{'s' if hours != 1 else ''}")
        if mins > 0:
            parts.append(f"{mins} min{'s' if mins != 1 else ''}")
        if secs > 0 or not parts:
            parts.append(f"{secs} sec{'s' if secs != 1 else ''}")
        
        return " ".join(parts)
    
    def get_usage_percentage(self) -> float:
        """Get percentage of tokens used."""
        data = self._load_data()
        used = data.get("used_tokens", 0)
        total = data.get("total_tokens", self.total_tokens)
        if total == 0:
            return 0.0
        return (used / total) * 100

