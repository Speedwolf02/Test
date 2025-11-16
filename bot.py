from pyrogram import Client

# Initialize your Pyrogram Client
# Replace with your actual credentials
API_ID = 12345
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"
TARGET_CHAT_ID = "@YourAnimeChannel" # The channel/chat where the command is executed

app = Client("my_auto_uploader", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

def upload_anime(anime_name: str, episode_number: int):
    """
    Function to send the command/trigger the upload process.
    
    In a simple bot, this might be a single command message.
    In a complex bot, this might call an internal upload function.
    We'll send a message to trigger the bot.
    """
    
    # 1. Start the client session
    with app:
        # 2. Define the command message
        # Assuming your bot responds to a simple text command
        command = f"/upload {anime_name} E{episode_number}"
        
        print(f"[{time.strftime('%H:%M:%S')}] Attempting to run command: {command}")
        
        # 3. Send the message to the target chat
        try:
            app.send_message(
                chat_id=TARGET_CHAT_ID,
                text=command
            )
            print(f"Successfully sent command for {anime_name} E{episode_number}.")
        except Exception as e:
            print(f"Error sending message for {anime_name}: {e}")

