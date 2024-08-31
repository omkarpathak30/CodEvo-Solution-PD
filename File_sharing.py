import http.server
import socketserver
import pyqrcode
import png
import os
import webbrowser
from urllib.parse import urlparse

# Configuration
PORT = 8000
USER_NAME = 'User'
DIRECTORY = os.getcwd()  # Directory to serve files from

# Handler to serve files
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def start_server():
    handler = RequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f"Serving at port {PORT}")

    # Get the local IP address
    hostname = os.popen('hostname').read().strip()
    local_ip = os.popen(f'ping -c 1 {hostname}').read().split()[2].strip('()')
    
    # Generate the URL
    url = f"http://{local_ip}:{PORT}"
    print(f"Access your files at: {url}")

    # Generate QR code
    qr = pyqrcode.create(url)
    qr.png('file_sharing_qr.png', scale=6)
    
    # Open QR code image in browser
    webbrowser.open('file_sharing_qr.png')

    # Start the server
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()
