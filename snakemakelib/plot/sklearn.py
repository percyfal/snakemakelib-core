# Copyright (C) 2015 by Per Unneberg
import pandas as pd
from bokeh.models import ColumnDataSource
"""Plotting functions for sklearn output"""

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
    df_pca = pd.read_csv(pca_results_file, index_col="sample")
    df_pca['color'] = [kwargs.get('color', 'red')] * df_pca.shape[0]
    df_pca['x'] = df_pca['0']
    df_pca['y'] = df_pca['1']
    df_pca['size'] = [kwargs.get('size', 10)] * df_pca.shape[0]
    source = ColumnDataSource(df_pca)
