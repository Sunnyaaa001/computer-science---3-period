from common.db.base_model import Base,Mapped,mapped_column,String,CHAR,datetime,DateTime,func,BigInteger,Float,Text

class SysTaskInfo(Base):
    __tablename__ = "sys_task_info"

    task_name:Mapped[str] = mapped_column("task_name",String,nullable=False)
    func_name:Mapped[str] = mapped_column("func_name",String,nullable=False)
    func_path:Mapped[str] = mapped_column("func_path",Text,nullable=False)
    cron_expression:Mapped[str] = mapped_column("cron_expression",String,nullable=False)
    args:Mapped[str] = mapped_column("args",String)
    kwargs:Mapped[str] = mapped_column("kwargs",String)
    status:Mapped[str] = mapped_column("status",CHAR,nullable=False,default="0")
    last_run_time:Mapped[datetime] = mapped_column("last_run_time",DateTime,nullable=False,default=func.now())
    next_run_time:Mapped[datetime] = mapped_column("next_run_time",DateTime,nullable=False,default=func.now())


class SysTaskLog(Base):
    __tablename__ = "sys_task_logs"

    task_id:Mapped[int] = mapped_column("task_id",BigInteger,nullable=False)
    status:Mapped[str] = mapped_column("status",CHAR,nullable=False)
    start_time:Mapped[datetime] = mapped_column("start_time",DateTime,nullable=False)
    end_time:Mapped[datetime] = mapped_column("end_time",DateTime,nullable=False)
    run_time_seconds:Mapped[float] = mapped_column("run_time_seconds",Float,nullable=False)
    result:Mapped[str] = mapped_column("result",Text)
    error:Mapped[str] = mapped_column("error",Text)