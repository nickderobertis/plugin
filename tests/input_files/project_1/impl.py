from typing import Tuple, Dict

from tests.input_files.project_1.spec import MyPluginSpec


class MyPluginImplementation(MyPluginSpec):
    def on_single_arg(self, value: float) -> float:
        return value + 10

    def on_two_args(self, value: float, value2: float) -> Tuple[float, float]:
        return value + 10, value2 + 10

    def on_kwargs(self, value: float = 10) -> Dict[str, float]:
        return dict(value=value + 10)

    def on_args_and_kwargs(self, value: float, value2: float = 10) -> Tuple[float, Dict[str, float]]:
        return value + 10, dict(value2=value2 + 10)

    def on_nothing(self):
        self.should_be_ten = 10