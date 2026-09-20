import http.server
import socketserver
import os

PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == "__main__":
    web_dir = os.path.dirname(__file__)
    if web_dir:
        os.chdir(web_dir)
    
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Сервер запущено: http://localhost:{PORT}")
        print("Натисніть Ctrl+C для зупинки сервера.")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nСервер зупинено.")