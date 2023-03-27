from email import message
from http.server import HTTPServer, BaseHTTPRequestHandler

from urllib.parse import parse_qs

class dlrHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path.endswith('/ack'):
            length = int(self.headers.get('Content-length', 0))

            data = self.rfile.read(length).decode()
            message = parse_qs(data)["message"][0]

            print(message)

            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()
            self.wfile.write('ACK/Jasmin'.encode())


def main():
    PORT = 3000
    server = HTTPServer(('localhost', PORT), dlrHandler)
    print('server is running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()