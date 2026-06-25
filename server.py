#!/usr/bin/env python3
"""
JEE 2027 PWA local server
Run: python server.py
Then open: http://localhost:8000  (or your LAN IP for phone)
"""
import http.server, socketserver, os

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Required for service worker scope
        self.send_header('Service-Worker-Allowed', '/')
        super().end_headers()
    def log_message(self, fmt, *args):
        print(f"  {args[0]} {args[1]}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    print(f"\n  JEE 2027 PWA Server running")
    print(f"  Local:   http://localhost:{PORT}")
    print(f"  Network: http://{ip}:{PORT}  ← open this on your phone")
    print(f"\n  Press Ctrl+C to stop\n")
    httpd.serve_forever()
