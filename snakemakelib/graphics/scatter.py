'''scatter plots with bokeh

Author: Per Unneberg
Created: Fri Oct 30 09:56:20 2015

'''

import pandas as pd
from bokeh.models import ColumnDataSource, GlyphRenderer
from bokeh.models.axes import LinearAxis, LogAxis
from . import utils
from .color import colorbrewer
import logging

logger = logging.getLogger(__name__)

__all__ = ['scatter']



def scatter(x, y, df, return_source=False, marker='circle', **kwargs):
    # setup figure
    kwfig = utils.fig_args(kwargs)
    fig = utils.create_bokeh_fig(plot_height=kwargs.pop('plot_height', None),
                                 plot_width=kwargs.pop('plot_width', None),
                                 **kwfig)
    fig_props = set(fig.properties())
    kwfig = utils.fig_args(kwargs, fig_props)
    fig.set(**kwfig)

    # Check color argument
    color=kwargs.pop("color", "blue")
    size=kwargs.pop("size", 8)
    
    # create data source and scatter
    source = ColumnDataSource(df)
    if color in source.column_names:
        colors = colorbrewer(datalen=len(list(set(source.data[color]))))
        colormap = {k:v for k,v in zip(sorted(set(source.data[color])), colors)}
        color = [colormap[i] for i in source.data[color]]
    if size in source.column_names:
        size = source.data[size]

    fig.scatter(x=x, y=y, source=source,
                marker=kwargs.pop('marker', 'circle'),
                size=size, color=color, **kwargs)

    if return_source:
        return fig, source
    else:
        return fig, None
