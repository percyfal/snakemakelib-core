'''

Author: Per Unneberg
Created: Tue Dec  1 08:56:58 2015

'''
import pandas.core.common as com
from bokeh.models import ColumnDataSource
from . import utils
from .color import colorbrewer
from snakemakelib.log import LoggerManager
from .axes import xaxis, yaxis

smllogger = LoggerManager().getLogger(__name__)

__all__ = ['dotplot', 'lines', 'points']



def dotplot(x, y, df, return_source=False, marker='circle',
            **kwargs):
    # setup figure
    fig = utils.create_bokeh_fig_set_props(plot_height=kwargs.pop('plot_height', None),
                                           plot_width=kwargs.pop('plot_width', None),
                                           **kwargs)
    xaxis(fig, **kwargs)
    yaxis(fig, **kwargs)
    color = kwargs.get('color', None)
    source = utils.df_to_source(df)
    if com.is_numeric_dtype(source.to_df()[x]) == True:
        raise TypeError("{}: dependant variable must not be numerical type".format(__name__))
    if isinstance(y, list):
        color = [None] * len(y)
        if 'color' in kwargs:
            if isinstance(kwargs['color'], list) and len(kwargs['color']) == len(y):
                color = kwargs['color']
            else:
                color = [kwargs['color']] * len(y)
        for yy, c in zip(y, color):
            if not c is None:
                kwargs['color'] = c
            fig = utils.add_glyph(fig, x, yy, source, marker, **kwargs)
    else:
        fig = utils.add_glyph(fig, x, y, source, marker, **kwargs)
    return fig


def points(x, y, df, return_source=False, marker='circle',
           **kwargs):
    """Add points to a figure.

    Args:
      x (str): x column name

    """
    # setup figure
    fig = utils.create_bokeh_fig_set_props(plot_height=kwargs.pop('plot_height', None),
                                           plot_width=kwargs.pop('plot_width', None),
                                           fig=kwargs.pop('fig', None),
                                           **kwargs)
    xaxis(fig, **kwargs)
    yaxis(fig, **kwargs)

    source = utils.df_to_source(df)
    fig = utils.add_glyph(fig, x, y, source, marker, **kwargs)
    return fig
    

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
                kwargs['legend'] = str(name)
            if 'color' in kwargs:
                kwargs['color'] = color
            fig.line(x=x, y=y, source=source, **kwargs)
    return fig
