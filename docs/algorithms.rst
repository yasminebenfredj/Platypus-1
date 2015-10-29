==========
Algorithms
==========

NSGA-II
-------

.. class:: NSGAII(problem[, population_size[, generator[, selector[, variator]]]])

   An instance of the Nondominated Sorting Genetic Algorithm II (NSGA-II)
   optimization algorithm.  Call :meth:`run` to optimize the problem and read
   the results from :attr:`result`.

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
   
**Example**

    from platypus.problems import DTLZ2
    from platypus.algorithms import NSGAII
    
    problem = DTLZ2(3)
    
    algorithm = NSGAII(problem)
    algorithm.run(10000)
    
    result = algorithm.result

NSGA-III
--------

.. autofunction:: platypus.algorithms.NSGAIII