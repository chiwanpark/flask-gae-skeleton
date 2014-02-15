# -*- coding: utf-8 -*-
from flask import Flask
from importlib import import_module
import os
import logging


def create_app():
    current_path = get_current_path()
    client_path = os.path.join(current_path, '..', 'client')

    app = Flask(__name__, template_folder=client_path, static_folder=client_path)
    logging.info('Flask application object is created.')

    modules = get_modules()
    register_blueprints(app, modules)

    return app


def register_blueprints(app, modules):
    for module_name in modules:
        try:
            module = import_module('server.%s' % module_name)
            app.register_blueprint(module.bp)

            logging.info('Module named %s is loaded.' % module_name)
        except ImportError as ex:
            logging.error('Could not load module named: %s | %s' % (module_name, ex))

    logging.info('Blueprints are registered.')


def get_modules():
    current_path = get_current_path()
    return [d for d in os.listdir(current_path) if os.path.isdir(os.path.join(current_path, d))]


def get_current_path():
    return os.path.dirname(os.path.abspath(__file__))
