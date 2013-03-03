#!/Applications/MNPP/Library/python26/bin/python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return "Hello World from flask!"

#def application(environ, start_response):
#  return app(environ, start_response)


#if __name__ == '__main__':
#    app.run()
