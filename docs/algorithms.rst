==========
Algorithms
==========

NSGA-II
-------

.. class:: NSGAII(problem[, population_size, generator, selector, variator])

   Creates a new instance of the Nondominated Sorting Genetic Algorithm II.

   :param problem: the problem definition
   :type problem: Problem
   :param population_size: the size of the population
   :type population_size: int
   :param generator: the generator for initializing the population
   :type generator: Generator
   :param selector: the selector for selecting parents during recombination
   :type selector: Selector
   :param variator: the recombination operator
   :type variator: Variator

NSGA-III
--------

.. autofunction:: platypus.algorithms.NSGAIII