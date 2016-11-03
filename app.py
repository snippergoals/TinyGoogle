from flask import Flask, request, render_template
from flask.ext.bootstrap import Bootstrap
import json, sys
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
key = 'AIzaSyCieQLOf0-4RILST4Eivz7CjdOp-4cCUOE'

# print json_data['queries']['request'][0]['count']

def toJson(data):
    line = json.dumps(data)
    return line

@app.route('/')
def index():
    return render_template('index.html',name='yrq')

@app.route('/query/',methods=['GET'])
def query():
    if request.method == 'GET':

        # read engineID
        # f = file('data/engine.json')
        # s = json.load(f)
        # no = 2
        # name = 'engine_' + str(no+1)
        # cx = s['engine'][no][name]['cx']

        # combine search string
        q = request.args.get('q')

        cx = "009989704776709960942:xgqpl9qptva"
        print type(q)
        url = "https://www.googleapis.com/customsearch/v1"
        query_string = {"key":key,"cx":cx,"num":"10","q":q}
        # print "quertstring is" + query_string
        response = requests.request("GET", url, params=query_string)
        json_data = json.loads(response.text)

        # current_page = json_data['queries']['request'][0]['startIndex']/10
        # next_page = current_page+1
        # engine_name = json_data['context']['title']

        result = []
        results = []
        items = json_data['items']

        for item in items:
            result.append(item['title'])
            result.append(item['link'])
            result.append(item['displayLink'])
            result.append(item['snippet'])
            results.append(result)
            result =[]
        print results
            # print ' title:' + item['title']
        # items = json_data['item']
        # print title, link
        # return toJson(response.text)
        # return toJson(items)
        return render_template('index.html',results=results)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug = True)
