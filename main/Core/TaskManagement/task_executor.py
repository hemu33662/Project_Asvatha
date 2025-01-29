
import logging
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from Core.CommandExecutor.system_commands import open_application, execute_system_command, handle_screenshot_task

def execute_task(task):
    """
    Executes a task based on its action and target.
    """
    try:
        action = task.get("action")
        target = task.get("target")

        if action == "open" and not target:
            logging.error(f"Missing target for action: {action}. Task details: {task}")
            return

        
        if action == "open":
            logging.info(f"Opening application: {target}")
            open_application(target)
        elif action == "restart" or action == "shutdown":
            logging.info(f"Executing system command: {action}")
            execute_system_command(action)
        elif task == "screenshot":
            result = handle_screenshot_task()  # Trigger screen reading task
            print(result)  # Optionally print the result for debugging
        else:
            logging.error(f"Unknown task: {action} with target: {target}")
    except KeyError as e:
        logging.error(f"Task format error, missing key: {e}")
    except Exception as e:
        logging.error(f"Error executing task: {e}")


# Test cases
task_1 = {"action": "open", "target": "notepad"}
execute_task(task_1)

# task_2 = {"action": "shutdown", "target": None}
# execute_task(task_2)

task_3 = {"action": "invalid_action", "target": "unknown"}
execute_task(task_3)

# task_4 = {"action": "restart", "target": None}
# execute_task(task_4)
