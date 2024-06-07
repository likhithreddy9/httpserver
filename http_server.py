gpio = {}
gpio_num = None
action = None

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
            gpio_num = self.path.split("/")[1].split("gpio")[1]
            action = self.path.split("/")[2]
            if not gpio_num in gpio:
              gpio[gpio_num] = 0 
            if action == "on":
                gpio_state[gpio_num] = 1
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("OK", "utf-8"))
            elif action == "off":
                gpio[gpio_num] = 0
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("OK", "utf-8"))
            elif action == "status":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                data = {"status": gpio_state[gpio_num]}
                self.wfile.write(bytes(json.dumps(data), "utf-8")) 
            else:
                self.send_response(400)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes("Invalid action", "utf-8"))
       else:
           self.send_response(404)
           self.send_header("Content-type", "text/plain")
           self.end_headers()
           self.wfile.write(bytes("Not Found", "utf-8"))
         
def run_server():
    server_address = ('127.0.0.1', 8000)
    httpd = HTTPServer(server_address, MyServer)
    print("Starting server on port 8000...")
    httpd.serve_forever()

run_server()

