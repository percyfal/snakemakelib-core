# Copyright (C) 2015 by Per Unneberg
"""
Helper functions for graphics with bokeh
"""

__all__ = ['create_bokeh_fig']


def _import_bokeh():
    try:
        import bokeh.plotting as plt
    except:
        raise ImportError("bokeh is not found.")

    return plt


def create_bokeh_fig(fig=None, plot_height=None, plot_width=None):
    if fig is None:
        plt = _import_bokeh()
        fig = plt.figure(plot_height=plot_height, plot_width=plot_width)

    return fig
