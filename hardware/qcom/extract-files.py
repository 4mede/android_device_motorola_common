#!/usr/bin/env -S PYTHONPATH=../../../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    "vendor/qcom/common/vendor/dsprpcd",
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libdiag',
        'libqmi',
        'libqmi_cci',
        'libqmi_common_so',
        'libqmiservices',
    ): lib_fixup_remove,
}

module = ExtractUtilsModule(
    'qcom',
    'motorola/common/hardware',
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
