import matplotlib.pyplot as plt
import pandas as pd
from typing import Any

from src import SQL_Executor, SQL_Queries


class Helper:
    def __init__(self):
        self.df = pd.DataFrame()
        self.executor = SQL_Executor()
        self.query = SQL_Queries()

    def visualize(self, **kwargs: Any) -> None:
        ax = self.df
        v_df = self.df
        if "index" in kwargs:
            v_df = v_df.set_index(kwargs["index"])

        v_df[kwargs["column"]].plot(
            kind=kwargs["kind"],
            ylim=kwargs.get("ylim"),
            title=kwargs.get("title"),
            secondary_y=kwargs.get("secondary_y"),
        )

        if "rotation" in kwargs:
            plt.xticks(rotation=kwargs["rotation"])
        if "xlabel" in kwargs:
            plt.xlabel(kwargs["xlabel"])
        if "ylabel" in kwargs:
            plt.ylabel(kwargs["ylabel"])
        if "legend" in kwargs:
            plt.legend(kwargs["legend"])
