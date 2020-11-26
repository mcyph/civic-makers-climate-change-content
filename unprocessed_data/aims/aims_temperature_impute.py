# TODO: Use https://datascienceplus.com/knnimputer-for-missing-value-imputation-in-python-using-scikit-learn/ to impute missing values!
import pandas as pd
from pathlib import Path
from os.path import realpath
from sklearn.impute import KNNImputer


base_path = Path(realpath(__file__)).parent / 'data_json_api' / 'tempdata_csv'

MODE_MAX = 0
MODE_MIN = 1
MODE_MEDIAN = 2
MODE_MEAN = 3

FROM_CUTOFF = "1992/12/17"
TO_CUTOFF = "2020/04/6"


def get_imputed(from_depth=0, to_depth=2, mode=MODE_MEAN):
    out = pd.DataFrame(index=pd.DatetimeIndex(pd.date_range(FROM_CUTOFF, TO_CUTOFF)))
    print("OUT:", out)

    for json_path in base_path.glob('*.csv'):
        print(json_path)
        with open(json_path, 'r') as f:
            df = pd.read_csv(f)

        df = df[(df.depth >= from_depth) & (df.depth <= to_depth)]
        df.index = pd.to_datetime(df['time'])

        df = df.drop(columns=['depth'])
        df = df.drop(columns=['time'])

        if df.empty:
            continue
        elif mode == MODE_MAX:
            df = df.groupby(pd.Grouper(freq='D')).max()
        elif mode == MODE_MIN:
            df = df.groupby(pd.Grouper(freq='D')).max()
        elif mode == MODE_MEDIAN:
            df = df.groupby(pd.Grouper(freq='D')).median()
        elif mode == MODE_MEAN:
            df = df.groupby(pd.Grouper(freq='D')).mean()
        else:
            raise Exception(mode)

        df = df.rename(columns={'value': json_path.name.replace('.csv', '')})
        out = pd.merge(out, df, left_index=True, right_index=True, how='outer')
        print(out)

    imputer = KNNImputer()
    out = pd.DataFrame(imputer.fit_transform(out),
                       columns=out.columns,
                       index=out.index)
    return out


if __name__ == '__main__':
    df = get_imputed()
    df.to_csv('out_imputed.csv')

    # Group by mid year so as to capture summer
    df = df.groupby(pd.Grouper(freq=pd.tseries.offsets.BYearEnd(month=6))).mean()
    # Cut off 2 years where there's incomplete data
    df = df.iloc[1:-1]
    # Average over 5 years
    df = df.rolling(window=5).mean()
    # Add the average over all weather stations
    df['mean'] = df.mean(axis=1)
    df.to_csv('out_imputed_average.csv')
