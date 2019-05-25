from flask import Flask, render_template
import requests

hackdash = "https://hackdash.org/projects/5ce8f714002e766ac0f23602"

app = Flask(__name__, static_url_path='', static_folder="static")


@app.route('/')
def index():
    return render_template("index.html")


# def factors(num):
#   return [x for x in range(1, num+1) if num%x==0]
#
#
# @app.route('/factors/<int:num>')
# def factors_route(num):
#     return "The factors of {} are {}".format(num, factors(num))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
