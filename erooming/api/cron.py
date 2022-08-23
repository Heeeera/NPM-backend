from turtle import update
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Routine
from datetime import datetime, date

def update_routine_status():
    print("-----update db-----")
    routines = Routine.objects.all()
    
    for routine in routines :
        if(routine.status == 'ready' and routine.start_date <= date.today()) :
            routine.status = 'active'
            routine.save()

def main():
    sched = BackgroundScheduler()
    sched.add_job(update_routine_status,'cron', day_of_week='mon-sun', hour=0, minute=0)
    sched.start()