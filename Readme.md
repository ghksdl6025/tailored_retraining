# Exploring the Performance Dynamics of Online Predictive Process Monitoring using Log Features

## Abstract
Predictive process monitoring is essential for forecasting on-going process outcomes. However, in practical online settings fluctuations of prediction performance are problematic. While existing research addresses performance drifts or stability measures, understanding the underlying causes of these fluctuations remains limited. This study aims to fill this knowledge gap by investigating factors contributing to performance variability in prediction models for online process outcome predictions. Through an analysis of log features and their correlation with model performance over time, insights are provided to inform strategies for mitigating performance drops and enhancing model reliability. Our results show a high correlation between log features and the model performance in many cases. Retraining the prediction models based on these insights shows accordingly shows improvement in both average performance and stability. Understanding these factors enables the development of resilient models and tailored retraining strategies, avoiding unnecessary retraining, energy consumption, and costs.

## Method

<p align="center">
    <img src="./readme_img/procedure_method.jpg" style="margin: 0px 0px 10px 0px">
</p>


## Log features
__1. Variant coverage__
This feature measures the appearance of newly observed variants in the test data, which were not included during model training.

<p align="center">
    <img src="./readme_img/formula/variant_coverage.png" style="margin: 0px 0px 10px 0px">
</p>

__2. Label distribution__
This log feature measures the appearance of newly observed categorical event-level attributes in the test data.

<p align="center">
    <img src="./readme_img/formula/label_distribution.png" style="margin: 0px 0px 10px 0px">
</p>


__3. Event level attributes coverage__
This log feature measures the appearance of newly observed categorical event-level attributes in the test data.

<p align="center">
    <img src="./readme_img/formula/event_level_attribute_coverage.png" style="margin: 0px 0px 10px 0px">
</p>

## [Results](./results.md "Results") 
