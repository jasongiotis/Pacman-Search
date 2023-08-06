# Pacman-Search
helping Pacman escape mazes using search algorithms  <br>

<h3> Question 1 : Finding a Fixed Food Dot using Depth First Search </h3> <br>

We can test our implementation by checking different maze sizes (tiny medium big)
```
python pacman.py -p ReflexAgent -l testClassic
```
```
python pacman.py -l mediumMaze -p SearchAgent
```
```
python pacman.py -l bigMaze -z .5 -p SearchAgent
```
also we can test using autograder

```
python autograder.py -q q1
```

<br>

<h3> Question 2 : Breadth First Search</h3> <br>

medium maze test:
  
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```
big maze test:

```
python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5
```
autograder:

```
python autograder.py -q q2
```

<br>

<h3> Question 3 : A* search </h3> <br>

test whith manhattan Heuristic

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
autograder:

```
python autograder.py -q q3
```
<br>

<h3> Question 4 : Finding All the Corners</h3> <br>


tiny corners test:
  
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
medium corners test:

```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
autograder:

```
python autograder.py -q q4
```

<br>







