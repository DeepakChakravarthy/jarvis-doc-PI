import json
from flask import Flask
from flask import request
from flask import jsonify
import re
import os
from commonregex import CommonRegex

app = Flask(__name__)
@app.route('/pii',methods=['GET','POST'])
def endpoint2():
    req = request.get_json()
    list1 = []
    list1.append({'html':req['article-content']})
    i = ', '.join(strings['html'] for strings in list1)
    print(i)
    print(type(i))
    print("Preprocess works")
    clean = re.compile('<.*?>')
    re.sub(clean, '', i)
    parsed_text = CommonRegex(i)
    PII = {}
    PII['PhoneNumber'] = parsed_text.phones
    PII['CreditCardNumber'] = parsed_text.credit_cards
    PII['Email'] = parsed_text.emails
    regex = "(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}"
    p = re.compile(regex)
    SSN = re.findall(p, i)
    PII['SSN'] = SSN
    y = json.dumps(PII)
    return y


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000,debug=True)
