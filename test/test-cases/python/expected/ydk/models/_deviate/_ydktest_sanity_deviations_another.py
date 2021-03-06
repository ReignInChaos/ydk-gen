
from enum import Enum
from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION
from ydk.models import _yang_ns


_deviation_table = {
    'Runner.NotSupported1.NotSupported12' : {
        'deviation_typ' : 'not_supported',
    },
    'Runner.NotSupported1.not_supported_leaf' : {
        'deviation_typ' : 'not_supported',
    },
    'Runner.NotSupported2' : {
        'deviation_typ' : 'not_supported',
    },
    'Runner.Ytypes.BuiltInT.llstring' : {
        'deviation_typ' : 'add',
        'keyword_value' : [
            ('max_elements', 7),
            ('min_elements', 0),
        ]
    },
}
