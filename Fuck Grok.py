# import requests
# import json

# cookies = {
#     'x-anonuserid': '8ce7be6d-63fe-4080-9dae-42d5e54e14a2',
#     'x-challenge': 'lxz218uncl8JX13UYwE0EsW4928JMfZCIopULCgzUJzmQEK1A%2FM0jwh7LUOOARnUvYxCaBI3WIZNJj2cxDjTjd%2BTXuf8YovPfcDhJI4o14nkbAfBpVn6Ev2mSzhqoSD1oJWdoWxe8uRk5dfYF170lNp8A9%2BxiVQfeO3g9tjRNYW5UBNhBvc%3D',
#     'x-signature': 'LVhjg9FO2llIw9AbZeE2j2aR2RwLmpKfqP4WQlKLZeEj%2FdH17GXJBq3RFpywZMTpJJm7A1IFuESALw425p7yUA%3D%3D',
#     'sso-rw': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
#     'sso': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
# }

# headers = {
#     'accept': '*/*',
#     'accept-language': 'zh-CN,zh;q=0.9',
#     'baggage': 'sentry-environment=production,sentry-release=iBZQ8t-jVt21Zx5DPQ8BK,sentry-public_key=b311e0f2690c81f25e2c4cf6d4f7ce1c,sentry-trace_id=47d4a625b7a64bb4af19e469904db2ba,sentry-sample_rate=1,sentry-sampled=true',
#     'content-type': 'application/json',
#     'origin': 'https://grok.com',
#     'priority': 'u=1, i',
#     'referer': 'https://grok.com/',
#     'sec-ch-ua': '"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'sentry-trace': '47d4a625b7a64bb4af19e469904db2ba-bb86410b9fcb4064-1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
#     # 'cookie': 'x-anonuserid=8ce7be6d-63fe-4080-9dae-42d5e54e14a2; x-challenge=lxz218uncl8JX13UYwE0EsW4928JMfZCIopULCgzUJzmQEK1A%2FM0jwh7LUOOARnUvYxCaBI3WIZNJj2cxDjTjd%2BTXuf8YovPfcDhJI4o14nkbAfBpVn6Ev2mSzhqoSD1oJWdoWxe8uRk5dfYF170lNp8A9%2BxiVQfeO3g9tjRNYW5UBNhBvc%3D; x-signature=LVhjg9FO2llIw9AbZeE2j2aR2RwLmpKfqP4WQlKLZeEj%2FdH17GXJBq3RFpywZMTpJJm7A1IFuESALw425p7yUA%3D%3D; sso-rw=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM; sso=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
# }

# first_json_data = {
#     'temporary': False,
#     'modelName': 'grok-latest',
#     'message': '',
#     'fileAttachments': [],
#     'imageAttachments': [],
#     'disableSearch': False,
#     'enableImageGeneration': True,
#     'returnImageBytes': False,
#     'returnRawGrokInXaiRequest': False,
#     'enableImageStreaming': True,
#     'imageGenerationCount': 2,
#     'forceConcise': False,
#     'toolOverrides': {},
#     'enableSideBySide': True,
#     'isPreset': False,
#     'sendFinalMetadata': True,
#     'customInstructions': '',
#     'deepsearchPreset': '',
#     'isReasoning': False,
# }

import requests
import json

