'''
První Hello Docker World aplikace ve Flasku s logováním.
'''
from logging.config import dictConfig
import logging
from flask import Flask

app = Flask(__name__)
LOG_CNF = ({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'filename': './logs/logs.txt',
            'formatter': 'default',
            'level': 'INFO',
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})


dictConfig(LOG_CNF)
logger = logging.getLogger('app')
logger.info('Flask app started')


@app.route("/")
def hello_world():
    '''
    Funkce pro zobrazení Hello World
    '''
    logger.info('Hello World endpoint was accessed')
    return "Hello Docker World"


if __name__ == "__main__":
    app.run()
