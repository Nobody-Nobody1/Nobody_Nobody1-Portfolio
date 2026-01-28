import tkinter as tk
import webview

def open_in_window():
    url = entry.get().strip()
    if url and not url.startswith(("http://", "https://")):
        url = "http://" + url
    try:
        webview.create_window("Web Viewer", url)
        webview.start()
    except Exception as e:
        print(f"Error loading page: {e}")

root = tk.Tk()
root.title("Embedded Web Viewer")

tk.Label(root, text="Enter URL:").pack(pady=5)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Open in Tkinter Window", command=open_in_window).pack(pady=10)

root.mainloop()