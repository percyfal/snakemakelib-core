# Copyright (C) 2015 by Per Unneberg
import numpy as np
from bokeh.models import ColumnDataSource
import pandas as pd
import statsmodels.api as sm
from . import rnaseq


# FIXME: make into class? use .fit() notation; see statsmodels,
# sklearn for inspiration
class ScrnaseqTechnicalNoise(object):
    def __init__(self, df, df_spikein, quantile=.95, cutoff=.3,
                 **kwargs):
        self._data = pd.concat([df, df_spikein], keys=["gene",
                                                       "spikein"])
        self._data.index.names = ["spikein"] + df.index.names
        self._data_norm = self._data
        self.quantile = quantile
        self.cutoff = cutoff

        
    def _calc_size_factors(self):
        return pd.Series({
            g[0]:rnaseq.estimate_size_factors_for_matrix(g[1]) for
            g in self._data.groupby(level="spikein")
        })

    
    def _calc_min_mean_for_fit(self):
        self._means = self._data_norm.mean(axis=1)
        self._vars = self._data_norm.var(axis=1)
        self._cv2 = self._vars / (self._means ** 2)
        self._min_mean_for_fit = self._means.loc['gene', :][(self._cv2.loc['gene', :] > self.cutoff)].dropna().quantile(q=self.quantile)
        
        
    @property
    def size_factors(self):
        return self._size_factors


    @property
    def coefficients(self):
        return self._coef

    
    def fit(self):
        self._size_factors = self._calc_size_factors()
        self._data_norm = pd.concat([
            df / self._size_factors[spikein]
            for spikein, df in self._data.groupby(level="spikein")
        ])
        self._calc_min_mean_for_fit()
        use_for_fit = self._means.loc['gene', :] > self._min_mean_for_fit
        X = 1/self._means.loc['gene', :][use_for_fit]
        X = sm.add_constant(X)
        X.columns = ['a0', 'a1tilde']
        gamma_results = sm.GLM(self._cv2.loc['gene', :][use_for_fit], X, family = sm.families.Gamma()).fit()
        self._xi = (1 / self.size_factors['gene']).mean()
        coef = gamma_results.params
        coef['a1tilde'] = coef['a1tilde'] - self._xi
        self._coef = coef
        self._fitted_data = pd.concat([self._means, self._cv2], axis=1)
        self._fitted_data.columns = ["normalized mean", "cv2"]
