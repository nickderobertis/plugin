from typing import Tuple, Any, Dict, Optional

from plugin import Plugin


class ChainPlugin(Plugin):
    def execute(
        self,
        method_name: str,
        args: Optional[Tuple[Any, ...]] = None,
        kwargs: Optional[Dict[str, Any]] = None,
    ):
        for handler in self.handlers:
            method = getattr(handler, method_name)
            if args is None and kwargs is None:
                method()
            elif args is not None and kwargs is None:
                args = method(*args)
            elif args is None and kwargs is not None:
                kwargs = method(**kwargs)
            else:
                # args is not None and kwags is not None
                args, kwargs = method(*args, **kwargs)

        if args is None and kwargs is None:
            return
        elif args is not None and kwargs is None:
            return args
        elif args is None and kwargs is not None:
            return kwargs
        else:
            # args is not None and kwags is not None
            return args, kwargs

