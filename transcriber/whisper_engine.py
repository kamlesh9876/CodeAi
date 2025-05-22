# transcriber/whisper_engine.py

import whisper

# Load Whisper model (base model is a good tradeoff for speed and accuracy)
model = whisper.load_model("base")

def transcribe_audio(audio_path):
    """
    Transcribes the given audio file to text using Whisper.
    
    Parameters:
        audio_path (str): Path to the audio .wav file.
        
    Returns:
        str: Transcribed text.
    """
    result = model.transcribe(audio_path)
    return result["text"]
