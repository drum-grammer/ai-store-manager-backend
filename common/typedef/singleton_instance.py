class Singleton:
    """
    Classes that require the Singleton pattern should inherit from this class.
    """
    _instance = None

    @classmethod
    def instance(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
        return cls._instance
