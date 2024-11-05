# generate_audio_files.py
# This script generates audio files for each line in a script using the Eleven Labs API.

# Install required packages for Eleven Labs
!pip install elevenlabs python-dotenv

# Import libraries for Eleven Labs API and file handling
import os
from elevenlabs.client import ElevenLabs, ApiError

# Initialize Eleven Labs API client
API_KEY = "X"  # Replace with your actual Eleven Labs API key
client = ElevenLabs(api_key=API_KEY)

# Define voice IDs for the skit characters
odd_voice = 'HEKjaqG2dPED8VVzR92a'
even_voice = 'jdCUBLZrDQYIoVbymEBl'

# Create a directory for storing audio files
os.makedirs('audio_files', exist_ok=True)

# Generate audio for each line in the script
audio_script = []
for i, (line_key, line_text) in enumerate(lines_dict.items(), start=1):
    voice_id = odd_voice if i % 2 == 1 else even_voice
    audio_file_path = generate_audio(line_text, voice_id, i)

    # Add generated audio file path to the list if successful
    if audio_file_path:
        audio_script.append(audio_file_path)
        print(f"Generated audio for {line_key}: {audio_file_path}")
    else:
        print(f"Failed to generate audio for {line_key}")

# Print the list of generated audio file paths
print("Audio script:", audio_script)
