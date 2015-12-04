# Copyright (C) 2015 by Per Unneberg
"""
Helper functions for graphics with bokeh
"""
from bokeh.models import ColumnDataSource
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

__all__ = ['create_bokeh_fig']


def _import_bokeh():
    try:
        import bokeh.plotting as plt
    except:
        raise ImportError("bokeh is not found.")

    return plt


def create_bokeh_fig(fig=None, plot_height=None, plot_width=None, **kw):
    if fig is None:
        plt = _import_bokeh()
        try:
            if plot_height is None or plot_width is None:
                smllogger.warning("plot_height and/or plot_width is None; figure will be initialized but not drawn")
            fig = plt.figure(plot_height=plot_height, plot_width=plot_width, **kw)
        except:
            raise
    return fig


def create_bokeh_fig_set_props(fig=None, plot_height=None, plot_width=None, **kwargs):
    """Create bokeh figure and set properties"""
    kwfig = fig_args(kwargs)
    fig = create_bokeh_fig(plot_height=kwargs.pop('plot_height', plot_height),
                           plot_width=kwargs.pop('plot_width', plot_width),
                           **kwfig)
    fig_props = set(fig.properties())
    kwfig = fig_args(kwargs, fig_props)
    fig.set(**kwfig)
    return fig


FIGURE_ATTRIBUTES = {'x_range', 'y_range', 'x_axis_type', 'y_axis_type',
                     'x_minor_ticks', 'y_minor_ticks', 'x_axis_location',
                     'y_axis_location', 'x_axis_label', 'y_axis_label',
                     'tools'}


def fig_args(kwargs, keys=FIGURE_ATTRIBUTES):
    return dict([ (k, kwargs.pop(k, None)) for k in keys if k in kwargs ])


def df_to_source(df):
    if not isinstance(df, ColumnDataSource):
        return ColumnDataSource(df)
    else:
        return df


GLYPH_ATTRIBUTES = {'color', 'size', 'alpha'}
    
def add_glyph(fig, x, y, source, marker, **kwargs):
    try:
        kwglyph = fig_args(kwargs, GLYPH_ATTRIBUTES)
        glyph = getattr(fig, marker)(x=x, y=y, source=source, **kwglyph)
        # props = glyph.properties()
        # kwglyph = fig_args(kwargs, props)
        # glyph.set(**kwglyph)
    except:
        raise
    return fig
