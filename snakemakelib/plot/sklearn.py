# Copyright (C) 2015 by Per Unneberg
"""Plotting functions for sklearn output"""
import pandas as pd
import pickle
import re
import numpy as np
from snakemakelib.plot.bokeh import colorbrewer
from snakemakelib.graphics import tooltips, xaxis, yaxis, dotplot, points
import snakemakelib.graphics.utils
from bokeh.plotting import figure, gridplot
from bokeh.models import ColumnDataSource, CustomJS, HoverTool, OpenURL, TapTool
from bokeh.charts import Scatter
from bokeh.io import vform
from bokeh.models.widgets import Select, Toggle

from snakemakelib.log import LoggerManager

smllogger = LoggerManager().getLogger(__name__)

TOOLS = "pan,wheel_zoom,box_zoom,box_select,lasso_select,resize,reset,save,hover"

def plot_pca(pca_results_file=None, metadata=None, pcaobjfile=None, taptool_url=None, **kwargs):
    """Make PCA plot

    Args:
      pca_results_file (str): pca results file
      metadata (str): metadata file name
      pcaobjfile (str): file name containing pickled pca object
      taptool_url (str): url prefix that is attached to taptool; typically a link to ensembl

    Returns: 
      dict: dictionary with keys 'fig' pointing to a (:py:class:`~bokeh.models.GridPlot`) Bokeh GridPlot object and key 'table' pointing to a (:py:class:`~bokeh.widgets.DataTable`) DataTable

    """
    md = None
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
    pca_source = ColumnDataSource(df_pca)
    cmap = colorbrewer(datalen = df_pca.shape[0])

    callback = CustomJS(args=dict(source=pca_source),
                        code="""pca_callback(source, cb_obj, "SM");""")
    xcallback = CustomJS(args=dict(source=pca_source),
                         code="""pca_component(source, cb_obj, "x");""")
    ycallback = CustomJS(args=dict(source=pca_source),
                         code="""pca_component(source, cb_obj, "y");""")

    if not md is None:
        # Waiting for callbacks to be implemented upstream in bokeh
        # rbg = RadioButtonGroup(labels=list(md.columns),
        #                        callback=callback)
        toggle_buttons = [Toggle(label=x, callback=callback) for x in list(md.columns) + ["TPM", "FPKM"]]
    else:
        toggle_buttons = []

    pca_components = sorted([int(x) + 1 for x in pca_source.column_names if re.match("\d+", x)])
    # NB: assumes existence of pcaobj
    menulist = ["{} ({:.2f}%)".format(x, 100.0 * p) for x, p in zip(pca_components, pcaobj.explained_variance_ratio_)]
    component_x = Select(title = "PCA component x", options = menulist, value=menulist[0],
                         callback=xcallback)
    component_y = Select(title = "PCA component y", options = menulist, value=menulist[1],
                         callback=ycallback)

    # Make the pca plot
    kwargs = {'plot_width': 400, 'plot_height': 400,
              'title_text_font_size': "12pt",
              'title': "Principal component analysis",
              'tools': TOOLS,
              'x_axis_label_text_font_size': '10pt',
              'x_major_label_orientation': np.pi/3,
              'y_axis_label_text_font_size': '10pt',
              'y_major_label_orientation': np.pi/3,
    }
    fig = points('x', 'y', df=pca_source, color='color', size='size', alpha=0.7, **kwargs)
    tooltiplist = [("sample", "@SM")] if "SM" in pca_source.column_names else []
    if not md is None:
        tooltiplist = tooltiplist + [(str(x), "@{}".format(x)) for x
                                     in md.columns] + \
        [("Detected genes (TPM)", "@TPM"), ("Detected genes (FPKM)", "@FPKM")]
    tooltips(fig, HoverTool, tooltiplist)

    # Loadings
    loadings = pd.DataFrame(pcaobj.components_).T
    loadings.columns = [str(x) for x in loadings.columns]
    loadings['x'] = loadings['0']
    loadings['y'] = loadings['1']
    try:
        loadings["gene_id"] = pcaobj.features
    except:
        smllogger.warn("failed to set gene_id")
        raise

    try:
        loadings["gene_name"] = [pcaobj.labels[x] for x in loadings["gene_id"]]
    except:
        smllogger.warn("failed to set gene_name")
        raise
    loadings_source = ColumnDataSource(loadings)
    kwargs.update({'title': "Loadings"})
    loadings_fig = points(x='x', y='y', df=loadings_source,
                          **kwargs)

    tooltips(loadings_fig, HoverTool, [('gene_id', '@gene_id'), ('gene_name', '@gene_name')])
    x_loadings_callback = CustomJS(args=dict(source=loadings_source),
                                   code="""pca_loadings(source, cb_obj, "x");""")
    y_loadings_callback = CustomJS(args=dict(source=loadings_source),
                                   code="""pca_loadings(source, cb_obj, "y");""")
    menulist = ["{} ({:.2f}%)".format(x, 100.0 * p) for x, p in zip(pca_components, pcaobj.explained_variance_ratio_)]
    loadings_component_x = Select(title = "PCA loading x", options = menulist, value=menulist[0],
                         callback=x_loadings_callback)
    loadings_component_y = Select(title = "PCA loading y", options = menulist, value=menulist[1],
                         callback=y_loadings_callback)


    # Add taptool url if present
    if taptool_url:
        loadings_fig.add_tools(TapTool(callback=OpenURL(url=taptool_url)))

    # Detected genes, FPKM and TPM
    kwargs.update({'title': 'Number of detected genes',
                   'xlabel': "Sample",
                   'ylabel': "Detected genes",
                   'x_range': list(pca_source.data["SM"])})
    n_genes_fig = dotplot(df=pca_source, x="SM", y="TPM", **kwargs)
    tooltips(n_genes_fig, HoverTool, [('sample', '@SM'),
                                      ('# genes (TPM)', '@TPM'),
                                      ('# genes (FPKM)', '@FPKM')])

    buttons = toggle_buttons + [component_x, component_y] + [loadings_component_x, loadings_component_y]
    return {'pca' : vform(*(buttons + [gridplot([[fig, loadings_fig, n_genes_fig]])]))}
