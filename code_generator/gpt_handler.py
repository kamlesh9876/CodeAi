# code_generator/gpt_handler.py

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load a small, local-compatible model
model_name = "bigcode/starcoderbase-1b"  # lightweight version of StarCoder
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_code(intent, context):
    """
    Uses a local Hugging Face model to generate code based on user intent.

    Parameters:
        intent (dict): Parsed intent containing the request.
        context (SessionContext): Current session context.

    Returns:
        str: Generated code string.
    """
    prompt = f"# {intent['details']}\n"

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=100,
        do_sample=True,
        temperature=0.5,
        pad_token_id=tokenizer.eos_token_id
    )

    generated = tokenizer.decode(outputs[0], skip_special_tokens=True)
    code = generated[len(prompt):].strip()  # Remove prompt part
    return code
