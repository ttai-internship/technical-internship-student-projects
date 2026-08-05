from .model import Task
from .storage import JsonStorage


class TaskService:
    def __init__(self, storage: JsonStorage) -> None:
        self.storage = storage

    def add(self, title: str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("title cannot be empty")
        tasks = self.storage.load()
        next_id = max((task.id for task in tasks), default=0) + 1
        task = Task.new(next_id, title)
        tasks.append(task)
        self.storage.save(tasks)
        return task

    def list(self) -> list[Task]:
        return self.storage.load()

    def complete(self, task_id: int) -> Task:
        # TODO(student): locate the task, mark it completed, save, and return it.
        raise NotImplementedError("complete is part of the student Core task")

    def delete(self, task_id: int) -> None:
        # TODO(student): delete exactly one task and persist the result.
        raise NotImplementedError("delete is part of the student Core task")
