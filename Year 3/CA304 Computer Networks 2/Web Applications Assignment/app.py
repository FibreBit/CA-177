from flask import Flask, redirect, url_for, request, render_template, jsonify
import csv
import json
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/formtest', methods=['GET', 'POST'])
def formtest():
    #if request is a post and client is sending info, take name as arguement to name.html
    #else, load submission page
    if request.method == 'POST':
        info = request.form
        name = info['name']
        return render_template('name.html', name=name)
    else:
        return render_template('login.html')

@app.route('/allegiances')
def all():
    data = []
    #read in csv rows and append them to list one by one
    with open('allegiance.csv', 'r') as csvFile:
        csvReader = csv.DictReader(csvFile)
        for rows in csvReader:
            data.append(rows)
    return jsonify(data)
        

@app.route('/allegiancesdashboard')
def table():
    return render_template('api.html')


if __name__ == '__main__':
   app.run()
