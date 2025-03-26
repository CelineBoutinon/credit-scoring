# credit-scoring documentation!

## Description

OpenClassrooms Data Scientist Project 7 - Implement a Credit Scoring Model

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `aws s3 sync` to recursively sync files in `data/` up to `s3://s3://sagemaker-ocds-p7/data/`.
* `make sync_data_down` will use `aws s3 sync` to recursively sync files from `s3://s3://sagemaker-ocds-p7/data/` to `data/`.


