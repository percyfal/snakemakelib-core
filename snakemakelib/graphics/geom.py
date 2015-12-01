'''

Author: Per Unneberg
Created: Tue Dec  1 08:56:58 2015

'''
from bokeh.models import ColumnDataSource
from .color import colorbrewer
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

__all__ = ['lines']

def lines(fig, x, y, df, groups=None, **kwargs):
    """lines: add lines to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      source (:py:class:`~bokeh.models.ColumnDataSource`): bokeh ColumnDataSource object
      groups (str, list(str)): string or list of strings for columns to group by
      kwargs: keyword arguments to pass to fig.line

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from snakemakelib.graphics import lines

          df = pd.DataFrame([[1,2], [2,5], [3,9]], columns=["x", "y"])

          f = figure(title="Line plot", plot_width=400, plot_height=400)
          lines(f, "x", "y", df, legend="y")
          lines(f, "x", "x", df, legend="x", color="red")

          show(f)

    """
    smllogger.debug("Adding points to figure {}".format(fig))
    if groups is None:
        source = ColumnDataSource(df)
        fig.line(x=x, y=y, source=source, **kwargs)
    else:
        try:
            grouped = df.groupby(groups)
        except:
            raise
        colors = colorbrewer(datalen=len(grouped.groups.keys()))
        for k, color in zip(grouped.groups.keys(), colors):
            name = k
            group = grouped.get_group(name)
            source = ColumnDataSource(group)
            if 'legend' in kwargs:
                kwargs['legend'] = name
            if 'color' in kwargs:
                kwargs['color'] = color
            fig.line(x=x, y=y, source=source, **kwargs)
    return fig
