

class PluginSpec:
    name: str = ''

    def __init__(self):
        if not self.name:
            self.name = self.__class__.__name__