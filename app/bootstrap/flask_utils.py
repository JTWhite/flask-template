import os
import importlib
from flask import Flask, Blueprint

class FlaskUtils:
    @staticmethod
    def is_dunder(name: str) -> bool:
        return name.startswith('__') and name.endswith('__')

    @staticmethod
    def is_view(name: str) -> bool:
        return any(name.endswith(v) for v in ["views", "view"])
    
    @classmethod
    def register_blueprints(cls, app: Flask) -> None:
        for path, _, _ in os.walk(os.path.join(app.root_path)):
            if cls.is_view(path):
                module_path = '.'.join(path[len(os.getcwd())+1:].split('/'))
                cls._register_module_blueprints(module_path, app)
    
    @staticmethod
    def _register_module_blueprints(module_path: str, app: Flask) -> None:
        
        module = importlib.import_module(module_path)
        for _, blueprint in module.__dict__.items():
            if isinstance(blueprint, Blueprint):
                importlib.import_module(module_path)
                app.register_blueprint(blueprint)
