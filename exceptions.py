class WrongSpectrometerReadingError(Exception):
    def __init__(self):
        self.error = "wrong type of spectrometer reading"

    def __str__(self):
        return self.error
