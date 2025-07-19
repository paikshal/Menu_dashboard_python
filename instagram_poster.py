"""
Instagram poster using instabot.
"""

from instabot import Bot
import os

def post_to_instagram(username: str, password: str, image_path: str, caption: str) -> str:
    try:
        bot = Bot()
        bot.login(username=username, password=password)
        bot.upload_photo(image_path, caption=caption)
        return "Posted to Instagram successfully."
    except Exception as e:
        return f"Instagram post failed: {str(e)}"