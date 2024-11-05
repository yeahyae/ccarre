# video_generation.py
# This script generates a video using Wav2Lip for lip-syncing with generated audio.

# Clone and install Wav2Lip (if not installed)
version = 'v8.3'
print("Installing Easy-Wav2Lip...")

if not os.path.exists('installed.txt'):
    !git clone -b {version} https://github.com/anothermartz/Easy-Wav2Lip.git
    %cd 'Easy-Wav2Lip'
    !python install.py
    print("Easy-Wav2Lip installation complete!")

# Define file paths for the video files to be used for lip-syncing
even_video_dir = "/content/drive/MyDrive/Content/Deepfakes/CR7/CristianoRonaldoDF.mp4"
odd_video_dir = "/content/drive/MyDrive/Content/Deepfakes/Rio Ferdinand/RioFerdinandDF.mp4"

# Generate final video with audio and video files
for audio_file in audio_script:
    generate_video(audio_file, even_video_dir if 'audio' in audio_file else odd_video_dir)
print("Video generation complete!")
