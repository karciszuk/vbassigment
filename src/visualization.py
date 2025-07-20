import matplotlib.pyplot as plt
import pandas as pd


class Vizualizator:
    def __init__(self, df):
        self.df = df

    def _create_labels(self, bins_inc):
        labels = []
        bins = bins_inc + [float("inf")]
        for i in range(len(bins) - 1):
            if bins[i + 1] == float("inf"):
                label = f"{bins[i]}+"
            else:
                label = f"{bins[i]}-{bins[i + 1] - 1}"
            labels.append(label)
        return labels

    def group_by_column(self, bins, target_column, column, drop_column=None):
        if drop_column:
            self.df = self.df.copy().drop(columns=drop_column)

        labels = self._create_labels(bins)

        group_column = f"group_{column}"
        self.df[group_column] = pd.cut(self.df[column], bins=bins, labels=labels)

        output_column = f"{target_column}_rate"
        self.df = self.df.groupby(group_column, observed=True).agg(
            **{output_column: (target_column, lambda x: (x.mean() * 100).round(2))}
        )

        return self

    def visualize(self, **kwargs):
        v_df = self.df
        if "index" in kwargs:
            v_df = v_df.set_index(kwargs["index"])

        v_df[kwargs["column"]].plot(
            kind=kwargs["kind"], ylim=kwargs.get("ylim"), title=kwargs.get("title")
        )

        if "rotation" in kwargs:
            plt.xticks(rotation=kwargs["rotation"])
        if "xlabel" in kwargs:
            plt.xlabel(kwargs["xlabel"])
        if "ylabel" in kwargs:
            plt.ylabel(kwargs["ylabel"])
        if "legend" in kwargs:
            plt.legend(kwargs["legend"])


if __name__ == "__main__":
    bins = [18, 26, 36, 51]
    test = Vizualizator("df", bins)
    test._create_labels()
