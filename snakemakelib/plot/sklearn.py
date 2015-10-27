# Copyright (C) 2015 by Per Unneberg
"""Plotting functions for sklearn output"""
import pandas as pd
import pickle
import re
import numpy as np
from snakemakelib.plot.bokeh import colorbrewer
from bokeh.plotting import figure, gridplot
from bokeh.models import ColumnDataSource, CustomJS, HoverTool
from bokeh.io import vform
from bokeh.models.widgets import Select, Toggle
from bokehutils.axes import xaxis, yaxis
from bokehutils.geom import dotplot, points
from bokehutils.tools import tooltips

TOOLS = "pan,wheel_zoom,box_zoom,box_select,lasso_select,resize,reset,save,hover"

def plot_pca(pca_results_file=None, metadata=None, pcaobjfile=None, **kwargs):
    """Make PCA plot

    Args:
      pca_results_file (str): pca results file
      metadata (str): metadata file name
      pcaobjfile (str): file name containing pickled pca object

    Returns: 
      dict: dictionary with keys 'fig' pointing to a (:py:class:`~bokeh.models.GridPlot`) Bokeh GridPlot object and key 'table' pointing to a (:py:class:`~bokeh.widgets.DataTable`) DataTable

    """
    if not metadata is None:
        md = pd.read_csv(metadata, index_col=0)
    if not pcaobjfile is None:
        with open(pcaobjfile, 'rb') as fh:
            pcaobj = pickle.load(fh)
    df_pca = pd.read_csv(pca_results_file, index_col=kwargs.get('index_col', "SM"))
    df_pca['color'] = [kwargs.get('color', 'red')] * df_pca.shape[0]
    df_pca['x'] = df_pca['0']
    df_pca['y'] = df_pca['1']
    df_pca['size'] = [kwargs.get('size', 10)] * df_pca.shape[0]
    source = ColumnDataSource(df_pca)
    cmap = colorbrewer(datalen = df_pca.shape[0])

    callback = CustomJS(args=dict(source=source),
                        code="""pca_callback(source, cb_obj, "SM");""")
    xcallback = CustomJS(args=dict(source=source),
                         code="""pca_component(source, cb_obj, "x");""")
    ycallback = CustomJS(args=dict(source=source),
                         code="""pca_component(source, cb_obj, "y");""")

    if not md is None:
        # Waiting for callbacks to be implemented upstream in bokeh
        # rbg = RadioButtonGroup(labels=list(md.columns),
        #                        callback=callback)
        toggle_buttons = [Toggle(label=x, callback=callback) for x in list(md.columns) + ["TPM", "FPKM"]]
    else:
        toggle_buttons = []

    pca_components = sorted([int(x) + 1 for x in source.column_names if re.match("\d+", x)])
    # NB: assumes existence of pcaobj
    menulist = ["{} ({:.2f}%)".format(x, 100.0 * p) for x, p in zip(pca_components, pcaobj.explained_variance_ratio_)]
    component_x = Select(title = "PCA component x", options = menulist, value=menulist[0],
                         callback=xcallback)
    component_y = Select(title = "PCA component y", options = menulist, value=menulist[1],
                         callback=ycallback)

    buttons = toggle_buttons + [component_x, component_y]

    # Make the pca plot
    kwfig = {'plot_width': 400, 'plot_height': 400,
             'title_text_font_size': "12pt"}

    p1 = figure(title="Principal component analysis",
                tools=TOOLS, **kwfig)

    points(p1, 'x', 'y', source=source, color='color', size='size',
           alpha=.7)
    kwxaxis = {
               'axis_label_text_font_size': '10pt',
               'major_label_orientation': np.pi/3}
    kwyaxis = {
        'axis_label_text_font_size': '10pt',
        'major_label_orientation': np.pi/3}
    xaxis(p1, **kwxaxis)
    yaxis(p1, **kwyaxis)
    tooltiplist = [("sample", "@SM")] if "SM" in source.column_names else []
    if not md is None:
        tooltiplist = tooltiplist + [(str(x), "@{}".format(x)) for x
                                     in md.columns] + \
        [("Detected genes (TPM)", "@TPM"), ("Detected genes (FPKM)", "@FPKM")]
    tooltips(p1, HoverTool, tooltiplist)

    # Detected genes, FPKM and TPM
    p2 = figure(title="Number of detected genes",
                x_range=list(df_pca.index), tools=TOOLS,
                **kwfig)
    kwxaxis.update({'axis_label': "Sample"})
    kwyaxis.update({'axis_label': "Detected genes"})
    dotplot(p2, "SM", "FPKM", source=source)
    xaxis(p2, **kwxaxis)
    yaxis(p2, **kwyaxis)
    tooltips(p2, HoverTool, [('sample', '@SM'),
                             ('# genes (FPKM)', '@FPKM')])
    return {'pca' : vform(*(buttons + [gridplot([[p1, p2]])]))}
