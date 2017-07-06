import random
import string
import os
import cherrypy


class calculadora(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="soma">
              <input type="text" name="operador1" />
              +
              <input type="text" name="operador2" />
              <button type="submit">Soma tetsyutsytuys</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def soma(self, operador1=3, operador2=3):
        resultado =  str((int(operador1) + int(operador2)))
        cherrypy.session['resultado'] = resultado
        return resultado

    @cherrypy.expose
    def display(self):
        return cherrypy.session['resultado']


if __name__ == '__main__':
    conf = {
        'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': int(os.environ.get('PORT', 8080)),
        },
        '/': {
            'tools.sessions.on': True
        }
    }
    cherrypy.quickstart(calculadora(), '/', conf)