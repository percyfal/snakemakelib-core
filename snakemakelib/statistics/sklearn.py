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

def pca_results(pcaobj, X, **kwargs):
    """Generate output file on which to base pca plots
    
    Args:
      pcaobj (PCA): pca model
      X (DataFrame): pandas data frame

    Returns:
      pcares (DataFrame): pca results
    """
    pcares = pd.DataFrame(pcaobj.fit(X).transform(X))
    if not X.index.name is None:
        pcares.index = X.index
    return pcares
