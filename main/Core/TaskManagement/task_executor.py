
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from Core.CommandExecutor.system_commands import open_application, execute_system_command

# def execute_task(task):
#     """
#     Executes a task based on its action and target.
#     """
#     try:
#         if task["action"] == "open":
#             open_application(task["target"])
#         elif task["action"] == "system":
#             execute_system_command(task["target"])
#         else:
#             print(f"Unknown task: {task}")
#     except KeyError as e:
#         print(f"Task format error, missing key: {e}")
#     except Exception as e:
#         print(f"Error executing task: {e}")

def execute_task(task):
    """
    Executes a task based on its action and target.
    """
    try:
        action = task.get("action")
        target = task.get("target")
        
        if action == "open":
            logging.info(f"Opening application: {target}")
            open_application(target)
        elif action == "restart" or action == "shutdown":
            logging.info(f"Executing system command: {action}")
            execute_system_command(action)
        else:
            logging.error(f"Unknown task: {action} with target: {target}")
    except KeyError as e:
        logging.error(f"Task format error, missing key: {e}")
    except Exception as e:
        logging.error(f"Error executing task: {e}")


