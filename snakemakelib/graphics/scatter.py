'''scatter plots with bokeh

Author: Per Unneberg
Created: Fri Oct 30 09:56:20 2015

'''

from bokeh.models import ColumnDataSource, GlyphRenderer
from . import utils
import logging

logger = logging.getLogger(__name__)

__all__ = ['scatter']


def scatter(x, y, df, return_source=False, glyph='circle', **kwargs):
    # setup figure
    fig = utils.create_bokeh_fig(plot_height=kwargs.pop('plot_height', None),
                                 plot_width=kwargs.pop('plot_width', None))
    fig_props = set(fig.properties())
    kwfig = {k: v for k, v in kwargs.items() if k in fig_props}
    fig.set(**kwfig)

    # create data source
    source = ColumnDataSource(df)

    # Add glyph
    # Must exist some easier way...
    glyph_props = set(GlyphRenderer().properties())
    kwglyph = {k: v for k, v in kwargs.items() if k in glyph_props}
    try:
        getattr(fig, glyph)(x=x, y=y, source=source, **kwglyph)
    except AttributeError:
        logger.error("no such glyph function {} for {}".format(glyph, fig))
        raise
    if return_source:
        return fig, source
    else:
        return fig, None
