# ----------------------------------------------------------------------------
# Copyright (c) 2012-2018, American Gut Project development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from ._version import get_versions
from ._fetch import fetch_amplicon
from ._type import QiitaMetadata
from ._format import QiitaMetadataDirectoryFormat, QiitaMetadataFormat


__version__ = get_versions()['version']
del get_versions


__all__ = ['fetch_amplicon', 'QiitaMetadata',
           'QiitaMetadataDirectoryFormat', 'QiitaMetadataFormat']
