---
layout: page
title: Transfer learning for cross-ancestry polygenic risk scores
authors: Al Depope, Marco Mondelli and Matthew R. Robinson
year: 2026
order: 60
pdf: false
teaser: TLgVAMP_small.svg
status: Work in progress
code: https://github.com/ADepope/TLgVAMP
summary: TLgVAMP extends the gVAMP framework with transfer learning, so that a polygenic risk score fitted in a large, well-powered cohort can inform inference in a smaller cohort from an under-represented population without washing out population-specific signal.
---

## Abstract

Polygenic risk scores are overwhelmingly derived from cohorts of European ancestry, and they transfer poorly to the populations that are under-represented in genomic studies. That gap is a practical fairness problem: the people least represented in the training data are the ones for whom prediction works worst.

TLgVAMP is a transfer-learning extension of the [gVAMP](https://github.com/medical-genomics-group/gVAMP) framework. The idea is to let inference in a small target cohort borrow strength from a large source cohort through a shared prior structure, while keeping population-specific effects identifiable rather than shrinking them towards the source. Because the underlying algorithm is approximate message passing, the amount of information transferred can be tracked through state evolution instead of being fixed by hand.

This is my main line of work as a postdoc. The implementation is being developed in the open at [github.com/ADepope/TLgVAMP](https://github.com/ADepope/TLgVAMP).
