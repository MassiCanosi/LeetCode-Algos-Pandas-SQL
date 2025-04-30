import pandas as pd

def big_countries(world: pd.DataFrame, population_thold: int = 25000000, area_thold: int = 3000000) -> pd.DataFrame:
    filtered = world[(world['area'] >= area_thold) | (world['population'] >= population_thold)]
    cols = ['name', 'population', 'area']
    return filtered[cols]
    