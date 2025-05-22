# 🎙️ CodeAI — Real-Time Voice-Controlled Coding Assistant

CodeAI is a powerful Python-based voice assistant that lets you **speak your coding tasks** and get them translated into actual code in real time. It also lets you run the generated code and get instant feedback — **no typing needed**.

![CodeAI Demo](https://img.shields.io/badge/Voice%20to%20Code-Enabled-brightgreen)
![Python](https://img.shields.io/badge/Made%20with-Python-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🔥 Features

- 🎤 **Voice Recognition**: Converts your spoken instructions to text using [Whisper](https://github.com/openai/whisper)
- 🧠 **Local Code Generation**: Uses a locally hosted AI model (e.g. CodeGen/StarCoder) — **no API key needed**
- ⚙️ **Smart Command Parsing**: Understands instructions like:
  - "Create a Flask login route"
  - "Build a function to sort a list"
  - "Run the code"
- 💬 **Live Feedback**: Get immediate printouts of results or errors
- 📝 **Auto-saves Code**: Generated code is saved in `output.py`
- 🛠️ **Cross-platform** and runs offline

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/CodeAi.git
cd CodeAi
2. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the assistant
bash
Copy
Edit
python main.py
🎯 How to Use
Just speak your command when prompted. Try:

Create a Python function to reverse a string

Make a class for a to-do list

Run the code

Exit to quit

The generated code will appear in output.py.

📂 Project Structure
bash
Copy
Edit
CodeAi/
│
├── audio_input/         # Microphone voice capture logic
├── code_generator/      # AI-based code generation using transformers
├── executor/            # Code execution logic
├── main.py              # Main controller file
├── output.py            # Auto-saved generated code
├── requirements.txt     # Python dependencies
└── README.md            # This file
🧠 Models Used
Whisper for voice-to-text

CodeGen or StarCoderBase-1B for code generation

Transformers backend from HuggingFace

🛡️ License
MIT License — Feel free to use and modify.

🤝 Contributing
Contributions are welcome! Feel free to fork and raise a pull request with enhancements or fixes.

🌐 Author
Developed with 💻 and 🎧 by Kamlesh9876