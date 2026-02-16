import yaml
from pathlib import Path
from typing import Any

class ConfigReader:
    _instance = "ConfigReader" | None = None
    _CONFIG_FILE = Path("resource/application.yml")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self,"_data") and getattr(self,"_data",None):
            return
        self._data : dict[str,Any] = {}

    def load(self):
        with self._CONFIG_FILE.open("r",encoding="utf-8") as f:
            self._data = yaml.safe_load(f) or {}   

