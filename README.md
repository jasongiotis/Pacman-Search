# Pacman-Search
Helping Pacman escape mazes using search algorithms  <br>


![alt text](https://inst.eecs.berkeley.edu/~cs188/sp21/assets/images/maze.png)

<h3> Question 1 : Finding a Fixed Food Dot using Depth First Search </h3> <br>

We can test our implementation by checking different maze sizes (tiny medium big)

suggested test: </br>

```
python pacman.py -l mediumMaze -p SearchAgent
```

also we can test using autograder

```
python autograder.py -q q1
```

<br>

<h3> Question 2 : Breadth First Search</h3> <br>

suggested test:
  
```
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

autograder:

```
python autograder.py -q q2
```

<br>

<h3> Question 3 : A* search </h3> <br>

suggested test (Big maze using Manhattan Distance as Heuristic)

```
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```
autograder:

```
python autograder.py -q q3
```
<br>

<h3> Question 4 : Finding All the Corners</h3> <br>


suggested tiny corners test:
  
```
python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
suggested medium corners test:

```
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```
autograder:

```
python autograder.py -q q4
```

<br>


<h3> Question 5 : Corners Problem with Heuristics</h3> <br>

suggested medium corners test:

```
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```
autograder:

```
python autograder.py -q q5
```


<br>

<h3> Question 6 : Eating All The Dots</h3> <br>

suggested hard search test:

```
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```
autograder:

```
python autograder.py -q q6
```


<br>


<h3> Question 7 : Greedy Search to the nearest dot </h3> <br>

suggested hard search test:

```
python pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```
autograder:

```
python autograder.py -q q7
```


<br>


<h3>test the whole project :</h3>h3>

```
python autograder.py 
```










