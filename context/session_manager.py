# context/session_manager.py

class SessionContext:
    def __init__(self):
        # Stores tuples of (voice_command, generated_code)
        self.history = []

    def update_history(self, voice_cmd, code):
        """
        Save the latest command and generated code.
        """
        self.history.append((voice_cmd, code))

    def undo(self):
        """
        Undo the last code generation command.
        Removes the last block of code and rewrites the output file.
        """
        if not self.history:
            print("[Undo] No history to undo.")
            return

        # Remove the last command from history
        removed_cmd, removed_code = self.history.pop()
        print(f"[Undo] Removed command: '{removed_cmd}'")

        # Rewrite main_output.py with remaining code
        with open("main_output.py", "w") as f:
            for _, code in self.history:
                f.write(code + "\n")

        print("[Undo] main_output.py has been updated.")
