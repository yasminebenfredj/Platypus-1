==========
Algorithms
==========

All optimization algorithms extend the :class:`Algorithm` class.  The typical
use of an optimization algorithm begins by first creating a new instance of
the algorithm.  Then, :meth:`run` is called to optimize the problem for a given
number of function evaluations.  Finally, the result is read from
:attr:`result`.  For example, optimizing the three-objective DTLZ2 problem with
NSGA-II could be programmed as follows

.. code-block:: python

   from platypus.problems import DTLZ2
   from platypus.algorithms import NSGAII
    
   problem = DTLZ2(3)
    
   algorithm = NSGAII(problem)
   algorithm.run(10000)
    
   result = algorithm.result

.. note::

   The contents of the result is defined by each algorithm.  Some algorithms may
   return a list of solutions, whereas others may return an :class:`Archive`.
   Additionally, the result may include dominated or infeasible solutions.  It
   is therefore good pratice to remove any dominated solutions by calling
   :code:`nondominated(result)`check for feasibility using
   :code:`solution.is_feasible`.
   
The choice of optimization algorithm can greatly affect the solution quality
both in terms of convergence and diversity, the required number of function
evaluations to converge to quality solutions, and the types of problems they
can solve.  Some algorithms may only support real-valued or binary decision
variables, for example.

NSGA-II
-------

.. class:: NSGAII(problem[, population_size[, generator[, selector[, variator]]]])

   An instance of the Nondominated Sorting Genetic Algorithm II (NSGA-II)
   optimization algorithm.  NSGA-II supports problems defined using
   :class:`Real`, :class:`Binary`, or :class:`Permutation` types.

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

.. class:: NSGAIII(problem, divisions[, divisions_inner[, generator[, selector[, variator]]]])

   An instance of the Nondominated Sorting Genetic Algorithm III (NSGA-III)
   optimization algorithm.  NSGA-III extends NSGA-II to using reference points
   to handle many-objective problems.  NSGA-III supports problems defined using
   :class:`Real`, :class:`Binary`, or :class:`Permutation` types.

   :param problem: the problem definition
   :type problem: Problem
   :param divisions: the number of divisions when generating reference points
   :type divisions: int
   :param divisions_inner: when specified, use the two-layered approach for
      generating reference points
   :type divisions_inner: int or None
   :param generator: the generator for initializing the population
   :type generator: Generator
   :param selector: the selector for selecting parents during recombination
   :type selector: Selector
   :param variator: the recombination operator
   :type variator: Variator
   
   .. note::
   
      NSGA-III is designed for many-objective problems.  Its use is discouraged
      on problems with one or two objectives.
      
ε-MOEA
------

.. class:: EpsMOEA(problem, epsilons[, population_size[, generator[, selector[, variator]]]])

   An instance of the steady-state ε-MOEA optimization algorithm.  ε-MOEA
   supports problems defined using :class:`Real`, :class:`Binary`, or
   :class:`Permutation` types.

   :param problem: the problem definition
   :type problem: Problem
   :param epsilons: the ε value used for ε-dominance
   :type divisions: list of floats
   :param population_size: the size of the population
   :type divisions_inner: int
   :param generator: the generator for initializing the population
   :type generator: Generator
   :param selector: the selector for selecting parents during recombination
   :type selector: Selector
   :param variator: the recombination operator
   :type variator: Variator