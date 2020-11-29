# valueIterationAgents.py
# -----------------------
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


# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent
import collections

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0
        self.runValueIteration()

    def runValueIteration(self):
        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        state_space = self.mdp.getStates()
        i = 0
        while i < self.iterations:
            values_copy = self.values.copy()
            for state in state_space:
                if not self.mdp.isTerminal(state):
                    max_q = -float('inf')
                    for action in self.mdp.getPossibleActions(state):
                        q_value = 0
                        for (next_s, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
                            immediate_reward = self.mdp.getReward(state, action, next_s)
                            future_reward = values_copy[next_s]
                            q_value += prob * (immediate_reward + self.discount * future_reward)
                        if q_value > max_q:
                            max_q = q_value
                    self.values[state] = max_q
            i += 1

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        value = 0
        for (next_s, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
            immediate_reward = self.mdp.getReward(state, action, next_s)
            future_reward = self.values[next_s]
            value += prob * (immediate_reward + self.discount * future_reward)
        return value

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # no such legal action
        if not self.mdp.getPossibleActions(state):
            return None
        actions = self.mdp.getPossibleActions(state)
        max_q = -float('inf'); best_action = None
        for action in actions:
            q_value = self.computeQValueFromValues(state, action)
            if q_value > max_q:
                max_q = q_value
                best_action = action
        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)

class AsynchronousValueIterationAgent(ValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        An AsynchronousValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs cyclic value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 1000):
        """
          Your cyclic value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy. Each iteration
          updates the value of only one state, which cycles through
          the states list. If the chosen state is terminal, nothing
          happens in that iteration.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state)
              mdp.isTerminal(state)
        """
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        state_space = self.mdp.getStates()
        for i in range(self.iterations):
            state = state_space[i % len(state_space)]
            if not self.mdp.isTerminal(state):
                max_q = -float('inf')
                for action in self.mdp.getPossibleActions(state):
                    q_value = 0
                    for (next_s, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
                        immediate_reward = self.mdp.getReward(state, action, next_s)
                        future_reward = self.values[next_s]
                        q_value += prob * (immediate_reward + self.discount * future_reward)
                    if q_value > max_q:
                        max_q = q_value
                self.values[state] = max_q


class PrioritizedSweepingValueIterationAgent(AsynchronousValueIterationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A PrioritizedSweepingValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs prioritized sweeping value iteration
        for a given number of iterations using the supplied parameters.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100, theta = 1e-5):
        """
          Your prioritized sweeping value iteration agent should take an mdp on
          construction, run the indicated number of iterations,
          and then act according to the resulting policy.
        """
        self.theta = theta
        ValueIterationAgent.__init__(self, mdp, discount, iterations)

    def runValueIteration(self):
        "*** YOUR CODE HERE ***"
        pqueue = util.PriorityQueue()
        state_space = self.mdp.getStates()
        predecessor_list = {state: [] for state in state_space}
        # build predecessor dictionary
        for state in state_space:
            if not self.mdp.isTerminal(state):
                for action in self.mdp.getPossibleActions(state):
                    for (next_s, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
                        if state not in predecessor_list[next_s]:
                            predecessor_list[next_s].append(state)

        # push state with priority of -diff into priority queue
        for state in state_space:
            if not self.mdp.isTerminal(state):
                q_value = self.values[state]
                max_q = -float('inf')
                for action in self.mdp.getPossibleActions(state):
                    q = self.getQValue(state, action)
                    if q > max_q:
                        max_q = q
                diff = abs(max_q - q_value)
                pqueue.update(state, -diff)

        for i in range(self.iterations):
            if pqueue.isEmpty():
                return None
            state = pqueue.pop()
            if not self.mdp.isTerminal(state):
                # update q value
                max_q = -float('inf')
                for action in self.mdp.getPossibleActions(state):
                    q_value = 0
                    for (next_s, prob) in self.mdp.getTransitionStatesAndProbs(state, action):
                        immediate_reward = self.mdp.getReward(state, action, next_s)
                        future_reward = self.values[next_s]
                        q_value += prob * (immediate_reward + self.discount * future_reward)
                    if q_value > max_q:
                        max_q = q_value
                self.values[state] = max_q

                # update predecessor
                for p in predecessor_list[state]:
                    if not self.mdp.isTerminal(p):
                        q_value = self.values[p]
                        max_q = -float('inf')
                        for action in self.mdp.getPossibleActions(p):
                            q = self.getQValue(p, action)
                            if q > max_q:
                                max_q = q
                        diff = abs(max_q - q_value)
                        if diff > self.theta:
                            pqueue.update(p, -diff)