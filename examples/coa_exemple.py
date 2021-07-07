from platypus import COA, Problem, Real, truncate_fitness, objective_key, ParticleSwarm, SMPSO
import numpy as np
import optproblems.cec2005 as cec2005

def Sphere(X):
    y = np.sum(X**2)
    return y


def printBestIndividual(self):
    print(self.result)
if __name__=="__main__":
    d = 30
    f = cec2005.F1(d)
    problem = Problem(d ,1 ,nconstrs=0 ,function=f)


    algorithmCOA = COA(problem, n_packs=20, n_coy=5, lb=-100, ub=100, random_seed=1)
    algorithmCOA.run(10000*d)
    """
    problem.types[:] = [Real(-100,100)]*d
    algorithmPSO = ParticleSwarm(problem, swarm_size=100)
    algorithmPSO.run(10000*d)
    """
    print(algorithmCOA.result)
    #print(algorithmPSO.result)