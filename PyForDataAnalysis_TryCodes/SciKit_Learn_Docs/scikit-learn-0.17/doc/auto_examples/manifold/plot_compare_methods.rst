

.. _example_manifold_plot_compare_methods.py:


=========================================
 Comparison of Manifold Learning methods
=========================================

An illustration of dimensionality reduction on the S-curve dataset
with various manifold learning methods.

For a discussion and comparison of these algorithms, see the
:ref:`manifold module page <manifold>`

For a similar example, where the methods are applied to a
sphere dataset, see :ref:`example_manifold_plot_manifold_sphere.py`

Note that the purpose of the MDS is to find a low-dimensional
representation of the data (here 2D) in which the distances respect well
the distances in the original high-dimensional space, unlike other
manifold-learning algorithms, it does not seeks an isotropic
representation of the data in the low-dimensional space.



.. image:: images/plot_compare_methods_001.png
    :align: center


**Script output**::

  standard: 0.14 sec
  ltsa: 0.33 sec
  hessian: 0.5 sec
  modified: 0.38 sec
  Isomap: 0.54 sec
  MDS: 3.2 sec
  SpectralEmbedding: 0.12 sec
  t-SNE: 6 sec



**Python source code:** :download:`plot_compare_methods.py <plot_compare_methods.py>`

.. literalinclude:: plot_compare_methods.py
    :lines: 21-

**Total running time of the example:**  11.87 seconds
( 0 minutes  11.87 seconds)
    