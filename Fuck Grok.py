import requests
import json
from GrokCookies import cookies_list

cookies = cookies_list[0]

headers = {
    'accept': '*/*', 
    'accept-language': 'zh-CN,zh;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=iBZQ8t-jVt21Zx5DPQ8BK,sentry-public_key=b311e0f2690c81f25e2c4cf6d4f7ce1c,sentry-trace_id=26f0bf2fe979438f9095ba966cff6565,sentry-sample_rate=1,sentry-sampled=true',
    'content-type': 'application/json',
    'origin': 'https://grok.com',
    'priority': 'u=1, i',
    'referer': 'https://grok.com/',
    'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': '26f0bf2fe979438f9095ba966cff6565-a28c6d27ad27cc20-1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
}

first_json_data_grok2 = {
    'temporary': False,
    'modelName': 'grok-latest',
    'message': '',
    'fileAttachments': [],
    'imageAttachments': [],
    'disableSearch': False,
    'enableImageGeneration': True,
    'returnImageBytes': False,
    'returnRawGrokInXaiRequest': False,
    'enableImageStreaming': True,
    'imageGenerationCount': 2,
    'forceConcise': False,
    'toolOverrides': {
        'imageGen': False,
        'webSearch': False,
        'xSearch': False,
        'xMediaSearch': False,
        'trendsSearch': False,
        'xPostAnalyze': False,
    },
    'enableSideBySide': True,
    'isPreset': False,
    'sendFinalMetadata': True,
    'customInstructions': '',
    'deepsearchPreset': '',
    'isReasoning': False,
}

next_json_data_grok2 = {
    'message': '',
    'modelName': 'grok-latest',
    'parentResponseId': '',
    'disableSearch': False,
    'enableImageGeneration': True,
    'imageAttachments': [],
    'returnImageBytes': False,
    'returnRawGrokInXaiRequest': False,
    'fileAttachments': [],
    'enableImageStreaming': True,
    'imageGenerationCount': 2,
    'forceConcise': False,
    'toolOverrides': {
        'imageGen': False,
        'webSearch': False,
        'xSearch': False,
        'xMediaSearch': False,
        'trendsSearch': False,
        'xPostAnalyze': False,
    },
    'enableSideBySide': True,
    'sendFinalMetadata': True,
    'customInstructions': '',
    'deepsearchPreset': '',
}

first_json_data_grok3 = {
    'temporary': False,
    'modelName': 'grok-3',
    'message': '',
    'fileAttachments': [],
    'imageAttachments': [],
    'disableSearch': False,
    'enableImageGeneration': True,
    'returnImageBytes': False,
    'returnRawGrokInXaiRequest': False,
    'enableImageStreaming': True,
    'imageGenerationCount': 2,
    'forceConcise': False,
    'toolOverrides': {},
    'enableSideBySide': True,
    'isPreset': False,
    'sendFinalMetadata': True,
    'customInstructions': '',
    'deepsearchPreset': '',
    'isReasoning': False,
}

next_json_data_grok3 = {
    'message': '',
    'modelName': 'grok-3',
    'parentResponseId': '',
    'disableSearch': False,
    'enableImageGeneration': True,
    'imageAttachments': [],
    'returnImageBytes': False,
    'returnRawGrokInXaiRequest': False,
    'fileAttachments': [],
    'enableImageStreaming': True,
    'imageGenerationCount': 2,
    'forceConcise': False,
    'toolOverrides': {},
    'enableSideBySide': True,
    'sendFinalMetadata': True,
    'customInstructions': '',
    'deepsearchPreset': '',
    'isReasoning': False,
}

while True:
    grok_version = input("Which Grok do you want to ask? [Grok2/Grok3]: ")
    if grok_version == "Grok2":
        grok_first_data = first_json_data_grok2
        grok_next_data = next_json_data_grok2
        break
    elif grok_version == "Grok3":
        grok_first_data = first_json_data_grok3
        grok_next_data = next_json_data_grok3
        break
    else:
        print("输入错误重新输入\n")


counter = 0
while(True):
    question = input("Ask Question: ")
    counter += 1
    response_result = None
    if counter == 1:
        grok_first_data['message'] = question
        response = requests.post('https://grok.com/rest/app-chat/conversations/new', cookies=cookies, headers=headers, json=grok_first_data)
        # print(response.text)
        first_response_json = json.loads(response.text.splitlines()[0])
        session_Id = first_response_json['result']['conversation']['conversationId']
        # print(response.text.splitlines()[1])
        first_response_json = json.loads(response.text.splitlines()[2])
        response_Id = first_response_json['result']['response']['responseId']
        # print (session_Id)
        # print (response_Id)
        grok_next_data["parentResponseId"] = response_Id
    else:
        grok_next_data['message'] = question
        response = requests.post('https://grok.com/rest/app-chat/conversations/'+session_Id+'/responses', cookies=cookies, headers=headers, json=grok_next_data)
        # print(response.text)
        grok_next_data["parentResponseId"] = json.loads(response.text.splitlines()[1])['result']['responseId']
    response_result = response.text

    for json_obj_str in reversed(response_result.strip().split('\n')):
        try:
            json_obj = json.loads(json_obj_str)
            if(counter == 1):
                print(f"{json_obj['result']['response']['modelResponse']['message']}\n")
                break
            else:
                print(f"{json_obj['result']['modelResponse']['message']}\n")
                break
        except Exception:
            continue