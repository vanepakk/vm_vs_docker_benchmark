import http.server
import socketserver
import os

PORT = 8000
DIR = os.path.join(os.path.dirname(__file__), '..', 'tetris')

os.chdir(DIR)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🎮 Tetris server running at http://localhost:{PORT}")
    httpd.serve_forever()
