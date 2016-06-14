from http.server import HTTPServer, BaseHTTPRequestHandler

import sys

url = "https://57f3f52c.eu.ngrok.io"
response = '<?xml version="1.0" encoding="UTF-8"?><Response onAnswer="{}" onHangup="{}" />'.format(url, url)


class StoreHandler(BaseHTTPRequestHandler):
    log = ""

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


if __name__ == '__main__':
    server = HTTPServer(('', 5000), StoreHandler)
    server.serve_forever()
