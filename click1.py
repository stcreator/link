from pynput import mouse, keyboard

print("Click anywhere on the screen.")
print("Press ESC to stop.\n")

click_count = 0  # Serial number counter

def on_click(x, y, button, pressed):
    global click_count
    if pressed:
        click_count += 1
        print(f"{click_count}. Mouse clicked at X={x}, Y={y}, Button={button}")

def on_press(key):
    if key == keyboard.Key.esc:
        print("\nStopping listener...")
        return False

# Start mouse and keyboard listeners
with mouse.Listener(on_click=on_click) as mouse_listener:
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()
