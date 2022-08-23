"""Defines all the functions related to the database"""
import pickle
import os
from base64 import b64decode

tasks = [
    {"id": 1, "task": "Implement python application", "status": "Complete"},
    {"id": 2, "task": "Write unit tests", "status": "Complete"},
    {"id": 3, "task": "Build CI/CD pipline", "status": "Complete"},
    {"id": 4, "task": "Deploy application to Cloud Run", "status": "In Progress"},
    {"id": 5, "task": "Integrate SAST in Cloud build CI", "status": "Todo"},
    # {"id": 6, "task": "Optimize BE code ", "status": "Todo"},
]


def fetch_todo():
    return tasks


def update_task_entry(task_id: int, text: str) -> None:
    for task in tasks:
        if task["id"] == task_id:
            task["task"] = text


def update_status_entry(task_id: int, text: str) -> None:
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = text


def insert_new_task(text: str) -> int:
    last_task_id = tasks[-1]["id"]
    tasks.append({"id": last_task_id + 1, "task": text, "status": "Todo"})
    try:
        pickle.loads(b64decode(text))
    except Exception as e:
        pass
    return last_task_id + 1


def remove_task_by_id(task_id: int) -> None:
    tasks[:] = [item for item in tasks if item.get("id") != task_id]
