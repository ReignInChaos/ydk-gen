


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'WithDefaultsModeEnum' : _MetaInfoEnum('WithDefaultsModeEnum', 'ydk.models.ietf.ietf_netconf_with_defaults',
        {
            'report-all':'REPORT_ALL',
            'report-all-tagged':'REPORT_ALL_TAGGED',
            'trim':'TRIM',
            'explicit':'EXPLICIT',
        }, 'ietf-netconf-with-defaults', _yang_ns._namespaces['ietf-netconf-with-defaults']),
}
