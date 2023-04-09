from typing import Iterable, Optional
from typing_extensions import Self

import circlify
from matplotlib import cm, colors, patches
import matplotlib.pyplot as plt

from truelearn.models import Knowledge
from truelearn.utils.visualisations._base import MatplotlibBasePlotter


class BubblePlotter(MatplotlibBasePlotter):
    """Bubble Plotter.

    Visualise the learner's knowledge in terms of bubble.
    Each subject is represented by a bubble in the chart.
    The diameter of the circle is proportional to the mean of the subject,
    and the shade of the circle represents the variance of the subject.
    """

    def __init__(
        self,
        title: str = "Comparison of learner's subjects",
        xlabel: str = "",
        ylabel: str = "",
    ):
        """Init a Bubble plotter.

        Args:
            title: the default title of the visualization
            xlabel: the default x label of the visualization
            ylabel: the default y label of the visualization
        """
        super().__init__(title, xlabel, ylabel)

    # pylint: disable=too-many-locals
    def plot(
        self,
        content: Knowledge,
        topics: Optional[Iterable[str]] = None,
        top_n: Optional[int] = None,
    ) -> Self:
        """Plot the graph based on the given data.

        Args:
            content:
                The Knowledge object to use to plot the visualisation.
            topics:
                The list of topics in the learner's knowledge to visualise.
                If None, all topics are visualised (unless top_n is
                specified, see below).
            top_n:
                The number of topics to visualise. E.g. if top_n is 5, then the
                top 5 topics ranked by mean will be visualised.
        """
        content_dict, _ = self._standardise_data(content, False, topics)[:top_n]

        means, variances, titles = list(zip(*content_dict))
        circles = circlify.circlify(
            means, show_enclosure=True, target_enclosure=circlify.Circle(x=0, y=0, r=1)
        )

        self.ax.axis("off")

        # set limit for x and y axis
        lim = max(
            max(
                abs(circle.x) + circle.r,
                abs(circle.y) + circle.r,
            )
            for circle in circles
        )
        plt.xlim(-lim, lim)
        plt.ylim(-lim, lim)

        cmap = cm.get_cmap("Greens_r")

        # Normalize data range to colormap range
        norm = colors.Normalize(vmin=min(variances) - 0.05, vmax=max(variances) + 0.05)

        sm = cm.ScalarMappable(norm=norm, cmap=cmap)

        for i, circle in enumerate(circles):
            if i < len(titles):
                x, y, r = circle
                self.ax.add_patch(
                    patches.Circle(
                        (x, y),
                        r,
                        linewidth=2,
                        color=sm.to_rgba(variances[len(variances) - 1 - i]),
                    )
                )
                plt.annotate(
                    titles[len(titles) - 1 - i], (x, y), va="center", ha="center"
                )

        # setup the colorbar on the right
        cbar = self.fig.colorbar(sm, ax=self.ax)
        cbar.ax.set_ylabel("Variance")

        return self
