# generate_audio_script.py
# This script prepares a conversational script by splitting it into individual lines for audio generation.

# Assume response contains the generated skit content from generate_conversational_script.py
response = """Person 1: Welcome to calculus! Person 2: Great to be here!"""

# Clean up the skit text and remove speaker labels
cleaned_script = response.replace("Person 1:", "").replace("Person 2:", "").strip()

# Split cleaned script into lines and store in dictionary format
lines = [line.strip() for line in cleaned_script.splitlines() if line.strip()]
lines_dict = {f'line{i + 1}': lines[i] for i in range(len(lines))}

# Print the dictionary of lines for verification
print(lines_dict)
