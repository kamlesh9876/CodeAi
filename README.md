<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>CodeAI — Voice-Controlled Coding Assistant</title>
</head>
<body>

<h1>🎙️ CodeAI — Real-Time Voice-Controlled Coding Assistant</h1>

<p>
  CodeAI is a powerful Python-based voice assistant that lets you <strong>speak your coding tasks</strong>
  and get them translated into actual code in real time. It also lets you run the generated code and get
  instant feedback — <strong>no typing needed</strong>.
</p>

<p>
  <img src="https://img.shields.io/badge/Voice%20to%20Code-Enabled-brightgreen" alt="Voice to Code Enabled">
  <img src="https://img.shields.io/badge/Made%20with-Python-blue" alt="Made with Python">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License">
</p>

<hr>

<h2>🔥 Features</h2>
<ul>
  <li>🎤 <strong>Voice Recognition</strong> — Converts your speech into text using <a href="https://github.com/openai/whisper">Whisper</a></li>
  <li>🧠 <strong>Local Code Generation</strong> — Powered by locally hosted models like CodeGen/StarCoder</li>
  <li>⚙️ <strong>Smart Command Parsing</strong> — Understands commands like:
    <ul>
      <li>“Create a Flask login route”</li>
      <li>“Make a function to sort a list”</li>
      <li>“Run the code”</li>
    </ul>
  </li>
  <li>💬 <strong>Live Feedback</strong> — View output or errors immediately</li>
  <li>📝 <strong>Auto-Saves Code</strong> — Writes code to <code>output.py</code></li>
  <li>🛠️ <strong>Offline & Cross-Platform</strong> — No internet required post-setup</li>
</ul>

<hr>

<h2>🚀 Quick Start</h2>

<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/yourusername/CodeAi.git
cd CodeAi
</code></pre>

<h3>2. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt
</code></pre>

<h3>3. Run the Assistant</h3>
<pre><code>python main.py
</code></pre>

<hr>

<h2>🎯 How to Use</h2>
<p>When prompted, just <strong>speak your coding command</strong>. Example commands:</p>
<ul>
  <li>Create a Python function to reverse a string</li>
  <li>Make a class for a to-do list</li>
  <li>Run the code</li>
  <li>Say "exit" to quit</li>
</ul>
<p>Generated code appears in <code>output.py</code>.</p>

<hr>

<h2>📂 Project Structure</h2>
<pre><code>CodeAi/
│
├── audio_input/         # Microphone voice capture logic
├── code_generator/      # AI-based code generation using transformers
├── executor/            # Code execution logic
├── main.py              # Main controller file
├── output.py            # Auto-saved generated code
├── requirements.txt     # Python dependencies
└── README.md            # This file
</code></pre>

<hr>

<h2>🧠 Models Used</h2>
<ul>
  <li><strong>Whisper</strong> — for speech-to-text conversion</li>
  <li><strong>CodeGen</strong> or <strong>StarCoderBase-1B</strong> — for generating Python code</li>
  <li><strong>Transformers</strong> — via HuggingFace</li>
</ul>

<hr>

<h2>🛡️ License</h2>
<p>This project is licensed under the <strong>MIT License</strong> — feel free to use, share, and modify.</p>

<hr>

<h2>🤝 Contributing</h2>
<p>Contributions are welcome! Fork the repository, make your changes, and submit a pull request.</p>

<hr>

<h2>🌐 Author</h2>
<p>Developed with 💻 and 🎧 by <a href="https://github.com/kamlesh9876">Kamlesh9876</a></p>

</body>
</html>
