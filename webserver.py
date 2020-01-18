from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime

PORT_NUMBER = 8080

with open("hello.html") as html_file:
	HTML = html_file.read()


def to_bytes(string):
	return string.encode("utf-8")


#This class will handles any incoming request from
#the browser 
class MyHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		params = {x.split("=")[0]: x.split("=")[1] for x in self.path.split("?")[1].split("&")}
		import pdb; pdb.set_trace()
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message

		string = HTML.format(
			timestamp=datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
		)
		self.wfile.write(to_bytes(string))
		return

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('0.0.0.0', PORT_NUMBER), MyHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
