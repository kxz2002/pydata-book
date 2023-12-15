from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi
import os
import chardet
from urllib.parse import urlparse, parse_qs
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = "F:\\Repos\\pydata-book\\practice\\http_pac\\index.html"
            try:
                with open(self.path, "rb") as file:
                    content = file.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('content-length',len(content))
                    self.end_headers()
                    self.wfile.write(content)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Not Found')
        elif self.path == '/favicon.ico':
            try:
                with open("F:\\Repos\\pydata-book\\practice\\http_pac\\favicon.ico", "rb") as icon_file:
                    icon_content = icon_file.read()
                    self.send_response(200)
                    self.send_header('Content-type', 'image/x-icon')
                    self.end_headers()
                    self.wfile.write(icon_content)
            except FileNotFoundError:
                self.send_response(404)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(b'404 - Favicon Not Found')
        # elif self.path=='/LLM':
        elif self.path.startswith('/LLM'):
            try:
                # 获取参数
                parsed_path = urlparse(self.path)
                query_params = parse_qs(parsed_path.query)
                print(parsed_path)

                # 获取参数值
                light = query_params.get('Light', [''])[0]
                temperature = query_params.get('Temperature', [''])[0]
                moist = query_params.get('Moist', [''])[0]

                # 组装参数字符串
                # factors = f'factors={{"Light":"{light}","Temperature":"{temperature}","Moist":"{moist}"}}'
                factors = f"Light={light}&Temperature={temperature}&Moist={moist}"
                # 调用API，获取响应
                api_response = self.call_api(factors)  # 自定义的方法，用于调用API
                if api_response is not None:
                    content_len = len(api_response)
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('content-length',content_len)
                    self.end_headers()
                    self.wfile.write(api_response.encode('utf-8'))
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'404 - Not Found')
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(f'500 - Internal Server Error: {str(e)}'.encode('utf-8'))

    # def do_POST(self):
    #     # Parse the form data
    #     form = cgi.FieldStorage(
    #         fp=self.rfile,
    #         headers=self.headers,
    #         environ={'REQUEST_METHOD': 'POST',
    #                  'CONTENT_TYPE': self.headers['Content-Type'],
    #                  }
    #     )

    #     # Get the form values
    #     first_name = form.getvalue("first_name")
    #     last_name = form.getvalue("last_name")

    #     self.send_response(200)
    #     self.send_header('Content-type', 'text/html')
    #     self.end_headers()
    #     self.wfile.write(b'Hello, ' + first_name.encode() + b' ' + last_name.encode())

    def call_api(self,factors):
        # 在这个方法中调用你的API，获取API的响应
        # 这里只是一个示例，你需要根据实际情况实现API的调用逻辑
        try:
            api_url = 'http://127.0.0.1:5000/big_model'  # 替换为你的API地址
            response = requests.get(api_url, params=factors)
            if response.status_code == 200:
                # encoding = chardet.detect(response.content)['encoding']
                txt = response.content.decode('utf-8')
                # print(f"txt:{txt}")
                return txt
            else:
                return None
        except Exception as e:
            return None

httpd = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()