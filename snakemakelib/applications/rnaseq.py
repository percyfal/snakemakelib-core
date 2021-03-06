# Copyright (C) 2015 by Per Unneberg
import numpy as np
import pandas as pd
import math
from snakemakelib.log import LoggerManager
from snakemakelib.odo.utils import annotate_df
from snakemakelib.odo import rpkmforgenes, rsem

logger = LoggerManager().getLogger(__name__)

__all__ = ['number_of_detected_genes', 'estimate_size_factors_for_matrix', 'summarize_expression_data']

def number_of_detected_genes(expr_long, cutoff=1.0, quantification="TPM", **kwargs):
    """Aggregate expression data frame to count number of detected genes

    Args:
      expr_long (DataFrame): pandas data frame with expression values in long format
      cutoff (float): cutoff for detected gene
      quantification (str): quantification label, TPM or FPKM

    Returns:
      detected_genes (DataFrame): aggregated data fram with number of detected genes per sample
    """
    try:
        detected_genes = expr_long.groupby(kwargs.get("groupby", 'SM')).agg(lambda x: sum(x > cutoff))
    except Exception as e:
        logger.warning("Failed to group genes by sample :", e)
        detected_genes = None
    return detected_genes

def _gene_name_map_from_gtf(gtf, unit_id, unit_name):
    """Get a mapping from gene_id to gene_name"""
    mapping = {}
    for feature in gtf[8]:
        tmp = {k.replace("\"", ""):v.replace("\"", "") for k, v in [x.split(" ") for x in feature.split("; ")]}
        mapping[tmp.get(unit_id, "")] = tmp.get(unit_name, tmp.get(unit_id, ""))
    return mapping


def read_gene_expression(infile, annotation=None, unit_id="gene_id",
                         unit_name="gene_name"):
    """Read gene expression file, renaming genes if annotation present.

    NB: currently assumes annotation file is in gtf format and that
    gene expression levels, not transcript, are used

    Args:
      infile (str): infile name
      annotation (str): annotation file, gtf format
      unit_id (str): id of measurement unit; gene_id or transcript_id
      unit_name (str): name of measurement unit, as defined by annotation file
    
    Returns:
      expr (DataFrame): (possibly annotated) data frame

    """
    expr = pd.read_csv(infile)
    if annotation:
        annot = pd.read_table(annotation, header=None)
        mapping = _gene_name_map_from_gtf(annot, unit_id, unit_name)
        expr[unit_name] = expr[unit_id].map(mapping.get)
    return expr

def summarize_expression_data(targets, outfile, parser, groupnames=["SM"]):
    """Summarize several expression result files and save as csv output file"""
    dflist = [annotate_df(t, parser, groupnames=groupnames) for t in targets]
    df_long = pd.concat(dflist)
    df_long.to_csv(outfile)
        

def estimate_size_factors_for_matrix(counts, locfunc=np.median):
    """Estimate size factors from count data frame.

    See bioconductor:DEseq2::estimateSizeFactorsForMatrix for original
    R implementation.

    Args:
      counts (DataFrame): counts data frame in wide format
      locfunc (func): location function

    Returns:
      sizes (Series): size factors for groups
    """
    loggeomeans = counts.apply(np.log, axis=1).mean(axis=1)
    finite = loggeomeans.apply(np.isfinite)
    factors = counts.apply(np.log, axis=1).apply(lambda x: np.exp( locfunc ((x - loggeomeans).loc[finite])))
    return factors
