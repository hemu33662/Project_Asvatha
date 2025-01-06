# ASVATHA

Asvatha is an intelligent, voice-driven AI assistant designed to perform tasks on a computer through natural language commands. It combines voice recognition, natural language processing, and task management systems to provide a seamless and efficient experience for users.

---

## Pre-requisites
- Python 3.9+
- Libraries:
  - SpeechRecognition
  - Pyttsx3
  - Queue

---

## Features

- **Voice Recognition**:
  Converts user speech into text for further processing.

- **Command Parsing**:
  Analyzes and understands the user's intent from their spoken input.

- **Task Management**:
  Efficiently queues and executes tasks based on user commands.

- **Error Detection**:
  Identifies incomplete or invalid commands, ensuring no unintended tasks are performed.

- **Command Handlers**:
  - **Open Applications** (e.g., "open Chrome")
  - **System Commands**:
    - Restart (e.g., "restart system")
    - Shutdown (e.g., "shutdown device")

---

## Designing the Voice Assistant

Designing Asvatha involves implementing a modular structure that allows the assistant to process natural language commands and execute tasks efficiently. Below is the high-level design approach:

### 1. Input Processing
- Convert user speech to text using the **SpeechRecognition** library.
- Handle background noise and improve recognition accuracy.

### 2. Command Parsing
- Analyze the recognized text to determine the user’s intent.
- Route parsed commands to the appropriate handler functions.

### 3. Task Management
- Queue user commands and execute them sequentially.
- Manage task dependencies and handle overlapping commands gracefully.

### 4. Error Detection and Handling
- Identify and rectify ambiguous or incomplete commands.
- Prompt the user for clarification if necessary.

### 5. Execution Flow
- Once validated, tasks are executed using appropriate system commands or APIs.

---

## Demo

![System Interaction](Asvatha_Demo_1.png)
![Task Execution](Asvatha_Demo_2.png)

---

## Results

The following features are successfully implemented in Sprint 1:
- **Speech-to-Text Conversion**: Robust recognition of user commands.
- **Command Parsing**: Handles diverse commands with flexibility.
- **Error Handling**: Prevents invalid tasks from execution.

Performance testing is underway to optimize task execution and system response.

---

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-repo-url>/Asvatha.git
   cd Asvatha
## Authors

- [Hemanth Nasaram](https://github.com/hemu33662)
<!-- voice -->
