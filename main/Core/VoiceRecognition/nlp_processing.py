import spacy

# Load the spaCy model for NLP processing
nlp = spacy.load("en_core_web_sm")

def process_command(command):
    """
    Process the command using NLP to extract the intent (action) and target (object).
    
    Args:
    - command (str): The command input from the user.
    
    Returns:
    - intent (str): The action the user wants to perform (e.g., "open", "restart").
    - target (str): The object the action is applied to (e.g., "Notepad", "Chrome").
    """
    # Process the command using spaCy
    doc = nlp(command.lower())  # Process the command in lowercase to ensure consistency
    
    # Debugging the processed command
    print(f"Processed command: {command}")
    
    # Define a list of possible actions (intents)
    possible_actions = ["open", "close", "restart", "shutdown", "search"]
    
    # Extract keywords from the command to identify the intent and target
    intent = None
    target = None

    # Search for an action (intent) from the command
    for token in doc:
        if token.lemma_ in possible_actions:
            intent = token.lemma_
            break  # Stop after finding the first action
    
    # Debugging the extracted intent
    print(f"Detected intent: {intent}")
    
    # If an intent is found, look for the target (the noun or object)
    if intent:
        # Extract a noun or named entity after the verb to serve as the target
        for ent in doc.ents:
            if ent.label_ == "ORG" or ent.label_ == "GPE" or ent.label_ == "PRODUCT":
                target = ent.text
                break
        
        # If no named entity, extract the noun closest to the verb
        if not target:
            for token in doc:
                if token.pos_ == "NOUN":
                    target = token.text
                    break

        # Debugging the extracted target
        print(f"Detected target: {target}")
    
    return intent, target
