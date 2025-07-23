import pandas as pd


def smart_format(x: int, pos) -> str:
    if x >= 1000000:
        return f"{x / 1000000:.1f}M"
    elif x >= 1000:
        return f"{x / 1000:.0f}k"
    else:
        return f"{x:.0f}"


def create_labels(bins_inc: list[int]) -> tuple[list[str], list[str]]:
    labels = []
    bins = bins_inc + [float("inf")]
    for i in range(len(bins) - 1):
        if bins[i + 1] == float("inf"):
            label = f"{bins[i]}+"
        else:
            label = f"{bins[i]}-{bins[i + 1] - 1}"
        labels.append(label)
    return bins, labels


def group_by_column(
    df: pd.DataFrame,
    bins_inc: list[str],
    target_column: str,
    column: str,
    drop_column: str = None,
) -> pd.DataFrame:
    bins, labels = create_labels(bins_inc)

    if drop_column:
        df = df.drop(columns=drop_column)

    group_column = f"group_{column}"
    df[group_column] = pd.cut(df[column], bins=bins, labels=labels)

    output_column = f"{target_column}_rate"
    df = df.groupby(group_column, observed=True).agg(
        **{output_column: (target_column, lambda x: (x.mean() * 100).round(2))}
    )

    return df


def dpd_calc(df: pd.DataFrame) -> pd.DataFrame:
    scheduled_date = pd.to_datetime(df["scheduled_date"])
    payment_date = pd.to_datetime(df["payment_date"])
    today = pd.Timestamp.today()

    df["dpd"] = 0

    df.loc[payment_date > scheduled_date, "dpd"] = (
        payment_date - scheduled_date
    ).dt.days

    df.loc[payment_date.isna(), "dpd"] = (today - scheduled_date).dt.days.clip(lower=0)

    df = df.drop(columns=["payment_date", "scheduled_date"])

    return df
