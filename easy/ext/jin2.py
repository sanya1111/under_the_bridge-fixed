from jinja2 import Environment, PackageLoader, BytecodeCache

class JinContext(object):
    def __init__(self, package, folder):
        self.env = Environment(loader=PackageLoader(package, folder))
    def put_to_globals(self, name, what):
        self.env.globals[name] = what

