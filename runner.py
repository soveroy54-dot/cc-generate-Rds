import subprocess
import time

while True:
    try:
        print("Starting bot.py ...")
        subprocess.run(["python3", "bot.py"])
    except Exception as e:
        print(f"Bot crashed: {e}")
    print("Restarting in 5 seconds...")
    time.sleep(5)
