from pynput import keyboard
from time import perf_counter
from collections import deque


dq = deque([])

current_tap_time = None
last_tap_time = None


# Key handling
def on_press(key):
    if key == keyboard.Key.space:
        tap_start = perf_counter()

    if key == keyboard.Key.esc:
        return False


# Init listener that watches for key presses
listener = keyboard.Listener(on_press=on_press, on_release=on_release)


def main():
    print("Tap the space key along to the music :>")


if __name__ == "__main__":
    main()
