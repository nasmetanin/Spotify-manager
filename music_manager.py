import os
import schedule
import time

run = """osascript -e 'tell application "Spotify"
	play track "spotify:playlist:37i9dQZF1DWWY64wDtewQt?si=73c375e585d943bb"
end tell'""", "Playing music"

stop = """osascript -e 'tell application "Spotify"
	pause
end tell'""", "Stop music"

weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
weekends = ['saturday', 'sunday']


def execute(action):
    print("Executing: " + action[1] + f" at {time.strftime('%H:%M:%S')}")
    os.system(action[0])

print("📅 Starting scheduler...")
for day in weekdays:
    schedule.every().day.at("06:45").do(execute, run)
    schedule.every().day.at("20:55").do(execute, stop)

print("📅 Starting scheduler for weekends too...")
for day in weekends:
    schedule.every().day.at("08:45").do(execute, run)
    schedule.every().day.at("18:55").do(execute, stop)

print("💤 Scheduler started! Going to sleep...")

while True:
    schedule.run_pending()
    time.sleep(1)
