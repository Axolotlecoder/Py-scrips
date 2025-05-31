import webbrowser
import urllib.parse

def web_search(query):
    base_url = 'https://www.google.com/search?q='
    search_query = urllib.parse.quote(query)
    webbrowser.open(base_url + search_query)

web_search('Python programming tutorials')
