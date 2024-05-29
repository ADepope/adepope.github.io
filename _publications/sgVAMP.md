---
layout: default
title: Incorporating summary statistics into VAMP framework
authors: Al Depope
year: 2024
pdf: false
---


## Abstract

Combining genome-wide association studies across genetically diverse cohorts of ancestries can potentially leverage the shared information and increase polygenic risk score portability. Current state-of-the-art cross-ancestry summary statistics methods rely on several regularized linear regressions or variational inference schemes. In contrast, an individual-level method called gVAMP was recently developed based on the approximate message passing framework, which is supposed to be Bayes optimal. gVAMP allows for the joint inference of genetic effects accounting for Bayesian prior while achieving similar performance to the top sampling-based methods in only a fraction of time. In this work, we first adapt gVAMP to the summary statistics setup in order to propose a novel method called summary gVAMP (sgVAMP). We demonstrate that compared to other popular summary statistics methods, sgVAMP achieves state-of-the-art out-of-sample prediction accuracy across several traits in the UK biobank using the 2.17 million SNP set. Secondly, we extend sgVAMP to a multi-cohort setting, which allows for the joint estimation of shared and population-specific signals across multiple ancestries. Finally, we use sgVAMP for the comprehensive joint analysis, combining UK biobank and Estonian biobank datasets using 500K and 200K individuals, respectively.
