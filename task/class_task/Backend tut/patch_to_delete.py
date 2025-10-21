from http.server import BaseHTTPRequestHandler, HTTPServer
import json

# Shared data
DATA = {
    "name": "ChrisDev",
    "track": "Backend Engineering",
    "age": 25
}

class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, payload, status=200):
        """Helper method to send JSON responses"""
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    # View all data
    def do_GET(self):
        self.send_data({"DATA": DATA}, 200)

    # PATCH: Update a specific field in DATA
    def do_PATCH(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        patch_data = json.loads(body)

        updated_fields = []

        for key, value in patch_data.items():
            if key in DATA:
                DATA[key] = value
                updated_fields.append(key)
            else:
                self.send_data({"error": f"Field '{key}' not found"}, 404)
                return

        self.send_data({
            "message": "Field(s) updated successfully",
            "updated_fields": updated_fields,
            "new_DATA": DATA
        }, 200)

    # DELETE: Remove a specific field from DATA
    def do_DELETE(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        delete_data = json.loads(body)

        deleted_fields = []

        for key in delete_data.keys():
            if key in DATA:
                del DATA[key]
                deleted_fields.append(key)
            else:
                self.send_data({"error": f"Field '{key}' not found"}, 404)
                return

        self.send_data({
            "message": "Field(s) deleted successfully",
            "deleted_fields": deleted_fields,
            "new_DATA": DATA
        }, 200)

def run():
    print("✅ Server running at http://localhost:5000")
    HTTPServer(('localhost', 5000), BasicAPI).serve_forever()

if __name__ == "__main__":
    run()
