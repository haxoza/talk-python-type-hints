
## What's Type Hints?


## Code Completion


Do you use code completion

in your IDE / code editor?


Let's have a look on PyCharm and Python 2.7

(demo)


PyCharm parses docstrings


![](/img/orly.jpg)

So PHP-ish


### Advantages

* Productivity
* Better code completion
* Early bug findings


### Disadvantages

* More code
* Maintenance
* docstrings - orly?



## Annotations to the rescue!


Python 3 introduces

**functions annotations** syntax

(PEP 3107)


## How does it look like?


```
def compile(source: "something compilable",
            filename: "where the compilable thing comes from",
            mode: "is this a single statement or a suite?"):
    ... 
```


## What does it give us?


### Use cases (from PEP 3107):

* Providing typing information
 * Type checking
 * Let IDEs show what types a function expects and returns
 * Function overloading / generic functions
 * Foreign-language bridges
 * Adaptation
 * Predicate logic functions
 * Database query mapping
 * RPC parameter marshaling
* Other information
 * Documentation for parameters and return values



## Type checking


Jukka Lehtosalo creates **mypy** (2012)


mypy uses function annotation
 
for static type checking


mypy does **not**

run Python code


### Some examples


### Built-in types

```
def greeting(name: str) -> str:
    return 'Hello ' + name
```


### Custom types

```
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)
Vector = Iterable[Tuple[T, T]]

def inproduct(v: Vector) -> T:
    return sum(x*y for x, y in v)
```


Python authors decides to built in

type hinting inspired by mypy


### PEP 484

> PEP 484 intorduces a provisional module to provide these standard definitions and tools, along with some conventions for situations where annotations are not available. 


PEP 484 will be introduced in Python 3.5


### PyCharm

> PyCharm has preliminary support for type hinting using function annotations as specified by PEP 484


Demo - mypy & PyCharm



Resources:

* [PyCharm Type Hinting](https://www.jetbrains.com/pycharm/help/type-hinting-in-pycharm.html)
* [PEP 3107](https://www.python.org/dev/peps/pep-3107/)
* [PEP 484](https://www.python.org/dev/peps/pep-0484/)
* [mypy](http://mypy-lang.org/)


Slides and code:

https://github.com/haxoza/talk-python-type-hints



## Thank you!

Q & A
