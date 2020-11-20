import pandas as pd
from unprocessed_data.climatewatch.get_aggregate_ghgs import get_lulucf
from unprocessed_data.gapminder.get_world_population import get_world_population


def get_ghgs_by_population():
    lulucf = get_lulucf()
    population = get_world_population()
    df = pd.merge(lulucf, population, left_index=True, right_index=True, suffixes=)

    for col in lulucf:
        if col.isdigit():
            lulucf[col] = lulucf[col].astype(float)
            df[col] = lulucf[col] / population[col]

    print(df)

    df.index = lulucf.index
    print(df)
    return df


if __name__ == '__main__':
    print(get_ghgs_by_population())




