#!/usr/bin/env python3
import os
import sys
import types
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

# ANSI escape codes for colors
GREEN = "\033[92m"
RED   = "\033[91m"
BLUE  = "\033[34m"
RESET = "\033[0m"

# Paths
SRC_DIR   = "src"
FILENAME  = "main"
SCRIPT    = os.path.join(SRC_DIR, f"{FILENAME}.py")

TEST_DIR  = "test"

BUILD_DIR = "build"
LOG_DIR   = os.path.join(BUILD_DIR, "log")
LOG_PATH  = os.path.join(LOG_DIR, f"{FILENAME}.log")
OUT_DIR   = os.path.join(BUILD_DIR, "out")

def test_src_structure():
    print(">>> Checking project structure...")
    assert os.path.isdir(SRC_DIR), f"{RED}Missing src directory{RESET}"
    assert os.path.isdir(TEST_DIR), f"{RED}Missing test directory{RESET}"
    print(f"{GREEN}Project structure OK{RESET}")

def test_script_exists():
    print(">>> Checking if Python script exists...")
    assert os.path.isfile(SCRIPT), f"{RED}Script not found at {SCRIPT}{RESET}"
    print(f"{GREEN}Script found: {SCRIPT}{RESET}")

def test_log_path_exists():
    print(">>> Checking if log path exists...")
    log_dir = os.path.dirname(LOG_PATH)
    assert os.path.isdir(log_dir), f"{RED}Log directory not found: {log_dir}{RESET}"
    print(f"{GREEN}Log directory OK{RESET}")

def test_log_no_errors():
    print(">>> Checking that log file has no [ERROR] entries...")
    assert os.path.isfile(LOG_PATH), f"{RED}Log file not found at {LOG_PATH}{RESET}"
    with open(LOG_PATH, "r") as f:
        content = f.read()
    assert "[ERROR]" not in content, f"{RED}Log file contains errors:\n{content}{RESET}"
    print(f"{GREEN}Log file contains no errors{RESET}")

def test_output_images_exist():
    print(">>> Checking that output images were generated...")
    real_vs_predicted = os.path.join(OUT_DIR, "real_vs_predicted.png")
    residuals = os.path.join(OUT_DIR, "residuals.png")

    assert os.path.isfile(real_vs_predicted), f"{RED}Missing {real_vs_predicted}{RESET}"
    assert os.path.isfile(residuals), f"{RED}Missing {residuals}{RESET}"

    print(f"{GREEN}Output images generated successfully{RESET}")


def test_run_pipeline_types():
    print(">>> Checking run_pipeline function and variable types...")

    import src.main

    try:
        result = src.main.run_pipeline()
    except Exception as e:
        raise AssertionError(f"{RED}run_pipeline failed: {e}{RESET}")

    # Validar que result sea un dict
    if result is None or not isinstance(result, dict):
        raise AssertionError(f"{RED}run_pipeline did not return a dict{RESET}")

    # Intentar extraer las claves esperadas
    try:
        df = result["df"]
        X = result["X"]
        y = result["y"]
        pipeline = result["pipeline"]
        y_pred = result["y_pred"]
    except KeyError as e:
        raise AssertionError(f"{RED}Missing expected key in result: {e}{RESET}")

    # Validar tipos
    assert isinstance(df, pd.DataFrame), f"{RED}df is not a DataFrame{RESET}"
    assert isinstance(X, pd.DataFrame), f"{RED}X is not a DataFrame{RESET}"
    assert isinstance(y, (pd.Series, np.ndarray)), f"{RED}y is not a Series/ndarray{RESET}"
    assert isinstance(pipeline, Pipeline), f"{RED}pipeline is not a Pipeline{RESET}"
    assert isinstance(y_pred, np.ndarray), f"{RED}y_pred is not a numpy array{RESET}"

    print(f"{GREEN}run_pipeline returned expected types{RESET}")
    print(f"{BLUE}df shape: {df.shape}, X shape: {X.shape}, y length: {len(y)}{RESET}")
    print(f"{BLUE}Pipeline steps: {pipeline.named_steps.keys()}{RESET}")
    print(f"{BLUE}y_pred sample: {y_pred[:5]}{RESET}")

if __name__ == "__main__":
    try:
        test_script_exists()
        test_run_pipeline_types()
        test_log_no_errors()
        test_output_images_exist()
        print(f"\n{GREEN}All tests passed{RESET}")
    except AssertionError as e:
        print(f"{RED}Test failed: {e}{RESET}")
        sys.exit(1)