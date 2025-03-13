import numpy as np
from scipy.sparse import spdiags, diags, eye
from scipy.sparse.linalg import spsolve 

def detrend_dense(signal, Lambda=50):
    """detrend(signal, Lambda) -> filtered_signal
    This code is based on the following article "An advanced detrending method with application
    to HRV analysis". Tarvainen et al., IEEE Trans on Biomedical Engineering, 2002.
    """
    signal_length = signal.shape[0]
    H = np.identity(signal_length)
    ones = np.ones(signal_length)
    minus_twos = -2 * np.ones(signal_length)
    diags_data = np.array([ones, minus_twos, ones])
    diags_index = np.array([0, 1, 2])
    D = spdiags(diags_data, diags_index, (signal_length - 2), signal_length).toarray()
    filtered_signal = np.dot((H - np.linalg.inv(H + (Lambda ** 2) * np.dot(D.T, D))), signal)
    return filtered_signal

def detrend(signal, Lambda=50):
    """The optimized detrend utilizes sparse matrix acceleration."""
    signal_length = signal.shape[0]
    
    diags_data = [
        np.ones(signal_length - 2),
        -2 * np.ones(signal_length - 2),
        np.ones(signal_length - 2)
    ]
    offsets = [0, 1, 2]
    D = diags(diags_data, offsets, shape=(signal_length-2, signal_length), format='csc')
    H = eye(signal_length, format='csc')
    DTD = D.T @ D 
    A = H + (Lambda ** 2) * DTD
    x = spsolve(A, signal)
    filtered_signal = signal - x
    
    return filtered_signal
