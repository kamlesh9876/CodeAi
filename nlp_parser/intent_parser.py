# nlp_parser/intent_parser.py

def parse_intent(transcribed_text):
    """
    Parses transcribed voice input and identifies intent.

    Parameters:
        transcribed_text (str): The text converted from voice.

    Returns:
        dict: A dictionary representing the intent.
    """
    text = transcribed_text.lower()

    if "create" in text and "route" in text:
        return {"action": "generate_code", "type": "flask_route", "details": text}
    elif "define" in text and "function" in text:
        return {"action": "generate_code", "type": "function", "details": text}
    elif "add" in text and "html" in text:
        return {"action": "generate_code", "type": "html", "details": text}
    elif "run" in text or "execute" in text:
        return {"action": "run_code"}
    elif "undo" in text:
        return {"action": "undo"}
    elif "exit" in text or "quit" in text:
        return {"action": "exit"}

    return {"action": "unknown"}
