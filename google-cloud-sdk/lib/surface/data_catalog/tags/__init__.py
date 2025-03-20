# -*- coding: utf-8 -*- #
# Copyright 2019 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Manage tags in Data Catalog."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.calliope import base


@base.Deprecate(
    is_removed=False,
    warning=(
        'This command is deprecated. '
        'Please use `gcloud dataplex entries` instead. '
        'Note that aspects - successors of tags - are part of the entry '
        'resource and are managed by `gcloud dataplex entries` command.'
    ),
    error=(
        'This command has been removed. '
        'Please use `gcloud dataplex entries` instead. '
        'Note that aspects - successors of tags - are part of the entry '
        'resource and are managed by `gcloud dataplex entries` command.'
    ),
)
@base.ReleaseTracks(base.ReleaseTrack.BETA, base.ReleaseTrack.ALPHA,
                    base.ReleaseTrack.GA)
@base.DefaultUniverseOnly
class Tags(base.Group):
  """Manage tags in Data Catalog."""
  pass
