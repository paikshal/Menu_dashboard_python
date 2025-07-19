from instagrapi import Client
import os
import logging

def post_instagram_photo(username, password, image_path, caption):
    """
    Posts a photo to Instagram using instagrapi.
    Args:
        username (str): Instagram username
        password (str): Instagram password
        image_path (str): Path to the image file
        caption (str): Caption for the post
    Returns:
        str: Success message or error message
    """
    if not os.path.exists(image_path):
        return f"Error: Image not found at path: {image_path}"
    try:
        cl = Client()
        cl.login(username, password)
        cl.photo_upload(path=image_path, caption=caption)
        return "✅ Image posted successfully!"
    except Exception as e:
        logging.error(f"Instagram post error: {e}")
        return f"Error posting image: {e}" 