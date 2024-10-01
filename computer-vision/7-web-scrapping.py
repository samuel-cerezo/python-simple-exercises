import requests
from bs4 import BeautifulSoup
import pandas as pd

# In order to download a web page, we use requests.get() 
# to send the HTTP request to the server and what the function returns is a response object, which is the HTTP response.
home_url = 'https://eoddata.com/stocklist/TSX/A.htm'   #The URL Address of the webpage we will scrape, i.e. Stocks starting from A
page = requests.get(home_url)      #requests.get()
#print(page.status_code)    #Here we are checking the Status code, -> 200-299 will mean that the request was successful

# Beautiful Soup enables us to get data out of sequences of characters.
page_contents = page.text
soup = BeautifulSoup(page_contents, 'html.parser')  #Now 'doc' contains entire html in parsed format

    # An HTML tag comprises of three parts:
    #   Name: (html, head, body, div, etc.) 
    #       Indicates what the tag represents and how a browser should interpret the information inside it.
    #   Attributes: (href, target, class, id, etc.) 
    #       Properties of tag used by the browser to customize how a tag is displayed and decide what happens on user interactions.
    #   Children: 
    #       A tag can contain some text or other tags or both between the opening and closing segments, e.g., <div>Some content</div>.
    #
    # ---- The most common use, such as <div> tag, <p> tag, <section> tag, <img> tag, <a> tags.

# here we display the first title of the webpage
#title = soup.find('title').text
#print(title)

# Now let’s get the individual td for the first stock, which has all the information required
# Here we get the main trtag for complete stock information. Note we have alternate stocks (with class re and ro) so getting both
tr_parent1 = soup.find_all('tr',{'class':'ro'}) 
tr_parent2 = soup.find_all('tr',{'class':'re'})

# Now let’s get the individual td for the first stock, which has all the information required
td_child1 = tr_parent1[0].find_all('td')
#print(len(td_child1))
company_name = td_child1[1].text.strip()
closing_value = td_child1[4].text.strip()

print('\nNombre de la compañia: ' + company_name)
print('Ultimo valor de la acción: $' + closing_value)

# -------- ahora creamos un diccionario para relevar todos ultimos valores de las acciones

def parse_document(tr_tag):
    td_tag = tr_tag.find_all('td') #viene a ser una fila
    symbol = td_tag[0].find('a').text.strip()
    name = td_tag[1].text.strip()
    high = td_tag[2].text.strip()
    low = td_tag[3].text.strip()
    close = td_tag[4].text.strip()
    volume = td_tag[5].text.strip()
    url = "https://eoddata.com/" + td_tag[0].find('a')['href']
    
    print("Symbol: " + symbol)
    print("Name: " + name)
    print("High: " + high)
    print("Low: " + low)
    print("Close: " + close)
    print("Volume: " + volume)
    print("URL: " + url)

    return {
        'Symbol' : symbol,
        'Name' : name,
        'High' : high,
        'Low' : low,
        'Close' : close,
        'Volume' : volume,
        'URL' : url
    }

def write_csv(items, path):
    with open(path, 'w') as f:
        if len(items) == 0:
            return
        
        headers = list(items[0].keys())
        f.write(','.join(headers) + '\n')

        for item in items:
            values = []
            for header in headers:
                values.append(str(item.get(header, "")))
            f.write(','.join(values) + "\n")


all_records1 = [parse_document(tag) for tag in tr_parent1]
all_records2 = [parse_document(tag) for tag in tr_parent2]

print(len(all_records1))

parse_document(tr_parent1[0])

write_csv(all_records1,"A.csv")
pd.read_csv('A.csv')