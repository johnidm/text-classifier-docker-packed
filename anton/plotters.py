import matplotlib.pyplot as plt
import config


def _save_label_group(df):
    ax = df.groupby("label").count().plot.bar(stacked=True,
                                              figsize=(10, 5),
                                              legend=None,
                                              cmap="viridis")

    label_sum = df["label"].count()

    for rect in ax.patches:
        height = int(rect.get_height())
        label_percentage = round(float(height/label_sum) * 100, 2)
        ypos = rect.get_y() + height/2

        ax.text(rect.get_x() + rect.get_width()/2.,
                ypos,
                f"{height}\n\n{label_percentage}%",
                ha="center",
                va="bottom",
                fontweight="bold",
                color="white")

    plt.savefig(f"{config.OUTPUT_DIR}/label_group.png")


def save_all(df):
    _save_label_group(df)
