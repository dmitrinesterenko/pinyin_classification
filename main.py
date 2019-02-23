import librosa

audio_path = "samples/ceng1.wav"

x, sr = librosa.load(audio_path)

print(type(x), type(sr))

print(x.shape, sr)
