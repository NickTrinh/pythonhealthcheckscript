from plyer import notification
import time
import schedule

def send_notification(title, message):
    notification.notify(
        title = title,
        message = message
    )

def main():
    schedule.every(1).hours.do(send_notification, title="Hydration Time!", message="Take a moment to drink some water.")
    schedule.every(2).hours.do(send_notification, title="Break Time!", message="Time to stretch and take a short break.")
    time.sleep(1)


if __name__ == "__main__":
    main()


