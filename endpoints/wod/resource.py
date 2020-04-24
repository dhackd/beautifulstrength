from flask import Flask
from flask_restful import Resource, Api
from bs4 import BeautifulSoup

import re
import requests, jsonify

class getWod(Resource):
    def get(self,yymmdd):
        webpage = requests.get('https://teddygym.com/wod/tdg-'+yymmdd)
        html = webpage.text
        new_html = re.sub('<br>','\n',html)
        soup = BeautifulSoup(new_html,'html.parser')

        contents = soup.find_all('div',{'class':'sqs-block-content'})
        x = contents[1]
        p = x.find_all('p')
        res = list()
        for x in p:
            res.append(x.string)
            res.append('\n')

        c = ''.join(res)
        self.body = c
        self.status_code = 200
        return {'status_code':self.status_code, 'WOD':self.body}