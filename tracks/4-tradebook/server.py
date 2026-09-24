import json
import sqlite3
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

BASE = Path(__file__).parent
DB_PATH = BASE / "tradebook.db"
PORT = 8001

class TradebookHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE), **kwargs)

    def do_GET(self):
        if self.path.startswith("/api/trades"):
            self.serve_trades()
        else:
            super().do_GET()

    def serve_trades(self):
        query = parse_qs(urlparse(self.path).query)
        instrument = query.get("instrument", [None])[0]

        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        sql = "SELECT * FROM trades"
        if instrument:
            sql += f" WHERE instrument = '{instrument}'"
        sql += " ORDER BY timestamp"
        rows = conn.execute(sql).fetchall()
        conn.close()

        trades = [dict(r) for r in rows]
        body = json.dumps(trades).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    if not DB_PATH.exists():
        raise SystemExit("tradebook.db not found — run migrate.py first")
    server = ThreadingHTTPServer(("localhost", PORT), TradebookHandler)
    print(f"Serving on http://localhost:{PORT}")
    server.serve_forever()
