from flask import Flask, render_template
import requests
import json
import os

hackdash = "https://hackdash.org/projects/5ce8f714002e766ac0f23602"
api_url = "https://api.jhcgn19.nwng.eu/getProduct"

application = Flask(__name__, static_url_path='', static_folder="static")


def url_for_static(filename):
    root = application.config.get('STATIC_ROOT', '')
    return os.path.join(root, filename)


@application.route('/')
def index():
    return render_template("index.html")


@application.route('/barcode')
def no_barcode(barcode):
    print(barcode)
    return "Da fehlt ein Barcode!"


@application.route('/barcode/<int:barcode>')
def barcode(barcode):

    headers = {"Content-Type": "application/json"}

    print(barcode)
    root = application.config.get('STATIC_ROOT', '')

    api_data = requests.post(api_url, data=json.dumps({"code": str(barcode), "origin": "de"}), headers=headers)

    print(api_data.text)

    return render_template("product.html", product=api_data.json(), root=root)


# def factors(num):
#   return [x for x in range(1, num+1) if num%x==0]
#
#
# @app.route('/factors/<int:num>')
# def factors_route(num):
#     return "The factors of {} are {}".format(num, factors(num))


if __name__ == '__main__':
    application.run(host='0.0.0.0')
