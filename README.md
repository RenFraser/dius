# Dius Coding Assessment


## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes.

I've decided to take the [Tennis challenge](https://github.com/DiUS/coding-tests/blob/master/dius_tennis.md).

### Prerequisites

- [Python 3.8.9+](https://www.python.org/downloads/)

### Installing

Pytest is the only external library. Use pip to install it.

```shell
pip3 install pytest
```

## Running the Tests

To run the unit tests, use pytest.

```shell
pytest
```


## Running the Code

I've added `main.py` as the main entry point to the project. You'll see the
standard `if __name__ == '__main__'` block that get's executed on invocation of
the file. To run it use:

```shell
python3 main.py
```

It's just a simple demo and check.


# Assumptions
- There are only ever two players to a match. If doubles were played, the team 
names would take the role of "player_one" and "player_two".

# Design Decisions:
- I've implemented test coverage for the happy paths. One thing that's missing
from the implementation is the tie-breaker scoring. The spec's listed the
different system for tie-breaker games. I haven't implemented this and as such
there's no coverage for it. 
- I haven't implemented edge case tests. If I had more time, I would've been
more rigorous with tests.
- I've intentionally left out tests for APIs that we're not that interested in. 
If I were to allocate more time to this assessment, I'd implement unit tests 
for the scoring (`Score.py`) classes.
- I've intentionally tested the public facing APIs and not the private methods.
