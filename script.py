import requests
import json

def taskernet(page_token=None):
    base_url = "https://taskernet.com/_ah/api/datashare/v1/shares/public"
    if page_token:
        request = requests.get(base_url + "?a=0&tags=&pageToken=" + page_token)
    else:
        request = requests.get(base_url)
    
    data = json.loads(request.content)
    shares = data["shares"]
    
    for share in shares:
        if shares:
            with open("taskernet_shares.json", "a") as myfile:
                share_name = share['name']
                share_name = share_name.replace('"', '').replace(',', '')
                myfile.write(json.dumps({'type': share['type'], 'share_name': share_name, 'url': share['url'], 'tags': share['tags']}) + '\n')
                print(f" {share_name}, {share['url']}")
                myfile.close()
        else:
            pass
    
    if "pageToken" in data:
        page_token_b = data["pageToken"]
        taskernet(page_token_b)
    else:
        print("No shares found")

taskernet()

