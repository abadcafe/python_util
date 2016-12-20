# -*- coding: utf-8 -*-
"""
shell util
"""
from __future__ import print_function
import subprocess
import sys


class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def run_bash_script(script,
                    print_trace=False,
                    return_stdout=False,
                    return_stderr=False,
                    combine_stderr=False):
    """
    run bash script
    :param script: bash script string
    :param print_trace: whether print script and result
    :param return_stdout: return stdout instead of printing
    :param return_stderr: return stderr instead of printing
    :param combine_stderr: redirect stderr to stdout
    :type script: str
    :type print_trace: bool
    :type return_stdout: bool
    :type return_stderr: bool
    :type combine_stderr: bool
    :return: ret_value, stdout, stderr
    :rtype: tuple[int, str, str]
    """
    if print_trace:
        print(Color.WARNING + script + Color.ENDC)
    if return_stdout:
        target_stdout = subprocess.PIPE
    else:
        target_stdout = sys.stdout
    if combine_stderr:
        target_stderr = subprocess.STDOUT
    else:
        if return_stderr:
            target_stderr = subprocess.PIPE
        else:
            target_stderr = sys.stderr

    p = subprocess.Popen("/bin/bash", stdout=target_stdout, stderr=target_stderr,
                         stdin=subprocess.PIPE)
    p.stdin.write(script)
    p.stdin.close()
    ret_value = p.wait()
    ret_stdout = None
    ret_stderr = None
    if return_stdout:
        ret_stdout = bytes.decode(p.stdout.read())
    if return_stderr and not combine_stderr:
        ret_stderr = bytes.decode(p.stderr.read())
    if print_trace:
        if ret_value == 0:
            print(Color.OKGREEN + str(ret_value) + Color.ENDC)
        else:
            print(Color.FAIL + str(ret_value) + Color.ENDC)
        if return_stdout:
            print(ret_stdout)
        if return_stderr and not combine_stderr:
            print(ret_stderr)
    return ret_value, ret_stdout, ret_stderr


# test
print("================= 1 =================")
print(run_bash_script("echo 123"))
print("================= 2 =================")
print(run_bash_script("echo 123 && cp", return_stderr=True, return_stdout=True, print_trace=True))
print("================= 3 =================")
print(run_bash_script("echo 123 && cp", return_stdout=True, return_stderr=True, combine_stderr=True, print_trace=True))
print("================= 4 =================")
print(run_bash_script("echo 123 && cp", return_stdout=True, return_stderr=False, combine_stderr=True, print_trace=True))
print("================= 5 =================")
print(run_bash_script("echo 123 && cp", return_stdout=True, return_stderr=False, print_trace=True))
print("================= 6 =================")
print(run_bash_script("echo 123 && cp", return_stdout=False, return_stderr=True, combine_stderr=True, print_trace=True))
print("================= 7 =================")
print(run_bash_script("echo 123 && cp", return_stdout=False, return_stderr=True, combine_stderr=False, print_trace=True))
print("================= 8 =================")
print(run_bash_script("echo 123 && cp", return_stdout=False, return_stderr=False, combine_stderr=True, print_trace=True))
print("================= 9 =================")
print(run_bash_script("echo 123 && cp", return_stdout=False, return_stderr=False, combine_stderr=False, print_trace=True))
