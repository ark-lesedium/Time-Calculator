# This entrypoint file to be used in development. Start by reading README.md
from time_calculator import add_time
from unittest import main


print(add_time("11:30 AM", "2:32", "Monday"))


# Run unit tests automatically
main(module='test_module', exit=False)