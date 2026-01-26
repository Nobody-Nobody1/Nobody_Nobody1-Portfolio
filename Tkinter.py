import tkinter as tk
from tkinter import messagebox
import webview

# Function to open the website in a Tkinter-embedded window
def open_website():
    url = url_entry.get().strip()
    if not url.startswith(("http://", "https://")):
        url = "https://" + url  # Ensure proper URL format
    try:
        # Create a new webview window inside Tkinter
        webview.create_window("Website Viewer", url)
        webview.start()
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not load website:\n{e}")

# Main Tkinter window
root = tk.Tk()
root.title("Tkinter Website Viewer")
root.geometry("400x150")

# URL input
tk.Label(root, text="Enter Website URL:").pack(pady=5)
url_entry = tk.Entry(root, width=40)
url_entry.pack(pady=5)
url_entry.insert(0, "https://www.example.com")

# Open button
tk.Button(root, text="Open Website", command=open_website).pack(pady=10)

root.mainloop()
