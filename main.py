# main.py

import os
import sys
import sounddevice as sd
import soundfile as sf
import tempfile

# Ensure local module imports work
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from transcriber.whisper_engine import transcribe_audio
from nlp_parser.intent_parser import parse_intent
from code_generator.gpt_handler import generate_code
from executor.runner import run_code
from context.session_manager import SessionContext

# Config
SAMPLE_RATE = 44100
DURATION = 5  # Recording time in seconds
OUTPUT_FILE = "main_output.py"

def record_audio():
    """
    Records microphone audio and returns the path to a temporary WAV file.
    """
    print("🎙️ Listening... Speak your command:")
    recording = sd.rec(int(SAMPLE_RATE * DURATION), samplerate=SAMPLE_RATE, channels=1, dtype='float32')
    sd.wait()

    temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    sf.write(temp_file.name, recording, SAMPLE_RATE)
    return temp_file.name

def setup_output_file():
    """
    Ensures the output code file exists.
    """
    if not os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "w") as f:
            f.write("# 🧠 Generated code will appear here\n")

def main():
    print("\n🚀 Real-Time Voice-Controlled Coding Assistant Started!")
    print("🎯 Say something like: 'Create a Flask login route' or 'run code'")
    print("❌ Say 'exit' anytime to quit\n")

    setup_output_file()
    context = SessionContext()

    while True:
        try:
            audio_path = record_audio()
            transcript = transcribe_audio(audio_path)
            os.remove(audio_path)

            print(f"\n📝 You said: {transcript}")
            intent = parse_intent(transcript)

            if intent["action"] == "exit":
                print("👋 Goodbye!")
                break
            elif intent["action"] == "undo":
                context.undo()
            elif intent["action"] == "run_code":
                output = run_code()
                print("📤 Output:\n", output)
            elif intent["action"] == "generate_code":
                code = generate_code(intent, context)
                print("🧠 Generated Code:\n", code)

                with open(OUTPUT_FILE, "a") as f:
                    f.write("\n" + code + "\n")

                context.update_history(transcript, code)
            else:
                print("🤖 Sorry, I didn't understand that.")

        except KeyboardInterrupt:
            print("\n❌ Interrupted by user. Exiting.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
