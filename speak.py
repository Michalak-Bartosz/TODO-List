import threading


class Threader(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(Threader, self).__init__(*args, **kwargs)

    def run(self):
        self._args[1].say(self._args[0])
        try:
            self._args[1].runAndWait()
        except RuntimeError:
            return
