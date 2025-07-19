# main.py
import os
from whatsapp_twilio import send_whatsapp_twilio
from whatsapp_pywhatkit import send_whatsapp_pywhatkit
from caller import call_using_twilio, open_calling_app
from email_sender import send_email
from instagram_poster import post_to_instagram
from sms_sender import send_sms
from ssh_remote import ssh_execute_command

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        print("\n--- Main Feature Menu ---")
        print("1. Send WhatsApp (Twilio)")
        print("2. Send WhatsApp (PyWhatKit)")
        print("3. Call using Twilio")
        print("4. Call using System Default App")
        print("5. Send Email")
        print("6. Post to Instagram")
        print("7. Send SMS")
        print("8. SSH Remote Access")
        print("0. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                to = input("Enter WhatsApp number (with country code): ")
                msg = input("Enter message: ")
                print(send_whatsapp_twilio(to, msg))

            elif choice == "2":
                to = input("Enter WhatsApp number (with country code): ")
                msg = input("Enter message: ")
                print(send_whatsapp_pywhatkit(to, msg))

            elif choice == "3":
                to = input("Enter number to call (with country code): ")
                print(call_using_twilio(to))

            elif choice == "4":
                number = input("Enter phone number to call: ")
                print(open_calling_app(number))

            elif choice == "5":
                to = input("Recipient Email: ")
                sub = input("Subject: ")
                body = input("Body: ")
                print(send_email(to, sub, body))

            elif choice == "6":
                username = input("Instagram username: ")
                password = input("Instagram password: ")
                img = input("Path to image: ")
                caption = input("Caption: ")
                print(post_to_instagram(username, password, img, caption))

            elif choice == "7":
                to = input("Enter phone number (with country code): ")
                msg = input("Message: ")
                print(send_sms(to, msg))

            elif choice == "8":
                host = input("Enter hostname/IP: ")
                port_input = input("Enter port (default 22): ") or "22"
                try:
                    port = int(port_input)
                except ValueError:
                    print("❌ Invalid port number. Using default port 22.")
                    port = 22
                user = input("Enter username: ")
                use_key = input("Use public key? (y/n): ").lower() == "y"

                if use_key:
                    key_path = input("Path to public key file: ")
                    print(ssh_connect(host, port, user, key_path=key_path))
                else:
                    password = input("Enter password: ")
                    print(ssh_connect(host, port, user, password=password))

            elif choice == "0":
                print("Exiting... 👋")
                break
            else:
                print("❌ Invalid option!")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

if __name__ == "__main__":
    clear()
    menu()