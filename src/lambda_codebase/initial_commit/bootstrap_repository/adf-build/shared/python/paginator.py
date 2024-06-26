# Copyright Amazon.com Inc. or its affiliates.
# SPDX-License-Identifier: MIT-0

"""
Paginator used with certain boto3 calls
when pagination is required
"""


def paginator(method, **kwargs):
    client = method.__self__
    iterator = client.get_paginator(method.__name__)
    for page in iterator.paginate(**kwargs).result_key_iters():
        yield from page
