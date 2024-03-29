from tkinter import *
from plyer import notification
import threading
import schedule
import time

def send_notification(message):
    notification.notify(
        title="Reminder",
        message=message,
        timeout=10,
        app_name="Your Health Checker"
    )

def run_reminders():
    while True:
        schedule.run_pending()
        time.sleep(1)

class ReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Reminder App")
        master.geometry("400x300")  # Set initial size to 800x600 pixels
        self.reminders = {}

        # Input for reminder message
        Label(master, text="Message:").pack()
        self.message_entry = Entry(master)
        self.message_entry.pack()

        # Input for reminder interval
        Label(master, text="Interval (minutes):").pack()
        self.interval_entry = Entry(master)
        self.interval_entry.pack()

        # Button to add a reminder
        Button(master, text="Add Reminder", command=self.add_reminder).pack()

        # Section to display added reminders
        self.reminders_frame = LabelFrame(master, text="Added Reminders")
        self.reminders_frame.pack(fill="both", expand="yes")

        # Initialize the background thread for reminders
        self.reminder_thread = threading.Thread(target=run_reminders, daemon=True)
        self.reminder_thread.start()

    def add_reminder(self):
        message = self.message_entry.get()
        try:
            interval = int(self.interval_entry.get())
            job = schedule.every(interval).minutes.do(send_notification, message=message)
            label, delete_button = self.update_reminders_display(message, interval, job)
            self.reminders[job] = (label, delete_button)  # Store the job, its label, and its delete button
        except ValueError:
            print("Please enter a valid number for the interval.")  # Console feedback

    def delete_reminder(self, job):
        if job in self.reminders:
            schedule.cancel_job(job)  # Cancel the job
            label, delete_button = self.reminders[job]
            label.destroy()  # Remove the label from the GUI
            delete_button.destroy()  # Remove the delete button from the GUI
            del self.reminders[job]  # Remove the job from the dictionary
        else:
            print(f"Job not found: {job}")

    def update_reminders_display(self, message, interval, job):
        # Display the new reminder in the reminders frame
        label = Label(self.reminders_frame, text=f"Every {interval} minutes: {message}")
        label.pack()
        # Add a delete button for this reminder
        delete_button = Button(self.reminders_frame, text="Delete", command=lambda: self.delete_reminder(job))
        delete_button.pack()
        # Optionally, clear the input fields after adding a reminder
        self.message_entry.delete(0, END)
        self.interval_entry.delete(0, END)
        return label, delete_button  # Return the label


def main():
    root = Tk()
    app = ReminderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()