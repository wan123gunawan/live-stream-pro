import schedule
import time

def start_scheduler(job_func):
    schedule.every().day.at("08:00").do(job_func)
    schedule.every().day.at("20:00").do(job_func)

    while True:
        schedule.run_pending()
        time.sleep(1)
