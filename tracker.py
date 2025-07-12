import random
import datetime

def encrypt_message(message):
    return ''.join(chr(ord(c) + 1) for c in message)

def get_timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

messages = [
    "Backup scheduled at midnight.",
    "Cipher update required.",
    "Check the place where stories go - https://medium.com/@JaceTyronis.",
    "Protocol 7 authorized."
]

def dispatch():
    msg = random.choice(messages)
    print(f"{get_timestamp()} — {encrypt_message(msg)}")

dispatch()
