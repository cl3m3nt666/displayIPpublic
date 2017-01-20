import bottle
from bottle import get, static_file
import requests
import json


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="css/")

@get("/js/<filepath:re:.*\.js>")
def css(filepath):
    return static_file(filepath, root="js/")

@bottle.route("/")
@bottle.view("ipinfo.tpl")
def index() :
    info = requests.get('http://ipinfo.io/')
    j = json.loads(info.text)
    return { "title":"IP informations", "ip" : j['ip'], "country" : j['country']}

bottle.run(bottle.app(), host='0.0.0.0', port=80, debug= True, reloader=True)
