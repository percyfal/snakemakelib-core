'''scatter plots with bokeh

Author: Per Unneberg
Created: Fri Oct 30 09:56:20 2015

'''

import pandas as pd
from bokeh.plotting import figure, gridplot
from bokeh.models import ColumnDataSource
from . import utils
from .color import colorbrewer
import logging

logger = logging.getLogger(__name__)

__all__ = ['scatter']

def scatter(x, y, df, return_source=False, marker='circle',
            **kwargs):
    """Wrapper for fig.scatter. Note that this function only supports a
    limited number of markers. For plotting e.g. text points, use
    points.

    """
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
                marker=marker,
                size=size, color=color, **kwargs)

    if return_source:
        return fig, source
    else:
        return fig, None


def points(x, y, df, return_source=False, glyph='circle', facet=None, **kwargs):
    # setup figure
    kwfig = utils.fig_args(kwargs)
    plot_height = kwargs.pop('plot_height', None)
    plot_width = kwargs.pop('plot_width', None)
    fig = utils.create_bokeh_fig(plot_height=plot_height,
                                 plot_width=plot_width,
                                 **kwfig)
    fig_props = set(fig.properties())
    kwfig = utils.fig_args(kwargs, fig_props)
    fig.set(**kwfig)

    # Check color argument
    color=kwargs.pop("color", "blue")
    size=kwargs.pop("size", 8)

    # create data source and scatter
    groups = None
    if color in df.columns:
        groups = df.groupby(color)
        colors = colorbrewer(datalen=len(list(set(df[color]))))
        colormap = {k:v for k,v in zip(sorted(set(df[color])), colors)}
    if size in df.columns:
        size = df[size]
    kwargs['size'] = size

    # In some cases we need to modify the arguments. There should be
    # an easy way to get this from the selected glyph properties.
    if glyph in ['text']:
        kwargs.pop('size')

    # Add arguments to kwargs
    kwargs['x'] = x
    kwargs['y'] = y

    source = ColumnDataSource(df)
    try:
        if groups:
            source_dict = {}
            for g, df in groups:
                kwargs['color'] = colormap[g]
                source = ColumnDataSource(df)
                kwargs['legend'] = str(g)
                getattr(fig, glyph)(source=source, **kwargs)
                source_dict[g] = source
            source = source_dict
        else:
            getattr(fig, glyph)(**kwargs)
    except:
        raise

    if return_source:
        return fig, source
    else:
        return fig, None
    
    # # Faceting function requested?
    # if facet is None:
    #     return _points(df=df, return_source=return_source, glyph=glyph, colormap=colormap, groups=groups, **kwargs)
    # else:
    #     kwargs['ncol'] = kwargs.get('ncol', 3)
    #     return _facet_grid(df=df, return_source=return_source, glyph=glyph, colormap=colormap, facet=facet, **kwargs)

    
def _points(df, return_source, glyph, colormap, groups, **kwargs):
    # setup figure
    kwfig = utils.fig_args(kwargs)
    fig = utils.create_bokeh_fig(plot_height=kwargs.pop('plot_height', None),
                                 plot_width=kwargs.pop('plot_width', None),
                                 **kwfig)
    fig_props = set(fig.properties())
    kwfig = utils.fig_args(kwargs, fig_props)
    fig.set(**kwfig)

    source = ColumnDataSource(df)
    try:
        if groups:
            source_dict = {}
            for g, df in groups:
                kwargs['color'] = colormap[g]
                source = ColumnDataSource(df)
                kwargs['legend'] = str(g)
                getattr(fig, glyph)(source=source, **kwargs)
                source_dict[g] = source
            source = source_dict
        else:
            getattr(fig, glyph)(**kwargs)
    except:
        raise

    if return_source:
        return fig, source
    else:
        return fig, None



def _facet_grid(df, return_source, glyph, colormap, facet, **kwargs):
    groups = df.groupby(facet)
    flist = []
    ncol = kwargs.pop('ncol')
    x = kwargs.pop('x')
    y = kwargs.pop('y')
    plot_height = kwargs.pop('plot_height')
    plot_width = kwargs.pop('plot_width')
    j = 0
    source_dict = {}
    for name, group in groups:
        name = str(name)
        kwfig = utils.fig_args(kwargs)
        subfig = utils.create_bokeh_fig(plot_height=plot_height,
                                        plot_width=plot_width,
                                        name = name,
                                        **kwfig)
        fig_props = set(subfig.properties())
        kwfig = utils.fig_args(kwargs, fig_props)
        subfig.set(**kwfig)
        source = ColumnDataSource(group)
        kw = {'legend': name,
              'x': x,
              'y': y}

        getattr(subfig, glyph)(source=source, **kw)
        source_dict[name] = source 
        if j > 0:
            if kwargs.get('share_x_range', None):
                subfig.x_range = flist[0].x_range
            if kwargs.get('share_y_range', None):
                subfig.y_range = flist[0].y_range
        j = j + 1
        flist.append(subfig)

    if return_source:
        return gridplot([flist[i:i+ncol] for i in range(0, len(flist), ncol)]), source_dict
    else:
        return gridplot([flist[i:i+ncol] for i in range(0, len(flist), ncol)]), None
