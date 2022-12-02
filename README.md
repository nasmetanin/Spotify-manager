# Spotify macOS automation script

Script allows you to automate playing playlist according to the schedule you choose. ***Script is macOS only***, since it uses the Apple Script language.
You can preset time, a day of a week or basically any schedule you want.[^1]

To run preset use background running mode: 
> output is needed for logs of the program 

`nohup python3 -u ./music_manager.py > output.log &`

To check if the script is running use: 

`ps -x | grep python`

[^1]: Soon I'll think about adding more customization features.

