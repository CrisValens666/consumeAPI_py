import requests, json

if __name__ == '__main__':

    url = 'https://httpbin.org/post'    
    payload = {'image': 'xxx', 'portContainer': '443'}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    # response = requests.put(url, data=json.dumps(payload), headers=headers)
    # response = requests.delete(url, data=json.dumps(payload), headers=headers)
    
    if response.status_code == 200:
        content = response.content 
        # print(content)
        
        headers_response = response.headers
        server = headers_response['Server']
        print(server)
        
        json_object = json.loads(content)
        json_formatted_str = json.dumps(json_object, indent=2)
        
        print(json_formatted_str)
