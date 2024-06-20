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

    # Example code: you should replace this with your actual data cleaning logic
    logger.info(f"Starting data cleaning with parameters: {args}")

    # Replace this with your actual data cleaning code
    cleaned_data = {}  # Your actual data cleaning output

    # Log the cleaned data to W&B
    wandb.log({"cleaned_data": cleaned_data})

    logger.info("Data cleaning completed.")
    run.complete()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script performs basic data cleaning and logs results to Weights & Biases.")

    parser.add_argument(
        "--parameter1",
        type=float,
        help="First parameter (insert description here)",
        required=True
    )

    parser.add_argument(
        "--parameter2",
        type=float,
        help="Second parameter (insert description here)",
        required=True
    )

    parser.add_argument(
        "--parameter3",
        type=str,
        help="Third parameter (insert description here)",
        required=True
    )

    args = parser.parse_args()

    go(args)
