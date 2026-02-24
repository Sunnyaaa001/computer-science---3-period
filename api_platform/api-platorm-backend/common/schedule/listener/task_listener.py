from apscheduler.events import JobExecutionEvent
from common.schedule.enum.task_enum import TaskRunningStatus
from datetime import datetime
from common.docerator.docerator import Transactional
import traceback
from common.schedule.model.task_info import SysTaskLog
from common.db.session import AsyncSession
import asyncio

def job_listener(event:JobExecutionEvent):
    asyncio.create_task(event_process(event=event))

async def event_process(event:JobExecutionEvent):
     task_id = event.job_id
     start_time = event.scheduled_run_time

     if event.exception:
        status = TaskRunningStatus.FAILED
        error = "".join(traceback.format_tb(event.traceback)) if event.traceback else str(event.exception)
        result = None
     else:
        status = TaskRunningStatus.SUCCESS
        result = str(event.retval)
        error = None

     await save_task_log(task_id,status,error,result,start_time)


@Transactional
async def save_task_log(job_id:int,status:str,error:str,result:str,start_time:datetime,session:AsyncSession):
    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    log = SysTaskLog(
        task_id = job_id,
        status = status,
        start_time = start_time,
        end_time = end_time,
        run_time_seconds = duration,
        result = result,
        error = error
    )
    session.add(log)
