import random
import numpy as np
from math import floor
from datetime import datetime

class Ticker(object):
    TIMESTAMP,OPEN, HIGH, LOW, CLOSE, VOLUME = range(6)
    def __init__(self, filename):
        self.data = np.loadtxt(
            f'ticker_data/{filename}.csv',
            delimiter=',',
            dtype=object,
            usecols=(0, 2, 3, 4, 5, 7),
            skiprows=1,
            converters={
                0: lambda x: datetime.strptime(x.decode("utf-8"), "%Y-%m-%d %H:%M:%S+00:00"),
                2: lambda x: float(x) if x else float(0),
                3: lambda x: float(x) if x else float(0),
                4: lambda x: float(x) if x else float(0),
                5: lambda x: float(x) if x else float(0),
                7: lambda x: int(x) if x else int(0),
            }
        )
        self.col = None
        self.rows, self.cols = self.data.shape

    def set_interested_col(self, col_name):
        self.col = getattr(self, col_name)

    def get_values(self):
        return self.data[:, self.col]

    def sample(self, size):
        max_index = self.rows - size
        start = np.random.randint(0, max_index)
        return TickerSample(self.slice(start, size))

    def date_slice(self, start, end):
        data = self.data[np.where(self.data[:, self.TIMESTAMP] >= start)]
        return data[np.where(data[:, self.TIMESTAMP] < end)][:, self.col]

    def slice(self, start, size):
        return self.get_values()[start:start+size]

    @staticmethod
    def sliding_windows(data_chunk, window_size, step_size):
        data = data_chunk.flatten()
        amount = floor((len(data)-window_size) / step_size) + 1
        indexer = np.arange(window_size)[None, :] + step_size * np.arange(amount)[:, None]
        windows = data[indexer]
        return windows

class TickerSample():
    def __init__(self, data):
        self.data = data

    def normalize(self):
        # TANGENT STUFF
        lowered = self.data - self.data.min()
        return lowered/lowered.max()
