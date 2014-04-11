from flask import Flask
import os
import yaml

app = Flask(__name__)
app.secret_key = 'SUPERSECRET' # you should change this to something equally random
app.config['CONFIG_FILE'] = os.path.abspath('app/config.yaml')
configStr = open(app.config['CONFIG_FILE'], 'r')
app.config['CONFIG'] = yaml.load(configStr)


from views import elastatus as elastatus
app.register_blueprint(elastatus)
