#To create map of website use the site_map(url), url domain !! ought !! to be http://127.0.0.1:8000/

import requests
from bs4 import BeautifulSoup

def transform_link(href, url):
    #returning transformed href to format -> http://127.0.0.1:8000/ + internallink
    if href[0:4] != url[0:4]:
            href = url[0:21] + href
    if href[0:20] == "http://0.0.0.0:8000/":
        href = "http://127.0.0.1:8000/" + href[20:len(href)]
    return href

def check_site(url):
    #takes the url and returns dictionary with url as a key and <title>'s slot as title, and all the links in the array 
    links = []    
    soup = BeautifulSoup(requests.get(url).text, features="html.parser")
    
    for link in soup.findAll("a"):
        href = link.get("href")
        transformed_href = transform_link(href,url)
        if transformed_href[0:10] == url[0:10]:
            links.append(transformed_href)        
    
    title = soup.title.string
    
    return {url: {"title": title, "links": links}}

def check_looping(dictionary, link):
    #condition to check for potential looping -> ? True: False
    print("Clarence is having fun browsing the internet :)")
    return link in dictionary


def site_map(url, dictionary = {}):  
    #recurent function generating map of website links  
    checked_site = check_site(url)
    dictionary[list(checked_site)[0]] = checked_site[list(checked_site)[0]]
    links = checked_site[list(checked_site)[0]]["links"]
    for link in links:
        if check_looping(dictionary,link):
            print("Clarence unfortunately had lost the path :(")
            pass
        else: 
            site_map(link, dictionary=dictionary)
    return dictionary

print(site_map("http://127.0.0.1:8000/" ))
