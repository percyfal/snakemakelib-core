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

def pca_results(pcaobj, expr, metadata=None, return_loadings=True, n_loadings=20, **kwargs):
    """Generate output file on which to base pca plots
    
    Args:
      pcaobj (PCA): pca model
      expr (DataFrame): pandas data frame with expression values
      metadata (DataFrame): sample metadata
      return_loadings (bool): return loadings for model
      n_loadings (int): number of loadings to use

    Returns:
      pcares (DataFrame): pca results concatenated,
      loadings (DataFrame): pca loadings of top n_loadings for each component
    """
    pcares = pd.DataFrame(pcaobj.fit(expr).transform(expr))
    if not expr.index.name is None:
        pcares.index = expr.index
    if not metadata is None:
        md = pd.read_csv(metadata, index_col=expr.index.name) # FIXME: may not be present!
        pcares = pcares.join(md)
    loadings = None
    if return_loadings:
        N = min(pcaobj.n_components, len(pcaobj.components_))
        if N < pcaobj.n_components:
            pass # Error message here
        sorted_components = [pcaobj.components_[i].argsort() for i in range(N)]
        loading_indices = [y for x in sorted_components for y in list(x[-n_loadings:]) + list(x[:n_loadings])]
        index = pd.MultiIndex.from_arrays([expr.iloc[:, loading_indices].columns,
                                           [y for x in [list(range(-n_loadings,0)) + list(range(1, n_loadings + 1))] * N for y in x],
                                           [x + 1 for i in list(range(N)) for x in [i] * n_loadings * 2]],
                                          names=["gene_id", "loading", "component"])
        loadings = pd.DataFrame(expr.iloc[:, loading_indices])
        loadings.columns = index
        loadings = loadings.stack(level=list(index.names)).reset_index()
        loadings.columns = list(loadings.columns[:-1]) + ["values"]
    return pcares, loadings
