from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.events import EVENT_JOB_ERROR,EVENT_JOB_EXECUTED
from apscheduler.triggers.cron import CronTrigger
from common.schedule.listener.task_listener import job_listener
import threading
from datetime import datetime

class APScheduler:
    _instance:BackgroundScheduler = None
    _lock = threading.Lock()
    _started = False
     
    @staticmethod 
    def _create_scheduler(pool:int,coalesce:bool,max_instance:int,timezone:str):
        executors = {"default": ThreadPoolExecutor(pool)}
        job_default = {
            "coalesce": coalesce,
            "max_instances":max_instance
        }
        return BackgroundScheduler(
            executors = executors,
            job_defaults = job_default,
            timezone = timezone,
            daemon = True
        )
    
    @classmethod
    def init(cls,pool:int,coalesce:bool,max_instance:int,timezone:str):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls._create_scheduler(pool,coalesce,max_instance,timezone)

        return cls._instance
    
    @classmethod
    def start(cls):
        if cls._instance and not cls._started:
           cls._instance.start()
           cls._started = True

    @classmethod
    def add_task(cls,task_info:dict):
        if cls._instance:
           trigger = CronTrigger.from_crontab(task_info["trigger"])
           cls._instance.add_job(
              func=task_info["func_name"],
              trigger=trigger,
              args=task_info.get("args", []),
              kwargs=task_info.get("kwargs", {}),
              id=task_info.get("id")
        )

    @classmethod       
    def remove_task(cls,task_id:int):
        if cls._instance:
            cls._instance.remove_job(task_id)

    @classmethod        
    def remove_all_tasks(cls):
        if cls._instance:
            cls._instance.remove_all_jobs()
    
    @classmethod
    def pause_task(cls,task_id:int):
        if cls._instance:
            cls._instance.pause_job(task_id)

    @classmethod        
    def pause_all_task(cls):
        if cls._instance:
            cls._instance.pause()

    @classmethod        
    def resume_task(cls,task_id:int):
        if cls._instance:
            cls._instance.resume_job(task_id)

    @classmethod        
    def resume_all_tasks(cls):
        if cls._instance:
           cls._instance.resume()

    @classmethod       
    def execute_once(cls,task_info:dict):
        if cls._instance:
            cls._instance.add_job(
              func=task_info["func_name"],
              trigger="date",
              run_date = datetime.now(),
              args=task_info.get("args", []),
              kwargs=task_info.get("kwargs", {}),
              id=task_info.get("id")
        )
            
    @classmethod        
    def add_listener(cls):
        if cls._instance:
            cls._instance.add_listener(job_listener,EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)        







