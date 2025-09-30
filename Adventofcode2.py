import pandas as pd



# Path
chemin = "/Users/alexandretranie/Downloads/input2.csv"
df = pd.read_csv(chemin, header=None, sep=None, engine='python')


def safe_report(levels, tolerance=False):
    # Remove NaN values
    clean_levels = [x for x in levels if pd.notnull(x)]
    if len(clean_levels) < 2:
        return False  # Not enough data
    diffs = [clean_levels[i+1] - clean_levels[i] for i in range(len(clean_levels)-1)]
    all_increasing = all(d > 0 for d in diffs)
    all_decreasing = all(d < 0 for d in diffs)
    if not (all_increasing or all_decreasing):
        if not tolerance:
            return False
        # Try removing one level at a time and check again
        for i in range(len(clean_levels)):
            test_levels = clean_levels[:i] + clean_levels[i+1:]
            if len(test_levels) < 2:
                continue
            test_diffs = [test_levels[j+1] - test_levels[j] for j in range(len(test_levels)-1)]
            test_increasing = all(d > 0 for d in test_diffs)
            test_decreasing = all(d < 0 for d in test_diffs)
            if test_increasing or test_decreasing:
                if all(1 <= abs(d) <= 3 for d in test_diffs):
                    return True
        return False
    if not all(1 <= abs(d) <= 3 for d in diffs):
        if not tolerance:
            return False
        # Try removing one level at a time and check again
        for i in range(len(clean_levels)):
            test_levels = clean_levels[:i] + clean_levels[i+1:]
            if len(test_levels) < 2:
                continue
            test_diffs = [test_levels[j+1] - test_levels[j] for j in range(len(test_levels)-1)]
            test_increasing = all(d > 0 for d in test_diffs)
            test_decreasing = all(d < 0 for d in test_diffs)
            if (test_increasing or test_decreasing) and all(1 <= abs(d) <= 3 for d in test_diffs):
                return True
        return False
    return True

# Apply the rule to each row (tolerance can be set to True or False)
df['safe'] = df.apply(lambda row: safe_report(row.tolist(), tolerance=True), axis=1)


if __name__ ==  '__main__':
    print(df.head(10))
    print(df.shape)
    number_safe_report = df['safe'].sum()
    print(f"Number of safe reports: {number_safe_report}")
