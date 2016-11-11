"""
Sentiment Dissonance (Utility methods)
======================================

This is a utility file contains helper methods for the workflow.
"""
import json
import os


def delete_file_if_exists(file_name):
    """Delete file if exists.

    Args:
        file_name (str): file name to be deleted.
    """
    if os.path.exists(file_name):
        os.unlink(file_name)


def create_file_if_not_exists(file_name):
    """Create file if not exist.

    Args:
        file_name (str): file name to be created. File will
            be created with an empty dictionary string: {}.
    """
    if not os.path.exists(file_name):
        json.dump({}, open(file_name, 'w'))
