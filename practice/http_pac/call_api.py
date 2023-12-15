import sys
sys.path.append("F:\Repos\pydata-book\practice\http_pac")
import SparkApi
import json
#以下密钥信息从控制台获取
appid = "bb2c98bc"     #填写控制台中获取的 APPID 信息
api_secret = "NzI1YzUxMDUxNWYzMTg3ZDUxZjdjYTQ3"   #填写控制台中获取的 APISecret 信息
api_key ="d9a1737235317827ec7ef73316e7e22a"    #填写控制台中获取的 APIKey 信息

#用于配置大模型版本，默认“general/generalv2”
# domain = "general"   # v1.5版本
domain = "generalv2"    # v2.0版本
#云端环境的服务地址
# Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址


text =[]
# func_call = []

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

# def get_function_call(arguments):
#     jsoncon = {}
#     if arguments:  # 检查 arguments 是否非空
#         jsoncon['arguments'] = json.dumps(arguments)
#         func_call.append(jsoncon)
#     return func_call

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    
def callAPI(factors):
    text.clear()
    # Input = input("\n" +"我:")
    Input = factors
    question = checklen(getText("user",Input))
    # if question == "quit":
    #     break
    SparkApi.answer =""
    print("星火:",end = "")
    SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
    getText("assistant",SparkApi.answer)
    # print(str(text))
    return text

if __name__ == '__main__':
    callAPI()

