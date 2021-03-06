import sys
import json

input_data = json.loads(sys.stdin.read())
args, kwargs = input_data['args'], input_data['kwargs']
val = args[0]
print(val + 20)