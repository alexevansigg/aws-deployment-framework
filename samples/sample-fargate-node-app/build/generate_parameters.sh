#!/usr/bin/env bash

# Copyright Amazon.com Inc. or its affiliates.
# SPDX-License-Identifier: Apache-2.0

set -e

aws s3 cp s3://$S3_BUCKET_NAME/adf-build/ adf-build/ --recursive --quiet
pip install -r adf-build/requirements.txt -q
python adf-build/generate_params.py
