#!/bin/bash
nohup python3 mail.py &
crontab -l | { cat; echo " 30 17 * * 0-6 /home/nabh/Documents/projects/ICS Deadline Email/mail.py"; } | crontab -
