from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from datetime import datetime

class TaskInfoParam(BaseModel):
    task_name: str = Field(..., description="Name of the task")
    cron_expression: str = Field(..., description="Cron expression, e.g., '*/5 * * * *'")
    func_name: str = Field(..., description="Task execution function, format: module.func")
    args: Optional[List] = Field(default_factory=list, description="List of positional arguments")
    kwargs: Optional[Dict] = Field(default_factory=dict, description="Dictionary of keyword arguments")
    status: Optional[str] = Field(default='0', description="Task status: 0=stop, 1=pause, 2=run")
    last_run_time: Optional[datetime] = Field(default=None, description="Last run time of the task")
    next_run_time: Optional[datetime] = Field(default=None, description="Next scheduled run time")