import schedule
import time
import threading

def job():
    print("📡 Running auto prediction...")

def start_auto_prediction(app):
    schedule.every(3).minutes.do(job)

    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    thread = threading.Thread(target=run_scheduler)
    thread.start()
