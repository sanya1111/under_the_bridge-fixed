from jinja2 import Environment, PackageLoader, BytecodeCache
import os.path, pkgutil
class JinContext(object):
    def __init__(self, package, folder):
        self.env = Environment(loader=PackageLoader(package, folder))
    def put_to_globals(self, name, what):
        self.env.globals[name] = what
    def load(self, module):
        for current in dir(module):
            if not current.startswith('__'):
                print(current)
                self.put_to_globals(current, getattr(module, current))

