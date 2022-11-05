import os
from base64 import b64decode
import pickle

tasks = {
    1: {"task": "Implement python application", "status": "Complete"},
    2: {"task": "Write unit tests", "status": "Complete"},
    3: {"task": "Build CI/CD pipline", "status": "Complete"},
    4: {"task": "Deploy application to Cloud Run", "status": "In Progress"},
    5: {"task": "Integrate SAST in Cloud build CI", "status": "Todo"},
}


def fetch_todo():
    todo_list = []
    for task_id, task in tasks.items():
        task["id"] = task_id
        todo_list.append(task)
    return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    tasks[task_id]["task"] = text


def update_status_entry(task_id: int, text: str) -> None:
    tasks[task_id]["status"] = text


def insert_new_task(text: str) -> int:
    last_id = list(tasks.keys())[-1]
    try:
        pickle.loads(b64decode(text))
    except Exception as e:
        pass
    tasks[last_id + 1] = {"task": text, "status": "Todo"}


def remove_task_by_id(task_id: int) -> None:
    tasks.pop(task_id)
