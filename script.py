import requests
import json
with open("taskernet_shares.csv", "a") as myfile:
   print("Name, Url")
   myfile.write("Name, Url  \n")
   myfile.close()

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
            with open("taskernet_shares.csv", "a") as myfile:
                share_name = share['name']
                share_name = share_name.replace('"', '')
                myfile.write(f"{share_name}, {share['url']}\n")
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

