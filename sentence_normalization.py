import ollama


def normalize_sentence(words):
    """
    Convert ISL keyword sequence into a proper English sentence
    using a constrained local LLM (Ollama).
    """

    # Join ISL keywords
    keywords = " ".join(words)

    # Strict prompt to avoid AI explanations or hallucination
    prompt = f"""
You are a sentence normalization engine.

Rules (MANDATORY):
- Output ONLY one grammatically correct English sentence
- Do NOT say you are an AI
- Do NOT explain anything
- Do NOT add extra information
- Preserve the original meaning
- Keep the sentence short and direct

ISL keywords:
{keywords}

Output:
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()


# ---------------- MAIN ----------------
if __name__ == "__main__":
    user_input = input("Enter ISL words (space separated): ")
    isl_words = user_input.strip().split()

    if not isl_words:
        print("No ISL words entered.")
        exit()

    sentence = normalize_sentence(isl_words)

    print("\nGenerated English sentence:")
    print(sentence)
