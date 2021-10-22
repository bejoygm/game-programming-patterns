class Singleton:
    _instance = None

    @classmethod
    def instance(self):
        if not self._instance:
            self._instance = Singleton()
        return self._instance