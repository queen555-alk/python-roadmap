import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class Handler(BaseHTTPRequestHandler):
    def _send(self, data, status=200):
        body = json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/":
            self._send({"status": "ok", "message": "API is running"})
        elif url.path == "/hello":
            name = parse_qs(url.query).get("name", ["world"])[0]
            self._send({"message": f"Hello, {name}!"})
        else:
            self._send({"error": "not found"}, 404)

    def do_POST(self):
        if self.path == "/echo":
            length = int(self.headers.get("Content-Length", 0))
            try:
                data = json.loads(self.rfile.read(length) or b"{}")
            except json.JSONDecodeError:
                return self._send({"error": "invalid JSON"}, 400)
            self._send({"you_sent": data})
        else:
            self._send({"error": "not found"}, 404)


if __name__ == "__main__":
    print("Running on http://localhost:8000")
    HTTPServer(("", 8000), Handler).serve_forever()
