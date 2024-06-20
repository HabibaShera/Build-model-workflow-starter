#!/usr/bin/env python
"""
Performs basic cleaning on the data and save the results in Weights & Biases
"""
import argparse
import logging
import wandb


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):

    run = wandb.init(job_type="basic_cleaning")
    run.config.update(args)

    # Download input artifact. This will also log that this script is using this
    # particular version of the artifact
    # artifact_local_path = run.use_artifact(args.input_artifact).file()

    ######################
    # YOUR CODE HERE     #
    ######################


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="his steps cleans the data")


    parser.add_argument(
        "--parameter1", 
        type=float## INSERT TYPE HERE: str, float or int,
        help="first parameter"## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--parameter2", 
        type=float## INSERT TYPE HERE: str, float or int,
        help="second paramter"## INSERT DESCRIPTION HERE,
        required=True
    )

    parser.add_argument(
        "--parameter3", 
        type=str## INSERT TYPE HERE: str, float or int,
        help="third parameter"## INSERT DESCRIPTION HERE,
        required=True
    )


    args = parser.parse_args()

    go(args)
