#!/bin/bash/env python3

import argparse
from enum import Enum
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
from great_expectations.data_context import DataContext

import run_ge_tests_11am_checkpoint


class Checkpoints(Enum):
    checkpoint10am = []
    checkpoint11am = [run_ge_tests_11am_checkpoint]
    checkpoint3pm = []


def run_checkpoint(data_context: DataContext,
                   checkpoint_name : str,
                   batch_request=None,
                   run_name=None) -> CheckpointResult:
    "Run checkpoint"

    result = data_context.run_checkpoint(checkpoint_name,
                                       batch_request,
                                       run_name)
    if not result['success']:
        print('Validation Failed!')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--checkpoint",
                        dest="checkpoint_name",
                        default=None,
                        help =f"Pass one of {[checkpoint.name for checkpoint in Checkpoints]} with the --checkpoint param")
    args = parser.parse_args()
    checkpoint_name = args.checkpoint_name

    if checkpoint_name:
        for checkpoint in Checkpoints[checkpoint_name].value:
            run_checkpoint(checkpoint.data_context,
                           checkpoint.checkpoint_name,
                           checkpoint.batch_request,
                           checkpoint.run_name)
