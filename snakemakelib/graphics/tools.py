'''

Author: Per Unneberg
Created: Mon Nov 30 16:59:49 2015

'''
from bokeh.models.tools import Tool

__all__ = ['tooltips']

def tooltips(fig, tool, tips):
    assert type(tool) == type(Tool),\
        "tool parameter must be of type {}".format(Tool)
    h = fig.select(dict(type=tool))
    h.tooltips = tips
