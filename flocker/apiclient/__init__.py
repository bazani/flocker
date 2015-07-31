# Copyright ClusterHQ Inc.  See LICENSE file for details.

"""
Client for the Flocker REST API.

This may eventually be a standalone package.
"""

from ._client import (
    IFlockerAPIV1Client, FakeFlockerAPIV1, Dataset, DatasetState,
)

__all__ = ["IFlockerAPIV1Client", "FakeFlockerAPIV1", "Dataset",
           "DatasetState"]
