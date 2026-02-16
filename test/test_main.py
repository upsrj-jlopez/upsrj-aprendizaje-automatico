#!/usr/bin/env python3
import subprocess
import os
import sys
import re

# ANSI escape codes for colors
GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[34m"
RESET = "\033[0m"

# Paths
SRC_DIR = "src"
FILENAME = "main"
SCRIPT    = os.path.join(SRC_DIR, f"{FILENAME}.py")
LOG_PATH  = os.path.join("build", "log", f"{FILENAME}.log")


def run_cmd(cmd, cwd=None, input_data=None):
    """Run a shell command and return (exit_code, stdout, stderr)."""
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            shell=True,
            input=input_data,
            capture_output=True,
            text=True
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)

def test_script_exists():
    print(">>> Checking if Python script exists...")
    assert os.path.isfile(SCRIPT), f"{RED}Script not found at {SCRIPT}{RESET}"
    print(f"{GREEN}Script found: {SCRIPT}{RESET}")

def test_log_exists_and_content():
    print(">>> Checking if log file exists and has content...")
    assert os.path.isfile(LOG_PATH), f"{RED}Log file not found at {LOG_PATH}{RESET}"
    with open(LOG_PATH, "r") as f:
        content = f.read().strip()
    assert content, f"{RED}Log file is empty{RESET}"
    print(f"{GREEN}Log file OK{RESET}")
    print(f"{BLUE}Log content:\n{content}{RESET}")

def test_code_functionality(test_input: str = None, iteration: int = 0, expected: str = None):
    """Black-box test: checks that expected result strings appear in output"""
    print(f">>> Testing program functionality (black-box) — case {iteration}")

    code, out, err = run_cmd(f"python3 {SCRIPT}", input_data=f"{test_input}\n")

    if err:
        print("stderr:", err)

    assert code == 0, f"{RED}Program execution failed{RESET}"
    assert expected == out, (
        f"{RED}Unexpected output (case {iteration}):\n"
        f"Expected to find:\n{expected}\n"
        f"Got:\n{out}{RESET}"
    )

    print(f"{GREEN}Case {iteration} OK{RESET}")

if __name__ == "__main__":
    try:
        testcases = {
            1: f"Hello World!\n"
        }
        test_script_exists()
        test_log_exists_and_content()
        for i, (id, expected) in enumerate(testcases.items()):
            test_code_functionality(id, i, expected)
        print(f"\n{GREEN}All tests passed{RESET}")
    except AssertionError as e:
        print(f"{RED}Test failed: {e}{RESET}")
        sys.exit(1)
