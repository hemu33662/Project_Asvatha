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
    possible_actions = [
        "open", "launch", "start", 
        "close", "exit", "quit", 
        "restart", "reboot", 
        "shutdown", "turn off", 
        "search", "find", 
        "change", "adjust", "set", 
        "pause", "resume", "stop", 
        "maximize", "minimize", "restore", 
        "mute", "unmute", "volume up", "volume down", 
        "lock", "unlock", "sign out", 
        "copy", "paste", "cut", "delete", 
        "screenshot", "take"
    ]
    
    # Expand actions with possible synonyms for flexibility
    action_synonyms = {
        "close": ["close", "exit", "quit", "shut down"],
        "open": ["open", "launch", "start", "run"],
        "restart": ["restart", "reboot", "relaunch"],
        "shutdown": ["shutdown", "turn off", "power off"],
        "maximize": ["maximize", "expand"],
        "minimize": ["minimize", "shrink"],
        "volume": ["volume up", "volume down", "mute", "unmute"]
    }
    
    # Extract intent and target
    intent = None
    target = None
    
    # Search for an action (intent) from the command
    for token in doc:
        # Lemmatization allows for matching actions even if the user uses different word forms
        if token.lemma_ in possible_actions:
            intent = token.lemma_
            break  # Stop after finding the first action
    
    # Debugging the extracted intent
    print(f"Detected intent: {intent}")
    
    # If no explicit action is found, try to check for action synonyms
    if not intent:
        for action, synonyms in action_synonyms.items():
            if any(synonym in command for synonym in synonyms):
                intent = action
                break
    
    # Handle special cases where the command might just be to "exit"
    if 'exit' in command:
        return 'exit', None

    # If an intent is found, look for the target (the noun or object)
    if intent:
        # Extract a noun or named entity after the verb to serve as the target
        for ent in doc.ents:
            if ent.label_ in ["ORG", "GPE", "PRODUCT"]:
                target = ent.text
                break
        
        # If no named entity, extract the noun closest to the verb
        if not target:
            for token in doc:
                if token.pos_ == "NOUN":  # Looking for noun (e.g., Chrome)
                    target = token.text
                    break
        
        # If the command implies a file or directory, treat it as a target (e.g., "open file.txt")
        if not target:
            for token in doc:
                if token.pos_ == "PROPN" or token.pos_ == "NUM":
                    target = token.text
                    break
    
        # Debugging the extracted target
        print(f"Detected target: {target}")
    
    return intent, target

