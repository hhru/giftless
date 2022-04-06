"""Entry point module for WSGI

This is used when running the app using a WSGI server such as uWSGI
"""
from .app import init_app
from .version import version

app = init_app()


@app.route('/status')
def status():
    return 'ok'


@app.route('/version')
def get_version():
    return version
