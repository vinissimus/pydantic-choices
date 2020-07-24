# Pydantic-Choices

[![Build Status](https://travis-ci.com/vinissimus/pydantic-choices.svg?branch=master)](https://travis-ci.com/vinissimus/pydantic-choices) [![PyPI version](https://badge.fury.io/py/pydantic-choices.svg)](https://badge.fury.io/py/pydantic-choices) ![](https://img.shields.io/pypi/pyversions/pydantic-choices.svg) [![Codcov](https://codecov.io/gh/vinissimus/pydantic-choices/branch/master/graph/badge.svg)](https://codecov.io/gh/vinissimus/pydantic-choices/branch/master) ![](https://img.shields.io/github/license/vinissimus/pydantic-choices)

## How to use

```python
from pydantic_choices import choice

import pydantic as pd


Licenses = choice(["GPL", "GPLv3+", "MIT", "MPL 2.0"])


class Project(pd.BaseModel):
    id: str
    url: str
    license: Licenses


# Validation passes
Project(
    id="pydantic_choices",
    url="https://github.com/vinissimus/pydantic-choices",
    license="MIT",
)

# Validation fails
p1 = Project(
    id="pydantic_choices",
    url="https://github.com/vinissimus/pydantic-choices",
    license="propietary",  # value not in choice
)
```
