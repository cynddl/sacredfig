from re import A
import matplotlib.pyplot as plt
import numpy as np
import pytest

import sacredfig

from sacredfig import add_labels_to_axes
from sacredfig import cm2in


@pytest.mark.mpl_image_compare
def test_plot_with_panels():
    with plt.style.context(sacredfig.style):
        fig, axes = plt.subplots(1, 2, figsize=(12 * cm2in, 6 * cm2in), dpi=150)

        # Panel A
        x = np.linspace(0, 5, 501)
        y = x * np.sin(x * np.pi)
        z = -(x + 0.5) * np.sin((x + 0.5) * np.pi)
        axes[0].plot(x, y)
        axes[0].plot(x, z, alpha=0.5)
        axes[0].fill_between(
            x,
            y,
            z,
            where=y > z,
            facecolor="#eeeeee",
        )
        axes[0].set(
            xlim=(0, 5), ylim=(-6, 6), xlabel="Time $t$", ylabel="Perturbations ($Y_t$, $Z_t$)"
        )
        axes[0].grid(False, which="major", axis="x")

        # Panel B
        axes[1].plot(y, z, c="k")
        axes[1].set(
            xlim=(-6, 6),
            ylim=(-6, 6),
            xlabel="Y-axis perturbation ($Y_t$)",
            ylabel="Z-axis perturbation ($Z_t$)",
        )

        # Ensure each panel is a perfect square
        for ax in axes:
            ax.set_box_aspect(1)

        # Adjust space between subplots
        fig.subplots_adjust(wspace=0.3)

        # Add labels a. and b.
        add_labels_to_axes(fig, axes)

        return fig


@pytest.mark.mpl_image_compare
def test_plot_boxplot():
    import seaborn as sns
    sns.reset_orig()

    iris = sns.load_dataset("iris")

    with plt.style.context(sacredfig.style):

        fig, ax = plt.subplots(figsize=(6 * cm2in, 6 * cm2in), dpi=150)
        ax.grid(False, which='major', axis='x')

        ax.boxplot([iris.sepal_length.values, iris.sepal_width.values],
                labels=['Sepal length', 'Sepal width'])

        ax.set_box_aspect(1)
        ax.set(xlabel="Attribute", ylabel="Empirical distribution", ylim=(0, 10));

        return fig
