# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

# In both pratical task and Assignment 1
def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE FOR TASK 3 ***"
    # util.raiseNotDefined()
    pqueue = util.PriorityQueue(); counter = util.Counter(); closed = []

    cur_coord = problem.getStartState()
    g_plus_h = 0 + heuristic(cur_coord, problem)
    counter[cur_coord] = g_plus_h
    pqueue.push((cur_coord, []), g_plus_h)

    while not pqueue.isEmpty():
        cur_coord, paths = pqueue.pop()
        if problem.isGoalState(cur_coord):
            return paths
        if cur_coord not in closed:
            closed.append(cur_coord)
            for next_coord, action, cost in problem.getSuccessors(cur_coord):
                g = problem.getCostOfActions(paths+[action])
                h = heuristic(next_coord, problem)
                g_plus_h = g + h
                counter[next_coord] = g_plus_h
                pqueue.push((next_coord, paths+[action]), g_plus_h)



# Extensions Assignment 1
def iterativeDeepeningSearch(problem):
    """Search the deepest node in an iterative manner."""
    "*** YOUR CODE HERE FOR TASK 1 ***"
    # util.raiseNotDefined()
    limit = 0
    while True:
        stack = util.Stack()
        stack.push((problem.getStartState(), [], 0, 0))
        while not stack.isEmpty():
            cur_coord, paths, total_cost, depth = stack.pop()
            if problem.isGoalState(cur_coord):
                return paths
            if depth >= limit:
                continue
            for (next_coord, action, cost) in problem.getSuccessors(cur_coord):
                stack.push((next_coord, paths+[action], total_cost+cost, depth+1))
        limit += 1

def enforcedHillClimbing(problem, heuristic=nullHeuristic):
    """
    Local search with heuristic function.
    You DO NOT need to implement any heuristic, but you DO have to call it.
    The heuristic function is "manhattanHeuristic" from searchAgent.py.
    It will be pass to this function as second arguement (heuristic).
    """
    "*** YOUR CODE HERE FOR TASK 2 ***"
    # util.raiseNotDefined()
    baseline_coord = problem.getStartState()
    paths = []

    while True:
        queue = util.Queue(); closed = []; baseline_h = heuristic(baseline_coord, problem)
        queue.push((baseline_coord, paths, baseline_h))
        while not queue.isEmpty():
            cur_coord, paths, h = queue.pop()
            if cur_coord not in closed:
                closed.append(cur_coord)
                if heuristic(cur_coord, problem) < baseline_h:
                    if problem.isGoalState(cur_coord):
                        return paths
                    baseline_coord = cur_coord
                    break
                for next_coord, action, cost in problem.getSuccessors(cur_coord):
                    queue.push((next_coord, paths+[action], heuristic(next_coord, problem)))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
ids = iterativeDeepeningSearch
ehc = enforcedHillClimbing