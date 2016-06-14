from http.server import HTTPServer, BaseHTTPRequestHandler

import sys
import urllib.request
import json

response = None


class StoreHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.return_http_200()

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/xml')
        self.end_headers()
        self.wfile.write(bytes(response, "utf8"))
        length = self.headers['content-length']
        data = self.rfile.read(int(length)).decode("utf-8")

        params = data.split("&")
        sys.stderr.write("[%s] %s\n" % (self.log_date_time_string(), params))

    def log_message(self, format, *args):
        return

    def return_http_200(self):
        self.send_header('Content-type', 'text/json')
        self.send_response(200, 'OK')
        self.end_headers()


def get_ngrok_url():
    with urllib.request.urlopen('http://localhost:4040/api/tunnels') as response:
        tunnels = json.loads(response.read().decode("utf-8"))

        # tunnels.get("tunnels")[0].get("public_url")
        return tunnels.get("tunnels")[1].get("public_url")


if __name__ == '__main__':
    url = get_ngrok_url()
    response = '<?xml version="1.0" encoding="UTF-8"?><Response onAnswer="{}" onHangup="{}" />'.format(
        url, url)

    server = HTTPServer(('', 5000), StoreHandler)
    server.serve_forever()
