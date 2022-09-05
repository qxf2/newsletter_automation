#!/bin/bash/env python3

import optparse
from enum import Enum
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
from great_expectations.data_context import DataContext


class Checkpoints(Enum):
    checkpoint10am = []
    checkpoint11am = ['run_ge_tests_11am_checkpoint']
    checkpoint3pm = []


def run_checkpoint(datacontext: DataContext,
                   checkpoint_name : str,
                   batch_request=None,
                   run_name=None) -> CheckpointResult:
    "Run checkpoint"

    return data_context.run_checkpoint(checkpoint_name,
                                       batch_request,
                                       run_name)


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--checkpoint",
                      dest="checkpoint_name",
                      default=None,
                      type="string")
    parser.print_help(f"Pass one of {[checkpoint.name where checkpoint in Checkpoints]} with the --checkpoint param")
    (options, args) = parser.parse_args()
    checkpoint_name = options.checkpoint_name

    if checkpoint_name:
        for checkpoint in Checkpoints[checkpoint_name].value:
            run_checkpoint(checkpoint.datacontext,
                           checkpoint.checkpoint_name,
                           checkpoint.batch_request,
                           checkpoint.run_name)
