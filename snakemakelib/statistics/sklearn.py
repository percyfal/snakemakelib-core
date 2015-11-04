# Copyright (C) 2015 by Per Unneberg
"""sklearn machine learning"""
from sklearn.decomposition import PCA
import pandas as pd

def pca(expr, **kwargs):
    """scrnaseq pca - run pca

    Args:
      expr (DataFrame): pandas data frame with expression values, rows
      correspond to samples/experimental units, columns to genes
      kwargs: keyword arguments

    Returns:
      pcaobj (PCA): PCA model fitted to expr
    """
    pcaobj = PCA(n_components=kwargs.get("n_components", 10))
    pcaobj.fit(expr)
    return pcaobj

def pca_results(pcaobj, expr, metadata=None, **kwargs):
    """Generate output file on which to base pca plots
    
    Args:
      pcaobj (PCA): pca model
      expr (DataFrame): pandas data frame with expression values
      metadata (DataFrame): sample metadata

    Returns:
      pcares (DataFrame): pca results concatenated,
      loadings (DataFrame): pca loadings of top 10 units for each component
    """
    pcares = pd.DataFrame(pcaobj.fit(expr).transform(expr))
    if not expr.index.name is None:
        pcares.index = expr.index
    if not metadata is None:
        md = pd.read_csv(metadata, index_col=expr.index.name) # FIXME: may not be present!
        pcares = pcares.join(md)
    return pcares
