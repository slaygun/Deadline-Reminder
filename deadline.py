from icalendar import Calendar
import requests
from datetime import date,timedelta

# Getting tomorrow's date
datetoday=date.today()
deadline=date.today() + timedelta(1)
deadline=str(deadline)

# iCal URL
url="add your ics url"
#url="https://lms.bennett.edu.in/calendar/export_execute.php?userid=6485&authtoken=ecf6b79c084834aa2c25197da04edfe54392339e&preset_what=all&preset_time=custom"
rep=(requests.get(url))

cal = Calendar.from_ical(rep.text)

# To check if it is getting fetched or not
if rep.status_code!=200:
    body="Failed to fetch calendar from the URL"
    print(body)
    exit()

# Body of the message which we will send via mail
body=""
sub_body=""
#link="https://lms.bennett.edu.in/my/index.php"
body+='{0}\n\n'.format(deadline)

for event in cal.walk('vevent'):
    enddate=str(event.decoded('dtend'))
    enddate=enddate[0:10]
    if deadline == enddate:
        eventname=str(event['summary'])
        endtime=str(event.decoded('dtend'))[10:16]
        desc=str(event['description'])

        #sub_body+='''{0} - {1}\n{2}\n'''.format(eventname,endtime,desc)
        sub_body+='''{0}\n{1}\n'''.format(eventname,desc)

# To check if there is any event
if sub_body=="":
    body=sub_body
elif sub_body!="":
    body+=sub_body
    #body+=link       
print(body)
      

        
        
