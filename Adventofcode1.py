import pandas as pd

# Path
chemin = "/Users/alexandretranie/Downloads/input.csv"
df = pd.read_csv(chemin, header=None, sep=None, engine='python')


def compute_distance(df):
    # Sort the column
    df[0] = df[0].sort_values().reset_index(drop=True)
    df[1] = df[1].sort_values().reset_index(drop=True)

    # Compute the distance
    distances = abs(df[1] - df[0])

    return distances.sum()



def compute_distance2(df):
    # Sort the column
    df[0] = df[0].sort_values().reset_index(drop=True)
    df[1] = df[1].sort_values().reset_index(drop=True)
    map_list = df[1].value_counts()
    return df[0].mul(df[0].map(map_list), axis=0).sum()




if __name__ ==  '__main__':
    distance = compute_distance(df)
    sum = compute_distance2(df)
    print(df.head())
    print(distance)
    print(sum)