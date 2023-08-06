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

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
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
    """
    "*** YOUR CODE HERE ***"
    start=problem.getStartState()
    frontier = util.Stack()       ## lifo stack
    frontier.push(start)
    expanded = []
    came_from={}
    result=[]
    action={}
    visited=[]
    while frontier.isEmpty()==False:
        node = frontier.pop()       ## remove the  top element of the stack
        visited.append(node) ## visit it
        if problem.isGoalState(node):  ## check if its the goal state
            curr = node
            while (curr!= start):           ## if it is backtrack the path
                result.append(action[curr])
                curr = came_from[curr]
            result.reverse()
            return result
        if node not in expanded:         ##insert its not visited children to the stack
            expanded.append(node)
            for child in problem.expand(node):
                if child[0] not in visited:
                    frontier.push(child[0])
                    came_from[child[0]]=node ## what action we will take if we chose this child
                    action[child[0]]=child[1] ## where does this child comes from

    util.raiseNotDefined()






def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    frontier = util.Queue()  #fifo Queue
    frontier.push(start)
    expanded = []
    came_from = {}
    result = []
    action = {}
    visited = []
    while frontier.isEmpty() == False:
        node = frontier.pop() #remove the top element of the Queue
        visited.append(node)
        if problem.isGoalState(node):      #check if it it the goal state
            curr = node
            while (curr != start):                ## if it is backtrack the path
                result.append(action[str(curr)])
                curr = came_from[str(curr)]
            result.reverse()
            return result
        if node not in expanded:
            expanded.append(node)
        for child in problem.expand(node):
            if child[0] not in visited:
                visited.append(child[0]) #we mark every childen as visited and then we push it to the queue
                frontier.push(child[0])
                action[str(child[0])] = child[1] ## what action we will take if we chose this child
                came_from[str(child[0])] = node  ## where does this child comes from


    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    start = problem.getStartState()
    frontier = util.PriorityQueue()
    frontier.push(start, 0)
    expanded = []
    came_from = {}
    result = []
    action = {}
    visited = []
    costsofar = {}
    closed = []
    costsofar[str(start)] = 0
    pushed = []

    while frontier.isEmpty() == False:
        node = frontier.pop()         #remove the top element of the PQueue
        if node not in visited:
            visited.append(node)
            if problem.isGoalState(node):
                curr = node
                while (curr != start):           ## if it is backtrack the path
                    result.append(action[str(curr)])
                    curr = came_from[str(curr)]
                result.reverse()
                return result
            a = list(problem.expand(node))
            for child in a:
                new_cost = costsofar[str(node)] + float(child[2])
                if str(child[0]) not in costsofar.keys() or new_cost < costsofar[str(child[0])]: #if there is no cost registered or better cost is found update the cost
                    costsofar[str(child[0])]=new_cost
                    prio = new_cost + heuristic(child[0], problem)
                    frontier.push(child[0], prio)
                    costsofar[str(child[0])]=new_cost  ## updating cost
                    action[str(child[0])]=child[1] ## what action we will take if we chose this child
                    came_from[str(child[0])]=node ## what action we will take if we chose this child



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
