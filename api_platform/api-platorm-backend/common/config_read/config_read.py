from __future__ import annotations
from pathlib import Path
from typing import Any
import yaml

class ConfigReader:
    _instance: ConfigReader | None = None

    def __new__(cls, module_name: str):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, module_name: str):
        if hasattr(self, "_data") and getattr(self, "_data", None):
            return

        self._data: dict[str, Any] = {}

        project_root = Path(__file__).resolve().parent.parent.parent
        self._CONFIG_FILE = project_root / module_name / "resource" / "application.yml"

        if not self._CONFIG_FILE.exists():
            raise FileNotFoundError(f"Config file not found: {self._CONFIG_FILE}")

    def load(self) -> dict[str, Any]:
        with self._CONFIG_FILE.open("r", encoding="utf-8") as f:
            self._data = yaml.safe_load(f) or {}
        return self._data