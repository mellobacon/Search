import fire
import requests
from bs4 import BeautifulSoup
from googlesearch import search

"""
Module to search Google using the cmd.

Args:

Search: keyword to search
Results: number of results
Keywords: keywords for query
Site: filter by website
Domain: top level domain (.com,.net etc.)
"""

# i got lazy here. bleh
print("Google Search CMD\nSearch: Your search query\nNumber of results: Results to search and return\nKeywords: Extra keywords to narrow down the search. Can be empty\nSite: Search from specific sites only. Can be empty\nDomain: Website domain. Can be empty")

def googlesearch(query="",g="com",k="",r=""):
    """
    Search google using specified parameters

    query: keyword to search

    g: top level domain (.com,.net etc.)

    k: keywords for query

    r: number of results
    """
    print("\n")

    query = input("Search: ")

    r = input("Number of results: ")
    if r == "":
        print("No results set. Defaulting to 10.")
        r = 10

    k = input("Keywords: ")
    if "none" in k or "None" in k:
        k = ""
    else:
        query = query + k

    site = input("Site: ")
    if "none" in site or "None" in site:
        sitespecific = False
    else:
        sitespecific = True

    g = input("Domain: ")  # specifies tld
    if "none" in g or "None" in g or "default" in g or "Default" in g:
        g = "com"  # default is .com
    
    Search = search(query, num_results=int(r), lang="en")  # search google

    count = 0  # counts number of urls found
    scount = 0  # counts number of urls found within specific site parameter
    print("\n")

    # prints urls
    for link in Search:
        if sitespecific:  # checks if results will be site specific or not
            if site in link:  # results shown will be from site specified
                    print(link)
                    scount +=1
        else:
            print(link)
        count += 1

    print("\n")
    print("{} result(s) found.".format(count))  # for keeping track of number of results
    if sitespecific:
        print("Out of {} result(s), {} result(s) were found.".format(count,scount))
        if scount == 0:
            print("Try expanding the search or changing the keyword.")

fire.Fire(googlesearch)


