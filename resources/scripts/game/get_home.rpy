init python -1:
    import os

    def home():
        return os.path.join(os.path.expanduser("~"), ".MonikaAfterStory")

    store.home = home