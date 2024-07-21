# Voice Fingerprinting Tool 

***
### List of Contents

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Voice Fingerprinting](#voice-fingerprinting-system)
    - [List of Contents](#list-of-contents)
    - [Basic information](#basic-information)
    - [Potential Use Cases](#potential-use-cases)
      - [Hatebase](#hatebase)
      - [Perspective API](#perspective-api)
      - [Example Workflow for Discord Bot](#example-workflow-for-discord-bot)
    - [Requirements](#requirements)
    - [Install the prerequisites](#install-the-prerequisites)
    - [Usage](#usage)
      - [Actions](#actions)
    - [Examples](#examples)
        - [1. Learn fingerprints from samples.json and save to fingerprints.json](#1-learn-fingerprints-from-samplesjson-and-save-to-fingerprintsjson)
        - [2. Recognize a new audio file](#2-recognize-a-new-audio-file)
        - [3. Bulk match audio files in the 'audio' directory](#3-bulk-match-audio-files-in-the-audio-directory)
        - [4. Show saved fingerprints](#4-show-saved-fingerprints)
    - [Input JSON Format](#input-json-format)
    - [ToDo's](#todos)
    - [DISCLIMER](#disclimer)
    - [Notes](#notes)
    - [License](#license)

<!-- /code_chunk_output -->

---

### Basic information
*This Python script implements a simple voice recognition using MFCC fingerprints. It allows you to:*

- **Learn:** Extract MFCC fingerprints from audio samples and save them to a JSON file.
- **Match:** Match a new audio sample against saved fingerprints to identify the speaker.
- **Bulk Match:** Process a directory of audio files and identify speakers for each file.
- **Show Fingerprints:** Display the saved fingerprints for debugging or analysis.

---

### Potential Use Cases

This system can be part of a larger ecosystem, such as:
Discord Bot for Voice Recognition and Hate Speech Detection

1. **Voice Recognition**: The bot can recognize users by their voice, even across multiple accounts, using the MFCC fingerprints.
2. **Hate Speech Detection**: Integrate with databases like Hatebase or APIs like the Perspective API to analyze voice content for hate speech.
3. **Account Management**: Automatically mute or block users identified as engaging in hate speech, and prevent multi-account abuse.

Integrating with Hatebase and Perspective API

---

#### Hatebase

Hatebase is a database that tracks hate speech across different languages and regions. By integrating with Hatebase, the bot can access a comprehensive list of hate speech terms and patterns.

- **API Access**: Use Hatebase's API to fetch the latest hate speech data.
- **Analysis**: Analyze audio transcripts for matches with Hatebase data.

---

#### Perspective API

The Perspective API, developed by Jigsaw, uses machine learning to detect toxic language in text. It can be adapted to work with transcriptions of audio samples.

- **Transcription**: Convert audio samples to text using speech-to-text tools.
- **Toxicity** Analysis: Use the Perspective API to score the transcribed text for hate speech and toxicity.
- **Action**: Take action based on the toxicity score (e.g., warning, muting, or blocking the user).

---

#### Example Workflow for Discord Bot

-> User Joins Voice Channel:
        The bot starts recording the user's speech.

-> Voice Recognition:
        Extract MFCC fingerprints from the user's speech.
        Match against known fingerprints to identify the user.

-> Speech Transcription:
        Convert the recorded speech to text using a speech-to-text service.

-> Hate Speech Analysis:
        Analyze the transcribed text using Hatebase and the Perspective API.
        Determine the toxicity score and identify any hate speech.

-> Action:
        If hate speech is detected, the bot can warn, mute, or block the user.
        The bot can also track and prevent multi-account abuse.

---

### Requirements

- Python 3.x
- librosa
- numpy
- json
- pydub

---

### Install the prerequisites

install manually:
```bash
pip install librosa numpy json pydub
```
or use bulk configuration files:
```bash
pip install -r requirements.txt
```

---

### Usage

The script can be run from the command line using the following arguments:
```bash
python voice_recognition.py --action <action> [--input_samples <json_file>] [--fingerprint_output <json_file>] [--match <audio_file>] [--bulk_match <directory>] [--fingerprints <json_file>]
```

---

#### Actions

1. **learn**: Extract fingerprints from audio samples.
: **--input_samples**: Path to a JSON file containing audio sample information.
: **--fingerprint_output**: Path to the output JSON file for saving fingerprints.

2. **recognize**: Match a new audio sample against saved fingerprints.
: **--match**: Path to the audio file to be recognized.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

3. **bulk_match**: Process a directory of audio files and identify speakers.
: **--bulk_match**: Path to the directory containing audio files.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

4. **show_fingerprints**: Display the saved fingerprints.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

---

### Examples

##### 1. Learn fingerprints from samples.json and save to fingerprints.json

```bash
python voice_recognition.py --action learn --input_samples samples.json --fingerprint_output fingerprints.json
```

##### 2. Recognize a new audio file

```bash
python voice_recognition.py --action recognize --match test.wav --fingerprints fingerprints.json
```

##### 3. Bulk match audio files in the 'audio' directory

```bash
python voice_recognition.py --action bulk_match --bulk_match audio --fingerprints fingerprints.json
```

##### 4. Show saved fingerprints

```bash
python voice_recognition.py --action show_fingerprints --fingerprints fingerprints.json
```

---

### Input JSON Format
The --input_samples argument expects a JSON file with the following structure:

```json
{
  "person_id1": {
    "name": "Person 1",
    "samples": [
      "path/to/audio1.wav",
      "path/to/audio2.wav"
    ]
  },
  "person_id2": {
    "name": "Person 2",
    "samples": [
      "path/to/audio3.wav",
      "path/to/audio4.wav"
    ]
  }
}
```

---

### ToDo's
- [X] Basic functionality - to learn and to recognize
- [ ] Database to keep data
- [ ] More ways to retrive audio samples
- [ ] Django web frontend
- [ ] Transcripting
- [ ] Integration with Hatedatabase
- [ ] Integration with Perspective AI
- [ ] Many, many, many more...
---

### DISCLIMER

*Make sure, that You using voice samples within law of Your country. I am NOT responsible for misusage*

---

### Notes

The script uses MFCC features for fingerprint extraction.
The confidence score is a simple measure based on the distance between MFCC vectors.
The script supports both WAV and M4A audio files.
The pydub library is used to convert M4A files to WAV for compatibility with librosa.

---

### License

GNU General Public License v3.0
