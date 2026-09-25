---
title: "About"
layout: page
hide_title: true
description: "Al Depope, PhD — Postdoctoral Researcher at ISTA working on Bayesian inference, approximate message passing and high-performance statistical genetics."
---

<div class="hero">
  <div class="hero-text">
    <h1 class="hero-name">Al Depope</h1>
    <p class="hero-role">Postdoctoral Researcher &middot; Statistical Genetics &amp; Machine Learning</p>
    <p class="hero-affil">Institute of Science and Technology Austria (ISTA) &middot; Klosterneuburg, Austria</p>
    <p class="hero-lede">I build mathematically grounded machine learning for genomics &mdash; Bayesian models and inference procedures that scale to biobank-sized data, and the high-performance code that makes them run.</p>
    <div class="hero-links">
      <a class="pill-link is-primary" href="mailto:al.depope@ist.ac.at">{% include icon.html name="envelope" %} Email</a>
      <a class="pill-link" href="{{ "/cv/" | relative_url }}">{% include icon.html name="file-alt" %} CV</a>
      <a class="pill-link" href="https://github.com/ADepope">{% include icon.html name="github" %} GitHub</a>
      <a class="pill-link" href="https://www.linkedin.com/in/al-depope/">{% include icon.html name="linkedin" %} LinkedIn</a>
      <a class="pill-link" href="https://orcid.org/0000-0001-8583-0609">{% include icon.html name="orcid" %} ORCID</a>
    </div>
  </div>
  <div class="hero-photo-wrap">
    <img class="hero-photo" src="{{ site.portrait | relative_url }}" alt="Portrait of Al Depope" width="760" height="760">
  </div>
</div>

## About me

