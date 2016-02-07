'''

Author: Per Unneberg
Created: Tue Dec  1 07:50:34 2015

'''
from bokeh.plotting import figure, gridplot
from bokeh.models import ColumnDataSource, GlyphRenderer, Legend
from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

__all__ = ['facet_grid']

def facet_grid(fig, x, y, df=None, source=None, groups=None, ncol=3,
               share_x_range=False, share_y_range=False, **kwargs):
    """
    facet_grid - generate a simple gridplot from a figure

    Args:
      fig (:py:class:`~bokeh.plotting.Plot`): bokeh Plot object
      x (str): string for x component
      y (str, list): string or list of strings for y component
      df (:py:class:`~pandas.DataFrame`): pandas DataFram
      groups (str, list(str)): groups to group by
      ncol (int): number of columns to use in gridplot
      share_x_range (bool): share x range across plots
      share_y_range (bool): share y range across plots
      kwargs: keyword arguments to pass to figure

    Returns:
      :class:~bokeh.models.GridPlot` object
    """
    if not groups:
        smllogger.warning("no groups defined; returning without modifying figure")
        return
    try:
        grouped = df.groupby(groups)
    except:
        raise
    flist = []
    gr = fig.select(GlyphRenderer)
    lgd = fig.select(Legend)
    if len(gr) == 0:
        smllogger.warning("no glyph renderer defined for plot; aborting")
        return
    j = 0
    for name, group in grouped:
        subfig = figure(title=str(name), **kwargs)
        for glyph, yy in zip(gr, y):
            plotfn = str(glyph.glyph).split(", ")[0].lower()
            kw = glyph.glyph.properties_with_values()
            kw.pop('x', None)
            kw.pop('y', None)
            kw.pop('xs', None)
            kw.pop('ys', None)
            source = ColumnDataSource(group)
            kw['legend'] = str(yy) if len(lgd) > 0 else None
            if plotfn == "multiline":
                plotfn = "line"
                getattr(subfig, plotfn)(x=x, y=yy, source=source, **kw)
            else:
                getattr(subfig, plotfn)(x=x, y=yy, source=source, **kw)
        if j > 0:
            if share_x_range:
                subfig.x_range = flist[0].x_range
            if share_y_range:
                subfig.y_range = flist[0].y_range
        j = j + 1
        flist.append(subfig)
    return gridplot([flist[i:i+ncol] for i in range(0, len(flist), ncol)])
    

