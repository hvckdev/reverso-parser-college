import requests
from bs4 import BeautifulSoup
from yaspin import yaspin


@yaspin(text="Parsing website..")
def getAllPageWith(word):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) '
                      'Version/15.3 Safari/605.1.15 '
    }

    return requests.get('https://context.reverso.net/перевод/английский-русский/' + word, headers=headers).text


word_to_translate = str(input('Please write the word that u want translate to Russian language: '))
html_page = getAllPageWith(word_to_translate)
soup = BeautifulSoup(html_page, 'html.parser')

translations = soup.find('div', attrs={'id': 'translations-content'}).findAll(class_='translation')
examples = soup.find('section', attrs={'id': 'examples-content'}).findAll('div', class_='example')

print('\n\nTranslations: ')
for i in range(0, 3):
    print(
        translations[i].text.strip()
    , end=' ')


print('\n\nExamples: ')
for i in range(0, 3):
    print(
        examples[i].find('div', class_='src ltr').text.strip() +
        ' - ' +
        examples[i].find('div', class_='trg ltr').text.strip()
    )
