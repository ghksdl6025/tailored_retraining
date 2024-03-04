## Empirical results

### Meta-measures: BPIC 2017 log with XGB classifier
| Prefix | Average F1 score  from streaming | Drops | Avg. moving std. | Max. Magnitude | Avg. Magnitude | Recovery rate |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 2 | 0.536 | 54 | 0.074 | 0.418 | 0.115 | 8.556 |
| 7 | 0.690 | 67 | 0.114 | 0.433 | 0.166 | 6.776 |
| 14 | 0.860 | 31 | 0.037 | 0.396 | 0.068 | 13.194 |
<p align="center">
    <img src="./img/empirical results/diff_prefix_length.png">
</p>

### Meta-measures comparison by classifier
| Classifier | Average F1 score  from streaming | Drops | Stability of performance | Max. Magnitude | Avg. Magnitude | Recovery rate |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| HATC | 0.646 | 57 | 0.058 | 0.382 | 0.095 | 5.825 |
| XGB | 0.824 | 72 | 0.082 | 0.431 | 0.123 | 6.653 |
| LSTM | 0.639 | 33 | 0.076 | 0.444 | 0.135 | 9.364 |

<p align="center">
    BPIC2017 with prefix length 10
</p>

| Classifier | Average F1 score  from streaming | Drops | Stability of performance | Max. Magnitude | Avg. Magnitude | Recovery rate |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| HATC | 0.694 | 44 | 0.058 | 0.290 | 0.088 | 6.568 |
| XGB | 0.778 | 44 | 0.113 | 0.347 | 0.152 | 5.455 |
| LSTM | 0.569 | 28 | 0.069 | 0.323 | 0.111 | 8.429 |
<p align="center">
    IRO5K with prefix length 7
</p>

### Meta-measures: Configuration
<p align="center">
    <img src="./img/empirical results/configuration.png"><br>
    
</p>


<h1>
<a href="https://github.com/ghksdl6025/online_ppm_stability/blob/master/result analysis.xlsx">Additional results</a> together with extra performance measurements

(Precision, Recall, Accuracy)
</h1>

