# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time, requests
import json

# import all the functions from our function filefromyourfilename.py
from web3helpers import *

hostName = "0.0.0.0"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>ETHAPIGET</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request:%s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an exampleweb server.</p>", "utf-8"))

    def do_POST(self):
        self.send_response(201)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>ETHAPIPOST</title></head>", "utf-8"))
        self.query_string = self.rfile.read(int(self.headers["Content-Length"]))
        data = json.loads(self.query_string)
        if self.path == "/eth":
            amount = data["amount"]
            address = data["address"]
            self.wfile.write(bytes("<br><p>Transferring ETH...</p>", "utf-8"))
            ethTransfer(address, amount)

        if self.path == "/token":
            address = data["address"]
            self.wfile.write(bytes("<br><p>Transferring Token...</p>", "utf-8"))
            tokenTransfer(address)


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))
    try:
        webServer.serve_forever()

    except KeyboardInterrupt:
        pass

    webServer.server_close()

    print("Server stopped.")
