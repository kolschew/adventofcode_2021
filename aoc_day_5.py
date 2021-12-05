import pandas as pd
import numpy as np
from collections import Counter


# Pandas surely is awesome for reading in data because of its versatility! #
file = 'input_puzzles/day_5_test.txt'
df5 = pd.read_csv(file, sep=',|->|,', header=None, engine='python', names=['x1', 'y1', 'x2', 'y2'])

# For part one, we want to use only the entries where either x1==x2 or y1==y2, which can be done with .loc #
# Also pandas keeps the indices, so it is necessary to reset them with df.reset_index (drop replaces the former ones) #
df_p1 = pd.DataFrame(df5.loc[(df5['x1'] == df5['x2']) | (df5['y1'] == df5['y2'])]).reset_index(drop=True)


def count_intersections(data):
    cnt = Counter()
    for ii in range(len(data)):
        xrange = np.linspace(data['x1'][ii], data['x2'][ii], abs(data['x1'][ii] - data['x2'][ii]) + 1)
        yrange = np.linspace(data['y1'][ii], data['y2'][ii], abs(data['y1'][ii] - data['y2'][ii]) + 1)
        if data['x1'][ii] == data['x2'][ii] or data['y1'][ii] == data['y2'][ii]:
            for xx in xrange:
                for yy in yrange:
                    cnt[(xx, yy)] += 1
        elif len(xrange) == len(yrange):
            for jj in range(len(xrange)):
                cnt[(xrange[jj], yrange[jj])] += 1
        else:
            pass
    res = len([count for _, count in cnt.items() if count > 1])
    return res
