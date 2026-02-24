from common.response.response_body import BaseResponseBody,Annotated,DateFormat,datetime
from typing import Optional

class TaskResponse(BaseResponseBody):
    task_name: str
    func_name: str
    func_path: str
    cron_expression: str
    args: str | None
    kwargs: str | None
    status: str
    last_run_time: Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]
    next_run_time: Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]


class TaskLogResponse(BaseResponseBody):
    task_id:int
    status: int
    start_time: Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]
    end_time: Optional[Annotated[datetime, DateFormat("%Y-%m-%d %H:%M:%S")]] = None
    run_time_seconds: Optional[float] = None
    result: Optional[str] = None
    error: Optional[str] = None

