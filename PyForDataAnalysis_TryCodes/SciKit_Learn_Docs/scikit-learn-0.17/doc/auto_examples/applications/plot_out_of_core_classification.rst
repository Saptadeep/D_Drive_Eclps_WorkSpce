

.. _example_applications_plot_out_of_core_classification.py:


======================================================
Out-of-core classification of text documents
======================================================

This is an example showing how scikit-learn can be used for classification
using an out-of-core approach: learning from data that doesn't fit into main
memory. We make use of an online classifier, i.e., one that supports the
partial_fit method, that will be fed with batches of examples. To guarantee
that the features space remains the same over time we leverage a
HashingVectorizer that will project each example into the same feature space.
This is especially useful in the case of text classification where new
features (words) may appear in each batch.

The dataset used in this example is Reuters-21578 as provided by the UCI ML
repository. It will be automatically downloaded and uncompressed on first run.

The plot represents the learning curve of the classifier: the evolution
of classification accuracy over the course of the mini-batches. Accuracy is
measured on the first 1000 samples, held out as a validation set.

To limit the memory consumption, we queue examples up to a fixed amount before
feeding them to the learner.



.. rst-class:: horizontal


    *

      .. image:: images/plot_out_of_core_classification_001.png
            :scale: 47

    *

      .. image:: images/plot_out_of_core_classification_002.png
            :scale: 47

    *

      .. image:: images/plot_out_of_core_classification_003.png
            :scale: 47

    *

      .. image:: images/plot_out_of_core_classification_004.png
            :scale: 47


**Script output**::

  downloading dataset (once and for all) into C:\Users\Mobimedia\scikit_learn_data\reuters
  untarring Reuters dataset...
  done.
  Test set is 878 documents (108 positive)
        NB Multinomial classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.877 in 1.29s (  743 docs/s)
                   SGD classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.911 in 1.30s (  740 docs/s)
            Perceptron classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.912 in 1.30s (  737 docs/s)
    Passive-Aggressive classifier :          962 train docs (   132 positive)    878 test docs (   108 positive) accuracy: 0.908 in 1.31s (  734 docs/s)
  
  
        NB Multinomial classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.885 in 3.72s ( 1052 docs/s)
                   SGD classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.920 in 3.72s ( 1050 docs/s)
            Perceptron classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.946 in 3.73s ( 1049 docs/s)
    Passive-Aggressive classifier :         3911 train docs (   517 positive)    878 test docs (   108 positive) accuracy: 0.958 in 3.73s ( 1048 docs/s)
  
  
        NB Multinomial classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.900 in 6.10s ( 1117 docs/s)
                   SGD classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.956 in 6.11s ( 1116 docs/s)
            Perceptron classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.934 in 6.11s ( 1115 docs/s)
    Passive-Aggressive classifier :         6821 train docs (   891 positive)    878 test docs (   108 positive) accuracy: 0.960 in 6.12s ( 1115 docs/s)
  
  
        NB Multinomial classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.909 in 8.39s ( 1163 docs/s)
                   SGD classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.956 in 8.39s ( 1162 docs/s)
            Perceptron classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.960 in 8.40s ( 1162 docs/s)
    Passive-Aggressive classifier :         9759 train docs (  1276 positive)    878 test docs (   108 positive) accuracy: 0.954 in 8.40s ( 1161 docs/s)
  
  
        NB Multinomial classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.915 in 10.34s ( 1129 docs/s)
                   SGD classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.941 in 10.34s ( 1129 docs/s)
            Perceptron classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.946 in 10.34s ( 1129 docs/s)
    Passive-Aggressive classifier :        11680 train docs (  1499 positive)    878 test docs (   108 positive) accuracy: 0.956 in 10.34s ( 1129 docs/s)
  
  
        NB Multinomial classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.925 in 12.57s ( 1163 docs/s)
                   SGD classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.966 in 12.57s ( 1163 docs/s)
            Perceptron classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.944 in 12.59s ( 1161 docs/s)
    Passive-Aggressive classifier :        14625 train docs (  1865 positive)    878 test docs (   108 positive) accuracy: 0.967 in 12.59s ( 1161 docs/s)
  
  
        NB Multinomial classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.932 in 14.61s ( 1188 docs/s)
                   SGD classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.957 in 14.61s ( 1187 docs/s)
            Perceptron classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.957 in 14.62s ( 1187 docs/s)
    Passive-Aggressive classifier :        17360 train docs (  2179 positive)    878 test docs (   108 positive) accuracy: 0.967 in 14.62s ( 1187 docs/s)



**Python source code:** :download:`plot_out_of_core_classification.py <plot_out_of_core_classification.py>`

.. literalinclude:: plot_out_of_core_classification.py
    :lines: 25-

**Total running time of the example:**  29.55 seconds
( 0 minutes  29.55 seconds)
    