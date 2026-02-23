from common.response.response_body import BaseResponseBody,Annotated,DateFormat,datetime

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