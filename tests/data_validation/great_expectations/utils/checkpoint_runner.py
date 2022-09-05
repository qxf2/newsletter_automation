#!/bin/bash/env python3

import optparse
from enum import Enum
from great_expectations.checkpoint.types.checkpoint_result import CheckpointResult
from great_expectations.data_context import DataContext


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
                      type="string")

