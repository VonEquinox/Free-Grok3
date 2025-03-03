import requests
import json
from GrokCookies import cookies_list

cookies = cookies_list[0]

headers = {
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=hPZj-aOLuqQ3QUlWq1JLg,sentry-public_key=b311e0f2690c81f25e2c4cf6d4f7ce1c,sentry-trace_id=88a45b7adf104accaf5b3534e28427c8,sentry-sample_rate=1,sentry-sampled=true',
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
    'sentry-trace': '88a45b7adf104accaf5b3534e28427c8-9bb73516996b0996-1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
    # 'cookie': '_ga=GA1.1.1049260078.1740896995; cf_clearance=Xjv3mXrBXcMYWFPfk.rKmFTVCg65rzBTxAvWfiq5fME-1740896995-1.2.1.1-YQdZpumZqzgrgam4ZMDlXEbybXjRjjFLYjrF.7V_nNGk7NDLFjwNCE7kO.7ZxZRFgqNjTrRA7S6f02i3lT0mzhOAVWO5HQOFRcU8B2_y57dga7iLW_T__aEwTlkt4PHdV_HTgh6qMNAupogQZztaCJiDn9dbmw6qgdBIMFYVySwGNU0maLZ8j2JhkzRQWeLrbnQWp0BZcpeFuiMLe7eQ7V0BNuuL475m1qgrneQTyVx1ByxRehUFYtPlXImYUbT9QNdfdKnqTwPo.JvozzuDFyXSNun5w4xebrcysOwgIv4GasGhcfz09R9QUN7SSLXibgdEoQBiA_d6GCtImXFfz5VFze6_4VEYB9nJkZKtXXsRJzQJaTKbqIfDxaoqGW.MPTmZOFIrnKRoEa_VHQjTxUi37Xf7xJPBfin06IwCl.Y; x-anonuserid=ee0dc661-3aa1-4e69-96b5-17862de1e85f; x-challenge=Va6w8fHDjn5TEy9HcfVBejL16wH06O%2BkA2sDZOBIUkLx98sl6EWiT8F59%2Fe8LGqD3vcrMwTFJeog%2FbH2W%2FerMBYZeRY2xg2U%2Fl4so2mJrEbovrR65aeLzF1DF6RF8ORVFnHj528xc9Z%2BBjJVg2zYHFBBi2nqFm0pql3nFi4iax69oQIw4GY%3D; x-signature=2%2BSm4M3rBP4THEniE%2BiuHwYkfpJRr9trpdNJA1XjSj508rZWKry9lSUs01VDXNMZ1ZGCWNiv%2BQCAdtnNZCnUmg%3D%3D; sso=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiZTZiZGM0YjktODY4OS00ZDNjLWFmNGUtMTgzOGE5ODE2OTMwIn0.8l379thYDlN2aNhwOgjl9b9n0X6N2DVXSrzfXqXa0-Q; sso-rw=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiZTZiZGM0YjktODY4OS00ZDNjLWFmNGUtMTgzOGE5ODE2OTMwIn0.8l379thYDlN2aNhwOgjl9b9n0X6N2DVXSrzfXqXa0-Q; _ga_8FEWB057YH=GS1.1.1740896995.1.1.1740897026.0.0.0',
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