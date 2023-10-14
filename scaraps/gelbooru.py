import requests
from bs4 import BeautifulSoup

def getscraps():
    url = 'https://gelbooru.com/index.php?page=post&s=list&tags=all'
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
    else:
        print(f"Failed to retrieve the web page (Status Code: {response.status_code})")

    article = soup.find_all("article")
    context = []
    src,title_list=[],[]

    for item in article:
        img = item.find('img')
        src.append(img.get('src'))
        title_list.append(img.get('title'))
    
    for i in range(0,len(src)):
        sub_context = {"image": src[i] , "category":title_list[i]}
        context.append(sub_context)

    data_dict = {item for item in context}
    return(data_dict)

print(getscraps())