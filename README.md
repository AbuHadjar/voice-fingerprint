# Voice Fingerprinting System {#custom-id}
***
*This Python script implements a simple voice recognition system using MFCC fingerprints. It allows you to:*

- **Learn:** Extract MFCC fingerprints from audio samples and save them to a JSON file.
- **Match:** Match a new audio sample against saved fingerprints to identify the speaker.
- **Bulk Match:** Process a directory of audio files and identify speakers for each file.
- **Show Fingerprints:** Display the saved fingerprints for debugging or analysis.

##### DISCLIMER: 
*Make sure, that You using voice samples within law of Your country.*

### List of Contents
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [Voice Fingerprinting System](#custom-id)
        - [DISCLIMER:](#disclimer)
    - [List of Contents](#list-of-contents)
    - [Requirements](#requirements)
    - [Install the prerequisites:](#install-the-prerequisites)
    - [Usage](#usage)
      - [Actions](#actions)
    - [Examples:](#examples)
      - [Learn fingerprints from samples.json and save to fingerprints.json](#learn-fingerprints-from-samplesjson-and-save-to-fingerprintsjson)
      - [Recognize a new audio file](#recognize-a-new-audio-file)
      - [Bulk match audio files in the 'audio' directory](#bulk-match-audio-files-in-the-audio-directory)
      - [Show saved fingerprints](#show-saved-fingerprints)
      - [Input JSON Format](#input-json-format)
    - [Notes](#notes)
    - [License](#license)

<!-- /code_chunk_output -->

### Requirements

- Python 3.x
- librosa
- numpy
- json
- pydub

### Install the prerequisites:

```bash
pip install librosa numpy json pydub
```
### Usage
The script can be run from the command line using the following arguments:
```bash
python voice_recognition.py --action <action> [--input_samples <json_file>] [--fingerprint_output <json_file>] [--match <audio_file>] [--bulk_match <directory>] [--fingerprints <json_file>]
```
#### Actions

**learn**: Extract fingerprints from audio samples.
: **--input_samples**: Path to a JSON file containing audio sample information.
: **--fingerprint_output**: Path to the output JSON file for saving fingerprints.

**recognize**: Match a new audio sample against saved fingerprints.
: **--match**: Path to the audio file to be recognized.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

**bulk_match**: Process a directory of audio files and identify speakers.
: **--bulk_match**: Path to the directory containing audio files.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

**show_fingerprints**: Display the saved fingerprints.
: **--fingerprints**: Path to the JSON file containing saved fingerprints.

### Examples:

#### Learn fingerprints from samples.json and save to fingerprints.json
```bash
python voice_recognition.py --action learn --input_samples samples.json --fingerprint_output fingerprints.json
```

#### Recognize a new audio file
```bash
python voice_recognition.py --action recognize --match test.wav --fingerprints fingerprints.json
```
#### Bulk match audio files in the 'audio' directory
```bash
python voice_recognition.py --action bulk_match --bulk_match audio --fingerprints fingerprints.json
```
#### Show saved fingerprints
```bash
python voice_recognition.py --action show_fingerprints --fingerprints fingerprints.json
```
#### Input JSON Format
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

### Notes
The script uses MFCC features for fingerprint extraction.
The confidence score is a simple measure based on the distance between MFCC vectors.
The script supports both WAV and M4A audio files.
The pydub library is used to convert M4A files to WAV for compatibility with librosa.
### License
This project is licensed under the MIT License.