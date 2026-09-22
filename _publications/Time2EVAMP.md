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

Identifying which molecular markers drive the timing of disease onset is a central question in precision medicine, and proteomic assays now measure thousands of such markers across hundreds of thousands of individuals. The standard tools for these data &mdash; penalised Cox regression and, more recently, deep-learning survival models &mdash; either treat markers one at a time, offer no calibrated uncertainty, or do not scale.

We propose vampW, an approximate message passing framework for time-to-event data under a Weibull model. It estimates the effect of every biomarker jointly, conditional on all the others, while retaining the state-evolution guarantees that make principled significance testing possible. Applied to the UK Biobank Pharma Proteomics Project, vampW achieves a 26&ndash;33% relative improvement in onset prediction over penalised Cox and baseline deep-learning approaches, and selects a sparse and interpretable set of markers.

A preprint is available on [bioRxiv](https://www.biorxiv.org/content/10.64898/2026.04.30.721585v1), and a short version appeared at the [ICLR Workshop on Machine Learning for Genomics Explorations](https://openreview.net/forum?id=Re1rA204zd). The code is on [GitHub](https://github.com/Information-and-learning-for-genomics/Time2EVAMP).
