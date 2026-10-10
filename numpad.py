import tkinter as tk
import subprocess

root = tk.Tk()
root.title("Numpad")
root.overrideredirect(True)
root.attributes('-topmost', True)
root.geometry('+100+100')

def press(key):
    subprocess.run(['xdotool', 'key', key])

keys = [
    ('7','7'), ('8','8'), ('9','9'), ('/','slash'),
    ('4','4'), ('5','5'), ('6','6'), ('*','asterisk'),
    ('1','1'), ('2','2'), ('3','3'), ('-','minus'),
    ('0','0'), ('.','period'), ('=','Return'), ('+','plus'),
]

# Add backspace row
keys.append(('⌫','BackSpace'))

for i, (label, code) in enumerate(keys):
    r, c = divmod(i, 4)
    btn = tk.Button(root, text=label, font=('Arial', 16), width=3, height=1,
                    command=lambda c=code: press(c))
    btn.grid(row=r, column=c, padx=2, pady=2)

# --- Drag to move (since no title bar) ---
def on_press(event):
    root._drag_x = event.x
    root._drag_y = event.y

def on_drag(event):
    x = root.winfo_x() + event.x - root._drag_x
    y = root.winfo_y() + event.y - root._drag_y
    root.geometry(f'+{x}+{y}')

# Bind drag to the whole window background
root.bind('<ButtonPress-1>', on_press)
root.bind('<B1-Motion>', on_drag)

root.mainloop()   
