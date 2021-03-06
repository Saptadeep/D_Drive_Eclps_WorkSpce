

.. _example_ensemble_plot_forest_importances.py:


=========================================
Feature importances with forests of trees
=========================================

This examples shows the use of forests of trees to evaluate the importance of
features on an artificial classification task. The red bars are the feature
importances of the forest, along with their inter-trees variability.

As expected, the plot suggests that 3 features are informative, while the
remaining are not.



.. image:: images/plot_forest_importances_001.png
    :align: center


**Script output**::

  Feature ranking:
  1. feature 1 (0.295902)
  2. feature 2 (0.208351)
  3. feature 0 (0.177632)
  4. feature 3 (0.047121)
  5. feature 6 (0.046303)
  6. feature 8 (0.046013)
  7. feature 7 (0.045575)
  8. feature 4 (0.044614)
  9. feature 9 (0.044577)
  10. feature 5 (0.043912)



**Python source code:** :download:`plot_forest_importances.py <plot_forest_importances.py>`

.. literalinclude:: plot_forest_importances.py
    :lines: 13-

**Total running time of the example:**  0.53 seconds
( 0 minutes  0.53 seconds)
    