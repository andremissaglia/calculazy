#!/usr/bin/env python

import sys
import os
import sympy
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".ico"):
            self.send_response(404)
            return
            
            self.send_response(200)
            self.end_headers()
        try:
            input = self.path[1:]
            value = str(sympy.simplify(input)).strip()
            self.wfile.write(value)
            print "evaluated", input, "=", value
            
        except Exception as e:
            self.wfile.write("couldn't evaluate that")
            print "error on", self.path
        finally:
            self.close_connection()
    
    def do_POST(self):
        pass
        
    def log_message(self, format, *args):
        return

def main():
   port = int(os.environ.get('PORT') or 80)
   server = HTTPServer(('', port), EchoHandler)
   print 'serving on port', port
   server.serve_forever()
    
if __name__ == '__main__':
    sys.exit(int(main() or 0))