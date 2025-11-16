from pyrogram import Client
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import time
import datetime
import pytz

# --- Configuration ---
# Set the desired time zone explicitly to IST
IST = pytz.timezone('Asia/Kolkata')

# Pyrogram Client Setup (Same as before)
API_ID =  24435985
API_HASH = "0fec896446625478537e43906a4829f8"
BOT_TOKEN = "7758738938:AAGwhb8vXtHw9INX8SzCr82PKYtjQJHE-3c"
TARGET_CHAT_ID = -1002183423252

app = Client("my_auto_uploader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# --- Upload Function ---

def upload_anime(anime_name: str, episode_number: int):
    """Function to send the command/trigger the upload process."""
    
    # Get the current time in IST for logging
    current_ist_time = datetime.datetime.now(IST).strftime('%Y-%m-%d %H:%M:%S %Z')

    # Start the client session
    with app:
        command = f"/upload {anime_name} E{episode_number}"
        
        print(f"[{current_ist_time}] Running scheduled job for: {anime_name}")
        
        try:
            app.send_message(
                chat_id=TARGET_CHAT_ID,
                text=command
            )
            print(f"Successfully sent command: {command}")
        except Exception as e:
            print(f"Error sending message for {anime_name}: {e}")


# --- Scheduler Setup ---

def start_scheduler():
    # Initialize the scheduler
    scheduler = BackgroundScheduler(timezone=str(IST))
    
    # 1. Schedule "One Piece"
    # Runs every Saturday (day_of_week='sun') at 10:30 (hour=09, minute=05) IST
    scheduler.add_job(
        upload_anime, 
        trigger=CronTrigger(day_of_week='sun', hour=09, minute=05, timezone=IST),
        id='one_piece_job',
        name='One Piece Auto-Upload',
        kwargs={'anime_name': 'One Piece', 'episode_number': 1120}
    )

    # 2. Schedule "Frieren"
    # Runs every Friday (day_of_week='fri') at 20:00 (8:00 PM) IST
    scheduler.add_job(
        upload_anime,
        trigger=CronTrigger(day_of_week='fri', hour=20, minute=0, timezone=IST),
        id='frieren_job',
        name='Frieren Auto-Upload',
        kwargs={'anime_name': 'Frieren', 'episode_number': 22}
    )

    # Start the scheduler
    scheduler.start()
    print(f"🤖 Auto-Upload Scheduler Started. Base Timezone: {IST}")
    print("Waiting for scheduled job...")

    # Keep the main thread alive so the scheduler can run in the background
    try:
        while True:
            time.sleep(2)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler Shut Down.")


if __name__ == "__main__":
    start_scheduler()
