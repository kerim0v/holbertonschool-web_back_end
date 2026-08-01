#!/usr/bin/python3
"""Module for calculating pagination index ranges."""


def index_range(page, page_size):
    """asdadd"""
    start_index = (page - 1) * page_size
    end_i = start_index + page_size
    return (start_index, end_i)
