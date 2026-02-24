from enum import Enum

class TaskRunningStatus(str,Enum):
    SUCCESS = "0"
    FAILED = "1"


class TaskStatus(str,Enum):
    RUNNING = "2"
    STOP = "0"