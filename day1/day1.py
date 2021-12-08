import pandas as pd


def raw_measurements():
    path_to_file = "C:/tfs/advent2022/day1/input.txt"
    with open(path_to_file) as f:
        lines = f.readlines()

    ints = [int(item) for item in lines]

    df = pd.DataFrame(data=ints, columns=["depth_measurement"])
    return df


def find_increases(df):
    frame = df.assign(
        diff=(
            df["depth_measurement"]
            .rolling(window=2)
            .apply(lambda df: df.iloc[1] - df.iloc[0])
        )
    )
    return frame.assign(increase=(frame["diff"] > 0))


def count_increases():
    df = find_increases(raw_measurements())
    return df.increase.sum()


def sliding_sum_count_increases():
    df = raw_measurements()
    sum_df = pd.DataFrame(
        data=df["depth_measurement"].rolling(window=3).sum().shift(-2),
        columns=["depth_measurement"],
    )
    diff_df = find_increases(sum_df)
    return diff_df.increase.sum()


print({"part 1": count_increases(), "part 2": sliding_sum_count_increases()})
