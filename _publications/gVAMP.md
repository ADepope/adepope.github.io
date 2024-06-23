---
layout: page
title: Light-speed inference of genetic effects via Approximate Message Passing
authors: Al Depope*, Jakub Bajzik, Marco Mondelli and Matthew R. Robinson
summary: We develop a new algorithmic paradigm, based on Approximate Message Passing (AMP), specifically tailored for both genomic prediction and association testing. Our gVAMP (genomic Vector AMP) approach requires less than a day to jointly estimate the effects of 8.4 million imputed genetic variants in over 400,000 UK Biobank participants, and it provides an association testing framework capable of directly fine-mapping each genetic variant, or gene burden score, conditional on all other measured DNA variation genome-wide. 
year: 2024
pdf: true
---

## Abstract

Efficient utilization of large-scale biobank data is crucial for inferring the genetic basis of disease and predicting health outcomes from the DNA. Yet we lack accurate statistical models to estimate the effect of each locus, conditional on all other genetic variants, controlling for both local and long-range linkage disequilibrium. Additionally, we lack algorithms which scale to data where health records are linked to whole genome sequence information. 

To address these issues, we develop a new algorithmic paradigm, based on Approximate Message Passing (AMP), specifically tailored for both genomic prediction and association testing. Our gVAMP (genomic Vector AMP) approach requires less than a day to jointly estimate the effects of 8.4 million imputed genetic variants in over 400,000 UK Biobank participants, and it provides an association testing framework capable of directly fine-mapping each genetic variant, or gene burden score, conditional on all other measured DNA variation genome-wide. 

Across 13 traits, we find 8,222 genome-wide significant autosomal associations that are localised to the single-locus level, conditional on all other imputed loci. Extending the model to jointly estimate the effects of rare variant gene burden scores from sequencing data and imputed X chromosome variants, conditional on all other genes and all 8.8 million variants, we find 60 genes where rare coding mutations significantly influence phenotype, and 76 associations localised to the single-locus level on chromosome X, for five traits. In comparison to existing state-of-the-art methods, both in simulations and in application to the UK Biobank, gVAMP yields out-of-sample prediction accuracy comparable to individual-level Bayesian methods, outperforms summary statistic Bayesian methods, and outperforms REGENIE for standard association testing, in a fraction of the compute time. This truly large-scale development of the AMP framework establishes the foundations for a far wider range of statistical analyses for hundreds of millions of variables measured on millions of people.
