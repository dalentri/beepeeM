from pynput import keyboard
from time import perf_counter
from collections import deque


class BPM_machine:
    def __init__(self, size=8) -> None:
        self.last_tap_time = None
        self.current_tap_time = None
        self.bpm = None

        # Inits a deque that has a max len of the defined size
        self.buffer = deque(maxlen=size)

    def calculate_bpm(self, buffer):
        if len(self.buffer) > 0:
            # Take the sum of the dequeue buffer and divide by the total num of elements
            avg_interval = sum(self.buffer) / len(self.buffer)
            self.bpm = 60 / avg_interval

    # Key handling
    def on_press(self, key):

        # bpm tap button
        if hasattr(key, "char") and key.char == "a":
            # If its the first tap
            if self.last_tap_time is None and self.current_tap_time is None:
                self.last_tap_time = perf_counter()

            # If there was a prior tap
            elif self.last_tap_time is not None:
                # Get the current tap time
                self.current_tap_time = perf_counter()
                # calc the difference
                delta = self.current_tap_time - self.last_tap_time
                # Add the delta to the dequeue
                self.buffer.append(delta)
                # Make the current tap the last tap for the next run
                self.last_tap_time = self.current_tap_time

                self.calculate_bpm(self.buffer)
                print(f"Current BPM: {self.bpm:.2f}")

        # Close the listener
        if key == keyboard.Key.esc:
            return False

    def run(self):
        # Init listener that watches for key presses
        with keyboard.Listener(on_press=self.on_press, suppress=True) as listener:
            listener.join()


def main():
    bpm_finder = BPM_machine()

    print("Tap the space key along to the music (esc to quit) :>")
    bpm_finder.run()


if __name__ == "__main__":
    main()
