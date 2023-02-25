# Deadline-Reminder
Python script which gets .ics file (calendar file format) and checks deadlines for next day and emails you if there is any.
I have made it to get assignment deadlines from LMS website of my university.

# How to automate the script to get reminders automatically
For Linux -

Run the setup.sh

      cd Deadline-Reminder
      ./setup.sh
Note- Change the path of mail.py according to your directory
      nohup.out will store the system output
      crontab schedule expression can be changed as per the need. Checkout https://crontab.guru/
      
For Windows -

1. Open the Task Scheduler by searching for it in the Start Menu or by typing taskschd.msc in the Run dialog box (press Win+R to open the Run dialog box).
2. Click on the "Create Task" link in the right-hand pane.
3. In the "General" tab, give your task a name and description.
4. In the "Triggers" tab, click on "New" and select "Daily" if you want to run the task every day. You can then specify the start date and time, as well as the frequency and duration of the task.
5. n the "Actions" tab, click on "New" and select "Start a program". In the "Program/script" field, enter the path to the Python interpreter (e.g., C:\Python39\python.exe) and in the "Add arguments (optional)" field, enter the path to the mail.py Python script (e.g., "C:\Users\username\mail.py").
6. In the "Conditions" tab, you can specify additional conditions for running the task, such as whether the computer should be idle or plugged in.
7. In the "Settings" tab, you can configure various settings for the task, such as whether the task should be run even if the user is not logged on, or whether the task should stop if it runs for too long.
8. Click "OK" to save the task
  