cookies = {
    'x-anonuserid': '8ce7be6d-63fe-4080-9dae-42d5e54e14a2',
    'x-challenge': 'lxz218uncl8JX13UYwE0EsW4928JMfZCIopULCgzUJzmQEK1A%2FM0jwh7LUOOARnUvYxCaBI3WIZNJj2cxDjTjd%2BTXuf8YovPfcDhJI4o14nkbAfBpVn6Ev2mSzhqoSD1oJWdoWxe8uRk5dfYF170lNp8A9%2BxiVQfeO3g9tjRNYW5UBNhBvc%3D',
    'x-signature': 'LVhjg9FO2llIw9AbZeE2j2aR2RwLmpKfqP4WQlKLZeEj%2FdH17GXJBq3RFpywZMTpJJm7A1IFuESALw425p7yUA%3D%3D',
    'sso-rw': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
    'sso': 'eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
    '_ga': 'GA1.1.1183786358.1740222063',
    '_ga_8FEWB057YH': 'GS1.1.1740222062.1.1.1740222796.0.0.0',
}

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
    # 'cookie': 'x-anonuserid=8ce7be6d-63fe-4080-9dae-42d5e54e14a2; x-challenge=lxz218uncl8JX13UYwE0EsW4928JMfZCIopULCgzUJzmQEK1A%2FM0jwh7LUOOARnUvYxCaBI3WIZNJj2cxDjTjd%2BTXuf8YovPfcDhJI4o14nkbAfBpVn6Ev2mSzhqoSD1oJWdoWxe8uRk5dfYF170lNp8A9%2BxiVQfeO3g9tjRNYW5UBNhBvc%3D; x-signature=LVhjg9FO2llIw9AbZeE2j2aR2RwLmpKfqP4WQlKLZeEj%2FdH17GXJBq3RFpywZMTpJJm7A1IFuESALw425p7yUA%3D%3D; sso-rw=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM; sso=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoiYTA4ODA0OTctM2IwYy00OGVkLThkNjctYjFmMGU4ZDM3YjI2In0.XGHRa75aNnU9VCVGZdeopENyjE274GMPEce9bW-L4wM',
}

# first_json_data = {
#     'temporary': False,
#     'modelName': 'grok-latest',
#     'message': '',
#     'fileAttachments': [],
#     'imageAttachments': [],
#     'disableSearch': False,
#     'enableImageGeneration': True,
#     'returnImageBytes': False,
#     'returnRawGrokInXaiRequest': False,
#     'enableImageStreaming': True,
#     'imageGenerationCount': 2,
#     'forceConcise': False,
#     'toolOverrides': {
#         'imageGen': False,
#         'webSearch': False,
#         'xSearch': False,
#         'xMediaSearch': False,
#         'trendsSearch': False,
#         'xPostAnalyze': False,
#     },
#     'enableSideBySide': True,
#     'isPreset': False,
#     'sendFinalMetadata': True,
#     'customInstructions': '',
#     'deepsearchPreset': '',
# }

# next_json_data = {
#     'message': '',
#     'modelName': 'grok-latest',
#     'parentResponseId': '',
#     'disableSearch': False,
#     'enableImageGeneration': True,
#     'imageAttachments': [],
#     'returnImageBytes': False,
#     'returnRawGrokInXaiRequest': False,
#     'fileAttachments': [],
#     'enableImageStreaming': True,
#     'imageGenerationCount': 2,
#     'forceConcise': False,
#     'toolOverrides': {},
#     'enableSideBySide': True,
#     'sendFinalMetadata': True,
#     'customInstructions': '',
#     'deepsearchPreset': '',
#     'isReasoning': False,
# }

first_json_data = {
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

# send data continuious
next_json_data = {
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

counter = 0

while(True):
    question = input("Ask Question: ")
    first_json_data['message'] = question
    counter += 1
    if counter == 1:
        response = requests.post('https://grok.com/rest/app-chat/conversations/new', cookies=cookies, headers=headers, json=first_json_data)
        # print(response.text)
        first_response_json = json.loads(response.text.splitlines()[0])
        session_Id = first_response_json['result']['conversation']['conversationId']
        # print(response.text.splitlines()[1])
        first_response_json = json.loads(response.text.splitlines()[2])
        response_Id = first_response_json['result']['response']['responseId']
        # print (session_Id)
        # print (response_Id)
        next_json_data["parentResponseId"] = response_Id
    else:
        response = requests.post('https://grok.com/rest/app-chat/conversations/'+session_Id+'/responses', cookies=cookies, headers=headers, json=next_json_data)
        # print(response.text)
        next_json_data["parentResponseId"] = json.loads(response.text.splitlines()[1])['result']['responseId']
    respones_text_index = -1
    while True:
        try:
            print(json.loads(response.text.splitlines()[respones_text_index])['result']['response']['modelResponse']['message'])
            break
        except Exception:
            respones_text_index -= 1
            continue
