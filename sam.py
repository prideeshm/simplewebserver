from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
      <title>top 5 software industries</title>
      <body>
             <table border="2" cellspacing="10" cellpaddding="6">
                     <caption> Top 5 Revenue Generating Software Companies </caption>
                     <tr>
<th>s.no</th>
<th>companies</th>
<th>revenue</th> 
</tr>  
<tr> 
<th>1</th>
<th>Microsoft</th>
<th>65 billion</th>
</tr>
<tr>
<th>2</th>
<th>oracle</th>
<th>29.5 billon</th>
</tr>
<tr>
<th>3</th>
<th>IBM </th>
<th>29.1 billon</th>
</tr>
<tr>
<th>4</th>
<th>SAP</th>
<th>6.4 billon</yh>
</tr>
<tr>
<th>5</th>
<th>symentec</th>
<th>5.6 billion</th>
</boby>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()