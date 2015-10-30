'''scatter plots with bokeh

Author: Per Unneberg
Created: Fri Oct 30 09:56:20 2015

'''

from bokeh.models import ColumnDataSource
from . import utils

__all__ = ['scatter']


def scatter(x, y, df, return_source=False, **kwargs):
    # setup figure
    fig = utils.create_bokeh_fig(plot_height=kwargs.pop('plot_height', None),
                                 plot_width=kwargs.pop('plot_width', None))
    fig_props = set(fig.properties())
    kwfig = {k: v for k, v in kwargs.items() if k in fig_props}
    fig.set(**kwfig)

    # create data source
    source = ColumnDataSource(df)
    fig.circle(x=x, y=y, source=source)
    print(fig.renderers)
    print(dir(fig))
    
    #glyph_props = set(fig.circle.properties)
    #print(glyph_props)
    #, *kwglyph)

def points(fig):
    """Add points to current figure"""
    pass
