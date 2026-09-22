---
layout: page
title: Joint variable selection for omic biomarkers in time-to-event data
authors: Jakub Bajzik*, Al Depope*, Marco Mondelli and Matthew R. Robinson
year: 2026
order: 50
pdf: false
teaser: Time2EVAMP_small.svg
status: ICLR workshop paper, 2026
doi: https://openreview.net/forum?id=Re1rA204zd
preprint: https://www.biorxiv.org/content/10.64898/2026.04.30.721585v1
code: https://github.com/Information-and-learning-for-genomics/Time2EVAMP
summary: We build vampW, a scalable Bayesian framework based on approximate message passing that models disease onset times under a Weibull model and selects omic biomarkers jointly, conditional on all others. Applied to the UK Biobank Pharma Proteomics Project, it improves onset prediction by 26–33% relative to penalised Cox regression and baseline deep-learning approaches.
---

## Abstract

The incidence of the vast majority of neurodegenerative, cancer, and metabolic diseases generally increases exponentially with age. In large-scale biobanks, linking time-to-diagnosis information in electronic health records to multiple genomic ("multiomics") measures has the potential to reveal the genes and biological pathways involved in the disease onset and progression. To date, association testing has commonly been conducted by testing one variable at a time using semiparametric Cox proportional hazards (CoxPH) models, which ignores correlation structure and increases the risk of false discoveries. To address these issues, we introduce a novel fully parametric Bayesian computational method, vampW, based on the Vector Approximate Message Passing framework applied to a Weibull model. vampW jointly models correlated features, while providing an interpretable hazard structure, producing a continuous survival curve, and incorporating prior knowledge. In an extensive simulation study, we demonstrate that joint modeling of omics data and time-to-event outcomes with vampW, substantially reduces false discoveries in comparison to marginal testing and other forms of joint CoxPH models. In 53,018 individuals from the UK Biobank, vampW identifies 219 protein associations with 24 disease outcomes, most of which are not among the top marginal discoveries. We further correct protein levels for exponential age effects, identifying 1,308 associations and highlighting the sensitivity of the analysis to age-correction methodology. Our findings replicate in independent cohorts using different measurement technologies, within data from Iceland and a novel Generation Scotland proteomics dataset. vampW also achieves significant improvement in the prediction of disease onset times: across 14 outcomes, it reduces the root mean squared error by over 32% and 26%, when compared to CoxPH variants and the deep learning approach DeepSurv, respectively, while maintaining predictive utility in minority populations. In summary, vampW offers accurate and interpretable variable selection and out-of-sample prediction within a single computational framework, making it a powerful tool for dissecting the genomic architecture of common complex disease onset.

A preprint is available on [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.30.721585v1), and a short version appeared at the [ICLR Workshop on Machine Learning for Genomics Explorations](https://openreview.net/forum?id=Re1rA204zd). The code is on [GitHub](https://github.com/Information-and-learning-for-genomics/Time2EVAMP).
