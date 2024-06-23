---
layout: page
title: Epigenome-wide association studies using approximate message passing
authors: Jakub Bajzik, Al Depope, Daniel L. McCartney, Markus J. Bauer, Riccardo E. Marioni, Marco Mondelli and Matthew R. Robinson
publication: 
year: 2024
pdf: false
summary: We develop and apply an approximate message passing-based paradigm called gVAMPomi to the largest human methylation dataset generated to date, the Generation Scotland study, and find 92 CpG probes whose effects are significantly associated with traits, conditional on all other CpG probes, representing a significant increase over 37 CpG probes discovered by baseline MCMC approach.
---


## Abstract

Recent technological advances allow for a diverse range of genomic features to be measured within individuals or single cells, that are linked to electronic health information and patient outcomes. However, current state-of-the-art statistical methods for these data do not allow for reliable significance testing and become inefficient in large scales and high dimensions. Ideally, we wish to utilize multiple types of genomic data (sequence, methylation, and/or gene expression) to jointly estimate the effect of each variable on an outcome, conditional on all others, whilst controlling for potential confounding factors. Marco Chain Monte Carlo (MCMC) methods have become a standard method for this in epigenome-wide association studies, however, they are characteristically slow and association testing is difficult. Here, we propose a new method called gVAMPomi, based on the recently developed genomic Vector Approximate Message Passing (gVAMP) algorithm, which is an iterative algorithm allowing for joint inference of model parameters, while providing joint p-value testing utilizing the properties of state evolution (SE). We initialize gVAMPomi with an efficient MCMC algorithm and then estimate biological variable associations and conduct association testing. Using simulations, we show that gVAMPomi reaches MCMC performance in both out-of-sample prediction accuracy and association testing. Next, we apply gVAMPomi to the largest human methylation dataset generated to date, the Generation Scotland study, and find 92 CpG probes whose effects are significantly associated with traits, conditional on all other CpG probes, representing a significant increase over 37 CpG probes discovered by baseline MCMC approach. Overall, gVAMPomi scales to accommodate future large-scale omics data, allowing for the construction of more complex models and testing novel biological hypotheses.
