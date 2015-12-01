'''

Author: Per Unneberg
Created: Tue Dec  1 08:59:21 2015

NOTE: the functions in this module allow for plotting of multiple
columns of a data frame. If ggplot conventions are to be followed, the
data frame should first be stacked. I keep these here for now as I'm
uncertain what is the best way forward.

'''

from bokeh.models import ColumnDataSource
from snakemakelib.graphics.geom import lines
from snakemakelib.log import LoggerManager

smllogger = LoggerManager.getLogger(__name__)

__all__ = ['mlines']


def mlines(fig, x, y, df, **kwargs):
    """mlines: add lines to a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str): string for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      color (bool): set color
      legend (bool): set legend
      kwargs: keyword arguments to pass to fig.line

    Example:

      .. bokeh-plot::
          :source-position: above

          import pandas as pd
          from bokeh.plotting import figure, show, hplot
          from snakemakelib.graphics import mlines

          df = pd.DataFrame([[1,2,4], [2,5,2], [3,9,12]], columns=["x", "y", "foo"])

          f = figure(title="Line plot", plot_width=400, plot_height=400)
          mlines(f, "x", ["y", "foo"], df, color=["red", "blue"], legend=["y", "foo"])

          show(f)

    """
    smllogger.debug("Adding points to figure {}".format(fig))
    color = kwargs.pop('color') if 'color' in kwargs else [None] * len(y)
    legend = kwargs.pop('legend') if 'legend' in kwargs else [None] * len(y)
    source = ColumnDataSource(df)
    for yy, c, l in zip(y, color, legend):
        kw = kwargs
        kw['color'] = c
        kw['legend'] = l
        lines(fig=fig, x=x, y=yy, df=df, **kwargs)
    return fig
    
