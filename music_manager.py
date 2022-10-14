import os
from apscheduler.schedulers.blocking import BlockingScheduler
import time

run = """osascript -e 'tell application "Spotify"
	play track "spotify:playlist:31BU4oBitkjrSzZd4IY67V?si=27f0f055d3834ba4"
end tell'""", "Playing music"

stop = """osascript -e 'tell application "Spotify"
	pause
end tell'""", "Stop music"


def execute(action):
    print("Executing: " + action[1] + f" at {time.strftime('%H:%M:%S')}")
    os.system(action[0])


intervals = [('mon-fri', (7, 00), (20, 55)), ('sat-sun', (9, 00), (18, 55))]

# test section to check permissions from macOS
execute(stop)
execute(run)

print("📅 Starting scheduler...")

scheduler = BlockingScheduler()
for interval in intervals:
    scheduler.add_job(execute, 'cron', [run],
                      day_of_week=interval[0], hour=interval[1][0], minute=interval[1][1])
    scheduler.add_job(execute, 'cron', [stop],
                      day_of_week=interval[0], hour=interval[2][0], minute=interval[2][1])

scheduler.start()
