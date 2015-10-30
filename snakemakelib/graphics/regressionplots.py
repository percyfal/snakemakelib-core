# Copyright (C) 2015 by Per Unneberg
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
from snakemakelib.graphics import utils


__all__ = ['plot_regression']


def plot_regression(y, x, data, **kwargs):
    source = ColumnDataSource(data)
    fig = figure(plot_height = kwargs.pop('plot_height', 400),
                 plot_width = kwargs.pop('plot_width', 400),
                 x_axis_type = kwargs.pop('x_axis_type', 'linear'),
                 y_axis_type = kwargs.pop('y_axis_type', 'linear'),
                 x_axis_label = kwargs.pop('x_axis_label', x),
                 y_axis_label = kwargs.pop('y_axis_label', y),
                 
    )
    fig.circle(x=x, y=y, source=source)
    return fig
