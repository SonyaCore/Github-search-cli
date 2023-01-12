################################
import time

################################
class TimeerError(Exception):
    pass


################################


class Timer:
    def __init__(self) -> None:
        self.start_time = None
        self.elapsed_time = None

    def start(self):
        if self.start_time is not None:
            raise TimeerError("Timer is running.")

        self.start_time = time.perf_counter()

    def stop(self):
        if self.start_time == None:
            raise TimeerError

        self.elapsed_time = time.perf_counter() - self.start_time
        self.start_time = None
        print("Elapsed time : {time:0.4f}".format(time=self.elapsed_time))
