import http.server
import socketserver

PORT = 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>It Works!</h1>")
        self.wfile.write(b"<p>If you can see this, your port 3000 is open and accessible.</p>")
        self.wfile.write(b"<p>The issue is likely with the Next.js development server configuration.</p>")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}. Open your browser to http://localhost:{PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        httpd.server_close() 