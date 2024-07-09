---
layout: page
title: Joint modelling of whole genome sequence data for human height via approximate message passing
authors: Al Depope*, Jakub Bajzik, Marco Mondelli and Matthew R. Robinson
summary: We develop a new algorithmic paradigm based on approximate message passing, gVAMP, to directly fine-map whole-genome sequence (WGS) variants and gene burden scores, conditional on all other measured DNA variation genome-wide. We find that the genetic architecture of height inferred from WGS data differs from that inferred from imputed single nucleotide polymorphism (SNP) variants: common variant associations from imputed SNP data are allocated to WGS variants of lower frequency, and there is a stronger relationship of effect size and variant frequency. 
year: 2024
pdf: true
---

## Abstract

Human height is a model for the genetic analysis of complex traits, and recent studies suggest the presence of thousands of common genetic variant associations and hundreds of low-frequency/rare variants. However, it has not yet been possible to fine-map the genetic basis of height, since all variant effects have not been modelled jointly leaving correlations unaccounted for. To address this issue, we develop a new algorithmic paradigm based on approximate message passing, gVAMP, to directly fine-map whole-genome sequence (WGS) variants and gene burden scores, conditional on all other measured DNA variation genome-wide. We find that the genetic architecture of height inferred from WGS data differs from that inferred from imputed single nucleotide polymorphism (SNP) variants: common variant associations from imputed SNP data are allocated to WGS variants of lower frequency, and there is a stronger relationship of effect size and variant frequency. Thus, even fine-mapped imputed variants are systematically mis-assigned and without the joint analysis of WGS data it remains premature, if not unfounded, to make statements regarding the number of independent associations and their properties. We validate gVAMP on various datasets across UK Biobank traits where it outperforms widely used methods for polygenic risk score prediction and association testing, offering a scalable foundation towards analyzing hundreds of millions of variables measured on millions of people.
