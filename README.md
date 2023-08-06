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
