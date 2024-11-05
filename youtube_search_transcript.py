# youtube_search_transcript.py
# This script searches YouTube for videos related to a user-inputted math concept and retrieves video transcripts.

# Install required packages for using YouTube API and transcript retrieval
!pip install google-api-python-client youtube-transcript-api

# Import necessary libraries
from googleapiclient.discovery import build
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, VideoUnavailable

# Step 1: Get user input for the math concept they need help with
user_input = input("Enter the math concept you're struggling with: ")

# Step 2: Set up YouTube API client
YOUTUBE_API_KEY = ''  # Replace with your YouTube API key
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Step 3: Search YouTube for videos related to the user's input and retrieve transcripts
search_response = youtube.search().list(
    q=user_input,
    part='snippet',
    maxResults=3
).execute()

# Step 4: Attempt to retrieve transcripts for each video
for item in search_response['items']:
    video_id = item['id']['videoId']
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        explanation = " ".join([entry['text'] for entry in transcript_list])
        print("Explanation extracted from the video:")
        print(explanation)
        break  # Stop after finding the first video with a valid transcript
    except NoTranscriptFound:
        print(f"No transcript found for video ID {video_id}. Trying the next video.")
    except VideoUnavailable:
        print(f"Video ID {video_id} is unavailable. Trying the next video.")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Trying the next video.")
else:
    print("No valid transcripts were found for the top search results.")
