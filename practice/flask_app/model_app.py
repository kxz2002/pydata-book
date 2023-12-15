from flask import Flask, request, jsonify
import json
import sys

sys.path.append("F:\Repos\pydata-book\practice")
from http_pac import call_api

model_app = Flask(__name__)

# 读取prompt
def load_prompt():
    path = "F:\\Repos\\pydata-book\\practice\\flask_app\\prompt.txt"
    with open(path, "rb") as file:
        content = file.read().decode("utf-8")
        return content

@model_app.route("/big_model", methods=["GET", "POST"])
def get_reply():
    if request.method == "GET":
        prompt = load_prompt()

        # 从请求的查询参数中获取 Light、Temperature 和 Moist 的值
        light = request.args.get('Light', '')
        temperature = request.args.get('Temperature', '')
        moist = request.args.get('Moist', '')

        # 拼装question
        factors = f'{{"Light":"{light}","Temperature":"{temperature}","Moist":"{moist}"}}'
        question = prompt + factors
        reply = call_api.callAPI(question)
        data = json.loads(json.dumps(reply[-1]))
        content = data['content']
        print(content)
        return json.dumps(json.loads(content))

    #    number1 = request.args.get('number1')
    #    number2 = request.args.get('number2')
    #    number3 = request.args.get('number3')
    #    reply = API.main(number1,number2,number3)
    #    return jsonify({'reply': reply})


#    elif request.method == "POST":
#        return create_programming_language(request.get_json(force=True))

if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
    model_app.debug = True
    model_app.run(ip, port, use_reloader=False)
