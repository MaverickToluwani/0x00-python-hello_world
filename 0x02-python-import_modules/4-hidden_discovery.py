#!/usr/bin/python3
import importlib.util


def non_magic_names(module_name):
    # Load the compiled module
    spec_from_file_location = importlib.util.spec_from_file_location
    spec = spec_from_file_location(module_name, module_name + ".pyc")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # Get all names defined in the module
    module_names = dir(module)
    # Print non-magic names in alphabetical order
    for name in module_names:
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    compiled_module_name = "hidden_4"
    non_magic_names(compiled_module_name)
