# test file

import requests
import re
from bs4 import BeautifulSoup

class MainClass:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def getWOD(yymmdd):
        webpage = requests.get('https://teddygym.com/wod/tdg-'+yymmdd)
        html = webpage.text
        new_html = re.sub('<br>','\n',html)
        soup = BeautifulSoup(new_html,'html.parser')

        contents = soup.find_all('div',{'class':'sqs-block-content'})
        x = contents[1]
        p = x.find_all('p')
        res = ''
        for x in p:
            res = ' {}'.format(x.string)
            print(res)

if __name__ == "__main__":
    MainClass.getWOD('200319')
