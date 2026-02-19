import importlib
import pkgutil

class TaskScanner:
    _tasks: dict[str, str] = {}

    @classmethod
    def register(cls, name: str, path: str):
        cls._tasks[name] = path

    @classmethod
    def get(cls, name: str) -> str | None:
        return cls._tasks.get(name)

    @classmethod
    def all(cls):
        return cls._tasks
    
    @staticmethod
    def scan(package: str):

        pkg = importlib.import_module(package)

        for _, mod, _ in pkgutil.walk_packages(
            pkg.__path__,
            pkg.__name__ + "."
        ):
            importlib.import_module(mod)
