import requests
from bs4 import BeautifulSoup
import pandas as pd 

def get_soup(url):
    try:
        page = requests.get(url)
        if page.status_code == 200:
            soup = BeautifulSoup(page.text,'html.parser')
            return soup
        else:
            print("page error",page.status_code)
            return None
    except:
        print("Internet error")
        return None

def find_synonyms(word,soup1):
    section  = soup1.find('div',{'class':'css-1gb0efu e1qo4u830'},'ul')        
    synonyms = section.find_all('li')
    syn = []
    for word in synonyms: 
        synonym = word.find('a').text
        syn.append(synonym)
    return syn


def find_def(word,soup2):
    if word:
        dsection = soup2.find('section',attrs={'class':'css-pnw38j e1hk9ate0'})
        defnition = dsection.find('div').text
        return {"Definition":defnition}
    else:
        print(f'no result found for {word}') 

if __name__ == "__main__":
    word = input("Enter the word to search: ")
    print("""Enter
    1 - To search synonym of the word
    2 - TO search Definition of the word""")
    choice = input("Enter the your choice: ")
    if choice == '1':
        syn_list = []
        url1 = f'https://www.thesaurus.com/browse/{word}?s=t'     
        bsoup1 = get_soup(url1)
        syn_list = find_synonyms(word,bsoup1)
        df1 = pd.DataFrame(syn_list)
        df1.to_csv(f'Synonyms_of_{word}.csv')
        print(f'Synonyms of {word} are scraped and saved')
    else:
        defn_list = []
        url2 = f'https://www.dictionary.com/browse/{word}?s=t'
        bsoup2 = get_soup(url2)
        defn = find_def(word,bsoup2)
        defn_list.append(defn)
        df2 = pd.DataFrame(defn_list)
        df2.to_csv(f'Definition_of_{word}.csv')
        print(f'Definition od {word} is scraped and saved')
