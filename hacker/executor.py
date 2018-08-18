"""
This module will help to run the program and in child process
and passes the test cases to the module, when requested by the module
"""
import subprocess
import sys
import os


def __call_module(fil, py_mod):
    """
    :param fil: test file
    :param py_mod: python module
    :return: None
    """
    child = subprocess.Popen(['python', py_mod], stdin=subprocess.PIPE, bufsize=1)
    with open(fil) as f:
        p = f.readline().split("\\n")
        if p[-1] == '':
            p.pop(-1)
        child.communicate("\n".join(p).encode())


def execute(py_mod, test_f, find_test=False):
    """
    :param py_mod:python module to execute
    :param test_f: list of test files, or test file starting string with find_test as True
    :param find_test: if True , it tries to find all test files in the current directory starting
    with test_f string
    :return: None
    """
    if find_test:
        for files in os.listdir(os.getcwd()):
            if not files.startswith(test_f):
                continue
            else:
                __call_module(files, py_mod)
    else:
        for files in test_f:
            __call_module(files, py_mod)


if __name__ == '__main__':
    """
    This will help when it runs directly
    """
    if len(sys.argv) > 1:
        python_file = sys.argv[1]
        test_files = sys.argv[2:]
        if len(test_files) == 1 and test_files[-1] == '*':
            find_tests = True
        else:
            find_tests = False
        execute(python_file, test_files, find_tests)
    else:
        print("Execute with another file and test files")
