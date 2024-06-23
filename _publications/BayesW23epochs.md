---
layout: page
title: Detection of age-specific genetic effects for age-at-onset complex traits
authors: Sven Erik Ojavee and Al Depope
year: 2020
slides: false
pdf: true
summary: We develop an extension of the time-to-event MCMC software called BayesW to two and three epochs by imposing statistical model and deriving Gibbs updates for interaction parameters and epoch-specific parameters.
---

## Abstract

The advent of genome-wide association (GWA) studies has enabled to better understand the genetic architecture and estimate its properties for many important complex traits. Among those are traits related to age-at-onset that stand out from others as they can almost always be right censored, meaning that we might only be able to measure the last known time without the event. Therefore, time-to-event traits have posed certain difficulties potentially leading to hampered statistical power or simply neglecting those traits from analyses. 

Recently, the methodology for conducting GWA studies for time-to-event traits has greatly improved. The usage of martingale residuals has enabled combining censoring and timing information into one summary statistic which can be then plugged in for other available methods and software for further analysis. For joint marker effect estimation that combines censoring and timing informations in the partial likelihood in regularised regression framework there exists Cox-LASSO implementation snpnet designed for variable selection and estimation in high-dimensional marker data. To analyse time-to-event traits in mixed model framework the COXMEG method has recently been proposed, although it might not yet be completely scalable for biobank-scale data sets. Joint effect size estimation along with variable selection and effect size classification has been lately implemented within Bayesian framework in the BayesW model that also enables partitioning genetic variance between different annotations. The latter approach has been shown to be efficient for genetic prediction and effect size classification enables better understanding of the genetic architecture.

Regardless of the advances proposed by the previous models, all of the previously described methods are assuming that the marker effect sizes on the trait remain constant throughout individual's life. That underlying assumption is definitely natural for many complex traits that are not describing age-at-onset. For example, once an individual has reached maximal growth, the height will remain relatively similar throughout the life and thus it is reasonable to model constant marker effect sizes having impacted height. In contrast to that, age-at-onset traits are affected by the hazard of onset that could vary throughout the life and it is possible that the changes in hazard are the result of markers having different effect throughout individual's life. There exists substantial evidence that genetic effects on individual's phenotype can vary significantly throughout lifespan. For example, higher ages have been shown to have lower heritabilities across many continous complex traits. 

We develop an extension to the BayesW model to two and three epochs by imposing statistical model and deriving Gibbs updates for interaction parameters and epoch-specific parameters.
