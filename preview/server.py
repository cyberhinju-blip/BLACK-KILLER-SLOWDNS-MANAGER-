#!/usr/bin/env python3
import http.server
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass

print("BLACK KILLER preview running on port 5000")
http.server.HTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
