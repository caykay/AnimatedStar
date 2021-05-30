# Star Animation with python Turtle
A python program that simulates simple animation of a star.
The star begins with a set size (length of each side) and keeps rotating around the center of the Turtle screen while 
its length decreasing

## Installation
Use the clone link provided, to clone this project.
```bash
git clone given-link
```
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all required packages/modules.

```bash
pip install -r requirements.txt
```

## Changing the star size
To change the star size, the initial length needs to be adjusted.

To do this, simply specify the initial length as an argument in the _animation_ function
```python
from main import animation
animation(400)
```

## Changing the number of rounds
You can alter the number of times the star is animated
by including another argument called rounds by default _rounds = 10_
```python
# Example
from main import animation
animation(size=400, rounds=20)
```

## Animation example
| At start      | At end      |
|------------|-------------|
|![Start image](images/start.png)|![End image](images/end.png)|
