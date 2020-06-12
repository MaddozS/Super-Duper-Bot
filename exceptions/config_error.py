class ConfigurationError(Exception):
    def __init__(self, environ):
        self.environ = environ
        self.message = f"The given environment ({environ}) isn't a valid"
        
        super().__init__(self.message)
        