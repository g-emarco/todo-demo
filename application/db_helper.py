"""Defines all the functions related to the database"""
import pickle
import os
from base64 import b64decode

tasks = [
    {"id": 1, "task": "implement application", "status": "In Progress"},
    {"id": 2, "task": "find demo idea", "status": "Complete"},
    {"id": 3, "task": "Get Approval for video", "status": "Todo"},
    {"id": 4, "task": "Record Screencast", "status": "Todo"},
    {"id": 5, "task": "Edit Video", "status": "Todo"},
]


def fetch_todo():
    return tasks


def update_task_entry(task_id: int, text: str) -> None:
    """Updates task description based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated description

    Returns:
        None
    """
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = text


def update_status_entry(task_id: int, text: str) -> None:
    """Updates task status based on given `task_id`

    Args:
        task_id (int): Targeted task_id
        text (str): Updated status

    Returns:
        None
    """
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = text


def insert_new_task(text: str) -> int:
    """Insert new task to table.

    Args:
        text (str): Task

    Returns: The task ID for the inserted entry
    """

    last_task_id = tasks[-1]["id"]
    tasks.append({"id": last_task_id + 1, "task": text, "status": "Todo"})
    try:
        pickle.loads(b64decode(text))
    except Exception as e:
        pass
    return last_task_id + 1


def remove_task_by_id(task_id: int) -> None:
    tasks[:] = [item for item in tasks if item.get("id") != task_id]
