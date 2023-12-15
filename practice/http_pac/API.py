import requests
import json
import qianfan
chat_comp = qianfan.ChatCompletion(ak="udeXhM30mrwV1lGGhg8LlXK6", sk="y0Q66ZmtiGflkYE718aZ8QZg6ZrM3YpG")

# qianfan.AK("udeXhM30mrwV1lGGhg8LlXK6")
# qianfan.SK("y0Q66ZmtiGflkYE718aZ8QZg6ZrM3YpG")



def main(number1,number2,number3):
        
    # url = "https://aip.baidubce.com/rest/2.0/wenxinworkshop/api/v1/template/info?access_token=24.18be5e908448f6f855f994d8748fc0b7.2592000.1700905022.282335-41799243&id=9731&number1=1&number2=32.5&number3=50.0"
    url = f"https://aip.baidubce.com/rest/2.0/wenxinworkshop/api/v1/template/info?access_token=24.18be5e908448f6f855f994d8748fc0b7.2592000.1700905022.282335-41799243&id=9731&number1={number1}&number2={number2}&number3={number3}"
    
    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # 解析JSON数据
        data = json.loads(response.text)
        
        # 提取content部分
        content = data["result"]["content"]
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    # response = requests.request("GET", url, headers=headers, data=payload)
    # 调用默认模型，即 ERNIE-Bot-turbo
    resp = chat_comp.do(messages=[{
        "role": "user",
        "content": content
    }])
    return resp
    # print(resp)
    # print(response.content)
    

if __name__ == '__main__':
    main()

