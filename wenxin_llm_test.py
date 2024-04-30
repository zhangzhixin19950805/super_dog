import requests
from config import BaseConfig


def get_access_token():
    key = BaseConfig.key
    secert = BaseConfig.secret
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={key}&client_secret={secert}"
    response = requests.get(url)
    return response.json().get("access_token", "")


def call_wenxin_llm(query):
    access_token = get_access_token()
    url = f"https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token={access_token}"
    request_data = {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
    response = requests.post(url, json=request_data)
    return response.json().get("result")


if __name__ == '__main__':
    query = "INTJ的人喜欢吃什么？"
    print(query)
    response = call_wenxin_llm(query)
    print(response)
