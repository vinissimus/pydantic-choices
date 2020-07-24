from pydantic_choices import choice

import pydantic as pd
import pytest

Licenses = choice(["GPL", "GPLv3+", "MIT", "MPL 2.0"])


class Project(pd.BaseModel):
    id: str
    url: str
    license: Licenses


def test_validate_choice_fails():
    with pytest.raises(pd.ValidationError) as excinfo:
        Project(
            id="pydantic_choices",
            url="https://github.com/vinissimus/pydantic-choices",
            license="propietary",
        )

    assert excinfo.value.errors() == [
        {
            "loc": ("license",),
            "msg": "value not found in choice",
            "type": "type_error.choicestr",
            "ctx": {"missing": "propietary"},
        }
    ]


def test_validate_choice_works():
    p = Project(
        id="pydantic_choices",
        url="https://github.com/vinissimus/pydantic-choices",
        license="MIT",
    )
    assert p.license == "MIT"
