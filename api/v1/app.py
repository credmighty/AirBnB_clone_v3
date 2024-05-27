
import storage from models
import app_views from api.v1.views
from flask import Flask

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_dataB():
   """close storage"""
   storage.close()

if __name__ == "__main__":
   """main function"""
   host = environ.get('HBNB_API_HOST')
   port = environ.get('HBNB_API_PORT')
   if not host:
       host = 0.0.0.0
   if not port:
       port = '5000'
   app.run(host=host, port=port, threaded=True)
