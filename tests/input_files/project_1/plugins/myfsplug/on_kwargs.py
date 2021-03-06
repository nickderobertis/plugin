# This section only needed due to project structure
import sys
from pathlib import Path
project_root = Path(__file__).parent.parent.parent.parent.parent.parent
sys.path.insert(0, str(project_root.resolve()))

# Start of actual script
from plugin import load_args_kwargs, output_args_kwargs

args, kwargs = load_args_kwargs()
kwargs['value'] += 20
output_args_kwargs(**kwargs)