from pydantic.errors import PydanticTypeError
from pydantic.utils import update_not_none
from typing import Any
from typing import Dict
from typing import List
from typing import Type
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pydantic.typing import CallableGenerator


class ChoiceStrError(PydanticTypeError):
    msg_template = "value not found in choice"


class Choice(str):
    values: List[str]

    def __init__(self, values):
        self.values = values

    @classmethod
    def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
        update_not_none(field_schema, values=cls.values)

    @classmethod
    def __get_validators__(cls) -> "CallableGenerator":
        yield cls.validate

    @classmethod
    def validate(cls, value: str) -> str:
        if value not in cls.values:
            raise ChoiceStrError(missing=value)
        return value


def choice(values: List[str]) -> Type[str]:
    return type("ChoiceStr", (Choice,), dict(values=values))
