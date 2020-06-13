import os
from exceptions.config_error import ConfigurationError

class Config():
    def __init__(self, config = os.environ["ENVIRONMENT_BOT"]):
        # print(os.environ)
        self.data = {}
        self.__setup_config(config)

    def __dev_config(self):
        self.data["google_api"]  = os.environ["GOOGLE_DEV_API"]
        self.data["google_cse"]      = os.environ["GOOGLE_CSE"]
        self.data["discord_api_key"] = os.environ["DISCORD_API_KEY_DEV"]
        self.data["command_prefix"] = "dev!"

    def __deploy_config(self):
        self.data["google_api"]  = os.environ["GOOGLE_DEPLOY_API"]
        self.data["google_cse"]      = os.environ["GOOGLE_CSE"]
        self.data["discord_api_key"] = os.environ["DISCORD_API_KEY_DEPLOY"]
        self.data["command_prefix"] = "sd!"

    def __setup_db(self):
        self.data["db_username"] = os.environ["DB_USERNAME"]
        self.data["db_name"] = os.environ["DB_NAME"]
        self.data["db_password"] = os.environ["DB_PASSWORD"]

    def __setup_config(self, environ):
        config_type = {
            "development": self.__dev_config,
            "deployment": self.__deploy_config
        }

        setup = config_type.get(environ, lambda: self.__unknown_environ(environ))
        setup()
        self.__setup_db()

    def __unknown_environ(self, environ):
        raise ConfigurationError(environ)

cfg = Config()
