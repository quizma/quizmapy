import webview
import threading
import time
import socket
import requests
from PIL import Image

URL = "https://quizma.github.io/quizma/"
VERSION = "1.0.0"

#gimmie ur internet!

def has_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False


#splash size an then you divide it by two

img = Image.open("assets/loading.png")
w, h = img.size
w, h = w // 2, h // 2

#slash window (frmeless)

splash = webview.create_window(
    "Updater",
    "splash.html",
    width=w,
    height=h,
    resizable=False,
    frameless=True
)

#main window

main_window = webview.create_window(
    "pygame",
    URL,
    width=1000,
    height=720,
    resizable=True
)

#startup logic

def startup():
    time.sleep(2)  # splash time

    # check internet
    if not has_internet():
        main_window.load_url("offline.html")

    # optional update check
    try:
        latest = requests.get(
            "https://quizma.github.io/quizma/version.txt",
            timeout=5
        ).text.strip()

        if latest != VERSION:
            print("Update available:", latest)
    except:
        pass

    # CLOSE SPLASH → SHOW MAIN WINDOW
    webview.windows[0].destroy()  # close splash

# run startup
threading.Thread(target=startup).start()

#both windows

webview.start()
import webview
import threading
import time
import socket
import requests
from PIL import Image

URL = "https://quizma.github.io/quizma/"
VERSION = "1.0.0"

#gimmie ur internet!

def has_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        return True
    except:
        return False


#splash size an then you divide it by two

img = Image.open("assets/loading.png")
w, h = img.size
w, h = w // 2, h // 2

#slash window (frmeless)

splash = webview.create_window(
    "Updater",
    "splash.html",
    width=w,
    height=h,
    resizable=False,
    frameless=True
)

#main window

main_window = webview.create_window(
    "pygame",
    URL,
    width=1000,
    height=720,
    resizable=True
)

#startup logic

def startup():
    time.sleep(2)  # splash time

    # check internet
    if not has_internet():
        main_window.load_url("offline.html")

    # optional update check
    try:
        latest = requests.get(
            "https://quizma.github.io/quizma/version.txt",
            timeout=5
        ).text.strip()

        if latest != VERSION:
            print("Update available:", latest)
    except:
        pass

    # CLOSE SPLASH → SHOW MAIN WINDOW
    webview.windows[0].destroy()  # close splash

# run startup
threading.Thread(target=startup).start()

#both windows

webview.start()
