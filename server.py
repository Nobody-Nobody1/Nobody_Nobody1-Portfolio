import http.server
import socketserver
import os

# Directory containing your HTML file
#HTML_DIR = "root"

# Port to run the server on
PORT = 8000

# Change to the directory with the HTML file
#os.chdir(HTML_DIR)

# Create the handler
Handler = http.server.SimpleHTTPRequestHandler

# Start the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()