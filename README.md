# Deadline-Reminder
Python script which gets .ics file (calendar file format) and checks deadlines for next day and emails you if there is any.

I have made it to get assignment deadlines from LMS website of my university.

# How to automate the script to get reminders automatically
For Linux -
Run the setup.sh file
Note- Change the path of mail.py according to your directory
      nohup.out will store the system output
      crontab schedule expression can be changed as per the need. Checkout https://crontab.guru/
      
For Windows -
    Open the Task Scheduler by searching for it in the Start Menu or by typing taskschd.msc in the Run dialog box (press Win+R to open the Run dialog box).

    Click on the "Create Task" link in the right-hand pane.

    In the "General" tab, give your task a name and description.

    In the "Triggers" tab, click on "New" and select "Daily" if you want to run the task every day. You can then specify the start date and time, as well as the frequency and duration of the task.

    In the "Actions" tab, click on "New" and select "Start a program". In the "Program/script" field, enter the path to the Python interpreter (e.g., C:\Python39\python.exe) and in the "Add arguments (optional)" field, enter the path to the mail.py Python script (e.g., "C:\Users\username\mail.py").

    In the "Conditions" tab, you can specify additional conditions for running the task, such as whether the computer should be idle or plugged in.

    In the "Settings" tab, you can configure various settings for the task, such as whether the task should be run even if the user is not logged on, or whether the task should stop if it runs for too long.

    Click "OK" to save the task.

