import scanpy as sc
import anndata



import importlib

import pandas as pd
import numpy as np
#import scanpy as sc
#import scycle as cc
# import scvelo as sv
#import anndata
from sklearn.decomposition import PCA

import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors


adata = sc.read_h5ad("data/SKM_human.h5ad")
cell_type_mask = adata.obs["annotation_level0"] == target_cell_type
expression_data = adata[cell_type_mask, adata.var_names == adata.var_names].X
mean_expression = expression_data.mean()
unique_cell_types = adata.obs["annotation_level0"].unique()
cell_types = unique_cell_types.tolist()
cell_type_counts = adata.obs["annotation_level0"].value_counts()
#cell_type_counts = adata.obs["annotation"].value_counts()

total_cells = len(adata.obs)
cell_type_proportions = {cell_type: count / total_cells for cell_type, count in cell_type_counts.items()}
valid_genes = list(adata.var_names)
expression_data = []

# Loop through each cell type and gene
for cell_type in cell_types:
    cell_mask = adata.obs["annotation_level0"] == cell_type
    
    for gene in valid_genes:
        mean_expression = adata[cell_mask, adata.var_names == gene].X.mean()
        expression_data.append({"Cell Type": cell_type, "Gene": gene, "Mean Expression": mean_expression})

# Convert to a Pandas DataFrame
expression_df = pd.DataFrame(expression_data)
expression_df=expression_df.drop_duplicates()
expression_df.to_csv("mean_expression_gene_cell_type.csv")

reshaped_df = expression_df.pivot(index="Gene", columns="Cell Type", values="Mean Expression")

# Optionally, sort the index and columns for better organization
reshaped_df = reshaped_df.sort_index().sort_index(axis=1)

reshaped_df["most abundant in"] = reshaped_df.idxmax(axis=1)
reshaped_df["most abundant in"]
reshaped_df.to_csv("results/mean_expression_cell.csv")
proportion_df = pd.DataFrame.from_dict(cell_type_proportions, orient="index", columns=["Proportion"])

# Reset the index to make the cell type a column (optional)
proportion_df = proportion_df.reset_index().rename(columns={"index": "Cell Type"})
proportion_df = proportion_df.set_index("Cell Type")

proportion_df.to_csv("results/proportion_cell_type.csv")