I am a Postdoctoral Researcher at the [Institute of Science and Technology Austria (ISTA)](https://ista.ac.at), co-affiliated with the [Medical Genomics group](https://ist.ac.at/en/research/robinson-group/) led by Prof. Matthew Robinson and the [Data Science, Machine Learning, and Information Theory group](https://ist.ac.at/en/research/mondelli-group/) led by Prof. [Marco Mondelli](http://marcomondelli.com/index.html). I completed my PhD at ISTA in July 2026, in the same two groups.

My work sits at the intersection of mathematically grounded machine learning, numerical mathematics, software development and genetics. During my doctorate I developed [gVAMP](https://github.com/medical-genomics-group/gVAMP), a family of approximate message passing algorithms for Bayesian inference in very high dimensions, and used it to run the largest joint genome-wide association study to date &mdash; 17 million whole-genome sequence variants analysed jointly, reaching 46% out-of-sample prediction accuracy for human height. The same machinery now carries over to methylation data, proteomic time-to-event models and cross-ancestry polygenic risk scores.

Before ISTA I obtained a BSc in Mathematics and an MSc in Mathematical Statistics from the [Department of Mathematics](https://www.pmf.unizg.hr/math/en), University of Zagreb.

<ul class="tag-row">
  <li class="tag">Bayesian inference</li>
  <li class="tag">Approximate message passing</li>
  <li class="tag">High-dimensional statistics</li>
  <li class="tag">Polygenic risk scores</li>
  <li class="tag">Survival analysis</li>
  <li class="tag">High-performance computing</li>
  <li class="tag">C++ / CUDA / MPI</li>
  <li class="tag">Python &amp; PyTorch</li>
</ul>

<ul class="stat-strip">
  <li class="stat"><b>17M</b><span>WGS variants jointly modelled</span></li>
  <li class="stat"><b>46%</b><span>prediction accuracy for human height</span></li>
  <li class="stat"><b>10&times;</b><span>speed-up over MCMC baselines</span></li>
  <li class="stat"><b>40+</b><span>talks and presentations given</span></li>
</ul>

<div class="section-head">
  <h2 id="current-work">What I am working on</h2>
  <a class="more-link" href="{{ "/research/" | relative_url }}">All projects {% include icon.html name="arrow-right" %}</a>
</div>

<ul class="card-grid">
  <li class="card">
    <span class="card-icon">{% include icon.html name="users" %}</span>
    <h3><a href="https://github.com/ADepope/TLgVAMP">TLgVAMP &mdash; transfer learning across ancestries</a></h3>
    <p>Polygenic risk scores transfer poorly to populations that are under-represented in genomic studies. TLgVAMP borrows strength from large, well-powered cohorts while keeping population-specific signal separate.</p>
    <div class="card-foot">
      <a href="https://github.com/ADepope/TLgVAMP">{% include icon.html name="github" %} Code</a>
    </div>
  </li>
  <li class="card">
    <span class="card-icon">{% include icon.html name="dna" %}</span>
    <h3><a href="https://doi.org/10.1016/j.xgen.2026.101162">gVAMP &mdash; joint modelling of whole-genome sequence data</a></h3>
    <p>An approximate message passing paradigm that fine-maps WGS variants and gene burden scores conditional on all other measured variation genome-wide. Published in <em>Cell Genomics</em>.</p>
    <div class="card-foot">
      <a href="https://doi.org/10.1016/j.xgen.2026.101162">{% include icon.html name="external-link-alt" %} Paper</a>
      <a href="https://github.com/medical-genomics-group/gVAMP">{% include icon.html name="github" %} Code</a>
      <a href="{{ "/gvamp/" | relative_url }}">{% include icon.html name="book" %} Tutorial</a>
    </div>
  </li>
  <li class="card">
    <span class="card-icon">{% include icon.html name="microscope" %}</span>
    <h3><a href="https://github.com/Information-and-learning-for-genomics/Time2EVAMP">vampW &mdash; proteomic survival analysis</a></h3>
    <p>A scalable Bayesian framework for disease onset times. On the UK Biobank Pharma Proteomics dataset it improves onset prediction by 26&ndash;33% relative to penalised Cox and deep-learning baselines.</p>
    <div class="card-foot">
      <a href="https://www.biorxiv.org/content/10.64898/2026.04.30.721585v1">{% include icon.html name="file-pdf" %} Preprint</a>
      <a href="https://github.com/Information-and-learning-for-genomics/Time2EVAMP">{% include icon.html name="github" %} Code</a>
    </div>
  </li>
</ul>

<div class="section-head">
  <h2 id="news">Latest updates</h2>
  <a class="more-link" href="{{ "/publications/" | relative_url }}">All publications {% include icon.html name="arrow-right" %}</a>
</div>

<ul class="timeline">
  <li class="is-new">
    <time datetime="2026-07">July 2026</time>
    <p>I completed my PhD at ISTA and started as a Postdoctoral Researcher in the same institute, continuing to develop <a href="https://github.com/ADepope/TLgVAMP">TLgVAMP</a>, a transfer-learning framework for cross-ancestry polygenic risk scores.</p>
  </li>
  <li class="is-new">
    <time datetime="2026-05">May 2026</time>
    <p>&lsquo;Joint modeling of whole-genome sequencing data for human height via approximate message passing&rsquo; is published in <em>Cell Genomics</em> 6(5):101162. <a href="https://doi.org/10.1016/j.xgen.2026.101162">[DOI]</a></p>
  </li>
  <li>
    <time datetime="2026-05">May 2026</time>
    <p>Our preprint on joint variable selection for omic biomarkers in time-to-event data is posted on bioRxiv. <a href="https://www.biorxiv.org/content/10.64898/2026.04.30.721585v1">[Preprint]</a></p>
  </li>
  <li>
    <time datetime="2026">2026</time>
    <p>&lsquo;Joint Variable Selection in Proteomics Survival Models&rsquo; is accepted at the <em>ICLR Workshop on Machine Learning for Genomics Explorations</em>, joint first-authored with Jakub Bajzik. <a href="https://openreview.net/forum?id=Re1rA204zd">[OpenReview]</a></p>
  </li>
  <li>
    <time datetime="2025-11">November 2025</time>
    <p>&lsquo;Deep eutectic solvent as a solution for polyester/cotton textile recycling&rsquo; appears in <em>Waste Management</em>, an output of a cross-field statistics collaboration with TU Wien. <a href="https://doi.org/10.1016/j.wasman.2025.115177">[DOI]</a></p>
  </li>
  <li>
    <time datetime="2024-11">November 2024</time>
    <p>Started a machine learning and privacy internship at the University of Vienna, building a <a href="https://github.com/ADepope/modular-Lan-MIA">modular library</a> for benchmarking membership inference attacks on large language models.</p>
  </li>
  <li>
    <time datetime="2024-06">June 2024</time>
    <p>Our work extending the gVAMP framework to whole-genome sequence analysis of human height was accepted for an oral presentation at the 7th International Conference of Quantitative Genetics. Our work on the summary-statistics version of gVAMP was accepted as a poster, presented by Jakub Bajzik.</p>
  </li>
  <li>
    <time datetime="2024-04">April 2024</time>
    <p>I presented &lsquo;Inference of Genetic Effects via Approximate Message Passing&rsquo; at <a href="https://2024.ieeeicassp.org">ICASSP 2024</a>. <a href="{{ "/download/ICASSP24_presentation_web.pdf" | relative_url }}">[Slides]</a></p>
  </li>
  <li>
    <time datetime="2024-04">April 2024</time>
    <p><span class="badge is-award">Award</span>Best student presentation at the <a href="https://emgm2024.ista.ac.at">52nd European Mathematical Genetics Meeting</a> in Vienna. <a href="{{ "/download/EMGM24_presentation.pdf" | relative_url }}">[Slides]</a></p>
  </li>
  <li>
    <time datetime="2024-03">March 2024</time>
    <p>The second version of the preprint &lsquo;Light-speed whole genome association testing and prediction via Approximate Message Passing&rsquo; is posted on <a href="https://www.biorxiv.org/content/10.1101/2023.09.14.557703v2">bioRxiv</a>.</p>
  </li>
</ul>

## Beyond research

I hike whenever the calendar allows &mdash; my most recent peak above 4,000 metres was Mauna Kea in Hawaii &mdash; and I run. When there is time, I volunteer by preparing and giving competitive mathematics lectures to gifted students at my [old high school](https://gimnazija-amohorovicica-ri.skole.hr) and at [MNM](https://mnm.hr) summer camps.

<ul class="photo-grid">
{% for photo in site.data.hikes %}
  <li class="photo">
    <img src="{{ "/images/" | append: photo.file | relative_url }}" alt="{{ photo.alt }}" loading="lazy"{% if photo.position %} style="object-position: {{ photo.position }}"{% endif %}>
    {% if photo.caption %}<span class="photo-caption">{{ photo.caption }}</span>{% endif %}
  </li>
{% endfor %}
</ul>
