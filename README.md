 Large language models (LLMs) are increasingly used inside synthetic-data pipelines to generate corpora, augment low-resource datasets, and simulate sensitive scenarios. This makes memorization a central trustworthiness concern: if a generator memorizes reproduces parts of its training data, ostensibly synthetic outputs may still leak private or proprietary information. Quantifying such memorization is therefore critical for validating privacy-preserving synthetic data generation and for benchmarking trustworthy data-centric AI systems.

  
  We investigate the empirical relationship between two metrics for quantifying memorization in generative sequence models: Exposure, an empirically successful metric that is widely used in practice and Fisher Information Leakage, a quantity with strong theoretical underpinnings but not tested in the text domain. We conduct a series of experiments to examine how the two measures of memorization compare in terms of their evolution during training, repeated exposure to secret information, and the effect of differential privacy. Although the two metrics align on broad patterns, their differences highlight the need for careful interpretation when using memorization metrics to evaluate privacy risks and to validate trustworthy synthetic data pipelines.

Work accepted for poster presentaion at ACM SynthAI@SIGMOD Workshop 2026. 
[Link for Poster](https://drive.google.com/file/d/1nJGDLRN2pH09AHbQ0ZxO3C84NBJZW1Dl/view?usp=drive_link)
[Link for Paper](https://drive.google.com/file/d/18W5aDEHsGWkLEgfJxiq-yKmnmumBkXHP/view?usp=sharing)
