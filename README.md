# Sparse Accelerated Detrending for HRV Analysis

This work represents an optimization of the open-source code from this paper [An advanced detrending method with application to HRV analysis](https://www.psicolibra.it/wp-content/uploads/2013/10/an_advanced_detrending_method_with_application_in_.pdf), which has been widely utilized in the analysis of various physiological signals, such as electrocardiogram (ECG), pulse wave (BVP), and remote photoplethysmography (rPPG). However, due to the algorithm's lack of utilization of sparse matrix solvers, its computational efficiency is suboptimal, with a time complexity of O(n^3). This limitation renders it inefficient for the analysis of long sequences. Through sparse acceleration, this work optimizes the time complexity, reducing it to O(n).

## The Acceleration Ratio of CPU Computation 

For a long sequence with a sampling rate of 30 Hz and a duration of 5 minutes, the computation time was reduced from 60.19 seconds to 23 ms, achieving an acceleration of 2617 times. 

![image](https://github.com/user-attachments/assets/d18ef633-ef35-4506-849a-df403cd88c13)

## Usage Example 
```python
signal = np.random.random((60*30,))

dsig1 = detrend_dense(signal)         # Original dense
dsig2 = detrend(signal)               # Sparse accelerated

max_err = np.max(np.abs(dsig1-dsig2)) # 2.38 e-13
```

## Citation 
```
@ARTICLE{979357,
  author={Tarvainen, M.P. and Ranta-aho, P.O. and Karjalainen, P.A.},
  journal={IEEE Transactions on Biomedical Engineering}, 
  title={An advanced detrending method with application to HRV analysis}, 
  year={2002},
  volume={49},
  number={2},
  pages={172-175},
  abstract={An advanced, simple to use, detrending method to be used before heart rate variability analysis (HRV) is presented. The method is based on smoothness priors approach and operates like a time-varying finite-impulse response high-pass filter. The effect of the detrending on time- and frequency-domain analysis of HRV is studied.},
  keywords={Heart rate variability;Frequency domain analysis;Frequency estimation;Electrocardiography;Detectors;Physics;Filters;Spectral analysis;Autonomic nervous system;Power distribution},
  doi={10.1109/10.979357},
  ISSN={1558-2531},
  month={Feb},}

```
