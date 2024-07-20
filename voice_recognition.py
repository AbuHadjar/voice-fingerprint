import librosa
import numpy as np
import json
import argparse
from pydub import AudioSegment
import tempfile

# Load and preprocess audio samples
def load_audio_samples(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    samples = []
    for person_id, info in data.items():
        mfcc_means = []
        for file_path in info['samples']:
            if file_path.endswith('.m4a'):
                y, sr = load_m4a(file_path)
            else:
                y, sr = librosa.load(file_path, sr=None)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            mfcc_mean = np.mean(mfcc, axis=1)
            mfcc_means.append(mfcc_mean)
        mfcc_mean_combined = np.mean(mfcc_means, axis=0)
        samples.append((person_id, info['name'], mfcc_mean_combined))
    
    return samples

def load_m4a(file_path):
    audio = AudioSegment.from_file(file_path, format="m4a")
    with tempfile.NamedTemporaryFile(delete=True) as temp_wav:
        audio.export(temp_wav.name, format="wav")
        y, sr = librosa.load(temp_wav.name, sr=None)
    return y, sr

# Save fingerprints for later use
def save_fingerprints(samples, output_file):
    fingerprints = {sample_id: {"name": name, "mfcc": mfcc.tolist()} for sample_id, name, mfcc in samples}
    with open(output_file, 'w') as file:
        json.dump(fingerprints, file)

# Load fingerprints from a file
def load_fingerprints(fingerprints_file):
    with open(fingerprints_file, 'r') as file:
        fingerprints = json.load(file)
    return {k: {"name": v["name"], "mfcc": np.array(v["mfcc"])} for k, v in fingerprints.items()}

# Match a new audio sample against saved fingerprints
def match_sample(file_path, fingerprints):
    if file_path.endswith('.m4a'):
        y, sr = load_m4a(file_path)
    else:
        y, sr = librosa.load(file_path, sr=None)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_mean = np.mean(mfcc, axis=1)
    
    distances = {sample_id: np.linalg.norm(fingerprint["mfcc"] - mfcc_mean) for sample_id, fingerprint in fingerprints.items()}
    best_match_id = min(distances, key=distances.get)
    
    return best_match_id, fingerprints[best_match_id]

# Show fingerprints
def show_fingerprints(fingerprints_file):
    fingerprints = load_fingerprints(fingerprints_file)
    for sample_id, info in fingerprints.items():
        print(f"ID: {sample_id}, Name: {info['name']}, MFCC: {info['mfcc']}")

# Command-line interface
def main():
    parser = argparse.ArgumentParser(description='Voice Recognition System')
    parser.add_argument('--action', required=True, choices=['learn', 'recognize', 'show_fingerprints'], help='Action to perform')
    parser.add_argument('--input_samples', help='JSON file with input audio samples for learning')
    parser.add_argument('--fingerprint_output', help='Output JSON file for saving fingerprints')
    parser.add_argument('--match_sample', help='Audio sample file for recognition')
    parser.add_argument('--matched_fingerprints', help='JSON file with saved fingerprints for recognition')
    
    args = parser.parse_args()
    
    if args.action == 'learn':
        if not args.input_samples or not args.fingerprint_output:
            print("Please provide both --input_samples and --fingerprint_output for learning action.")
            return
        audio_samples = load_audio_samples(args.input_samples)
        save_fingerprints(audio_samples, args.fingerprint_output)
        print(f"Fingerprints saved to {args.fingerprint_output}")
    
    elif args.action == 'recognize':
        if not args.match_sample or not args.matched_fingerprints:
            print("Please provide both --match_sample and --matched_fingerprints for recognition action.")
            return
        fingerprints = load_fingerprints(args.matched_fingerprints)
        best_match_id, best_match_info = match_sample(args.match_sample, fingerprints)
        print(f"Best Match ID: {best_match_id}, Name: {best_match_info['name']}")
    
    elif args.action == 'show_fingerprints':
        if not args.matched_fingerprints:
            print("Please provide --matched_fingerprints to show fingerprints.")
            return
        show_fingerprints(args.matched_fingerprints)

if __name__ == "__main__":
    main()
