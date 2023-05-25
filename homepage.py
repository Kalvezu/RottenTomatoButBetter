import http.server
import webbrowser

class PageHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        if self.path == '/':
            with open('pages/homepage.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8'))
        elif self.path == '/about':
            with open('pages/about.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8'))
        elif self.path == '/homepage':
            with open('pages/homepage.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8'))
        elif self.path == '/crud':
            with open('pages/crud.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8')) 
        elif self.path == '/impress':
            with open('pages/impress.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8'))
        elif self.path == '/login':
            with open('pages/login.html', 'r') as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, 'utf-8'))
        else:
            self.send_error(404, 'Page Not Found')

def start_server():
    server_address = ('', 8000)  # Empty string indicates localhost
    httpd = http.server.HTTPServer(server_address, PageHandler)
    print('Server running at http://localhost:8000/homepage')
    webbrowser.open('http://localhost:8000')  # Open the browser automatically
    httpd.serve_forever()

if __name__ == '__main__':
    start_server()