
from bs4 import BeautifulSoup
import requests



wiki_url = 'https://en.wikipedia.org/wiki/History_of_Mexico'



def get_citations_needed_count(url):

    # First Step getting the html 
    response = requests.get(url)

    html_text = response.text


    # Second step Parsing the html into usable parts
    parsed_html = BeautifulSoup( html_text,'html.parser')

    wanted_content = parsed_html.find_all('sup', class_= 'noprint Inline-Template Template-Fact')
   
    return len(wanted_content)


def get_citations_needed_report(url):


    response = requests.get(url)

    html_text = response.text


    # Second step Parsing the html into usable parts
    parsed_html = BeautifulSoup( html_text,'html.parser')

    wanted_content = parsed_html.find_all('sup', class_= 'noprint Inline-Template Template-Fact')
    string = ""

    for paragraph in wanted_content:
        paragraph.parent.find('sup').clear()
        paragraph_after = paragraph.parent.text
        string = string + f'Citation needed for {paragraph_after}' 
    return string

print(get_citations_needed_report(wiki_url))
