import pandas as pd
from unprocessed_data.climatewatch.get_aggregate_ghgs import get_lulucf
from unprocessed_data.gapminder.get_world_population import get_world_population


def get_ghgs_by_population():
    lulucf = get_lulucf()
    population = get_world_population()
    df = pd.merge(lulucf.add_suffix('_ghg'),
                  population.add_suffix('_pop'),
                  left_index=True, right_index=True)
    print("MERGED:", df)

    for col in df:
        if '_ghg' in col and not 'source' in col:
            df['%s_ratio' % col.replace('_ghg', '')] = df[col] / df['%s_pop' % col.replace('_ghg', '')]

    print('GHG:', df['2017_ghg'])
    print('POP:', df['2017_pop'])
    print('RATIO:', df['2017_ratio'])
    df.to_csv('out.csv')
    return df


if __name__ == '__main__':
    get_ghgs_by_population()
    #print()




