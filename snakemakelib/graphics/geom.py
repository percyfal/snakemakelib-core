'''

Author: Per Unneberg
Created: Tue Dec  1 08:56:58 2015

'''
import pandas.core.common as com
from bokeh.models import ColumnDataSource
from . import utils
from .color import colorbrewer
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

__all__ = ['dotplot', 'lines']



def dotplot(x, y, df, return_source=False, marker='circle',
            **kwargs):
    # setup figure
    kwfig = utils.fig_args(kwargs)
    fig = utils.create_bokeh_fig(plot_height=kwargs.pop('plot_height', None),
                                 plot_width=kwargs.pop('plot_width', None),
                                 **kwfig)
    fig_props = set(fig.properties())
    kwfig = utils.fig_args(kwargs, fig_props)
    fig.set(**kwfig)
    source = utils.df_to_source(df)
    if com.is_numeric_dtype(source.to_df()[x]) == True:
        raise TypeError("{}: dependant variable must not be numerical type".format(__name__))
    fig.circle(x=x, y=y, source=source, **kwargs)
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
