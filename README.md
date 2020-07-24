# Pydantic-Choices

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
