#(C) Michael Molinari 2019


#--------------------------------------------------Server stuff
import time
import _thread
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote


class Serv(BaseHTTPRequestHandler):
	print("bonjour")
"""	os.system("clear")     #ca ce sont mes choses 
	os.system("ls")
	os.system("docker ps")
	os.system("python3 server.py")
	os.system("python3 resolution.py")"""

	def do_GET(self):
		print(self.path)

		try:
			commandToRun = str(unquote(self.path))
			commandToRun = commandToRun[1:]
			if (commandToRun.startswith("~") == True):
				ShellCommandToRun = commandToRun[1:]
				os.system(ShellCommandToRun)
		except:
			print("probleme d'execution")
		self.send_response(200)
		self.end_headers()
		myReturnMSG = "Welp we did that action"
		self.wfile.write(bytes(myReturnMSG, 'utf-8'))

def runTheServer():
	httpd = HTTPServer(('0.0.0.0', 8001), Serv)
	httpd.serve_forever()




runTheServer()



	