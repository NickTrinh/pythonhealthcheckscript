from plyer import notification
import time
import schedule

def send_notification(title, message):
    notification.notify(
        title = title,
        message = message
    )

def run_reminders():
    while True:
        next_run = schedule.idle_seconds()
        if next_run is None:
            # No more jobs; can break or continue as needed
            break
        elif next_run > 0:
            # Sleep until the next scheduled job should run
            time.sleep(next_run)
        schedule.run_pending()


def setup_reminders():
    schedule.every(1).hours.do(send_notification, title="Hydration Time!", message="Take a moment to drink some water.")
    schedule.every(2).hours.do(send_notification, title="Break Time!", message="Time to stretch and take a short break.")

def main():
    setup_reminders()
    run_reminders()


if __name__ == "__main__":
    main()


