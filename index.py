import os
import random
import string

import cherrypy

from Calculadora import Calculadora


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
              <button type="submit">Soma</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def soma(self, operador1=3, operador2=3):
        calculadora = Calculadora()
        resultado = calculadora.soma(int(operador1), int(operador2))
        resutadoString = str(resultado)

        cherrypy.session['resultado'] = resutadoString
        return resutadoString

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
