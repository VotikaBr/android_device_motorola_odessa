#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_vendorcompat,
    lib_fixups_user_type,
    libs_proto_3_9_1,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/motorola',
    'hardware/qcom-caf/common/libqti-perfd-client',
    'vendor/motorola/sm6150-common',
    'vendor/qcom/opensource/display',
]

# Correções em bibliotecas (caso precise ajustar links de dependência)
lib_fixups: lib_fixups_user_type = {
    libs_proto_3_9_1: lib_fixup_vendorcompat,
}

# Fixes específicos para blobs do odessa (adicione conforme necessário)
blob_fixups: blob_fixups_user_type = {
    # Exemplo de fixup genérico, pode remover se não aplicável ao odessa
    # 'vendor/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so': blob_fixup()
    #     .sig_replace('13 0A 00 94', '1F 20 03 D5'),
}

module = ExtractUtilsModule(
    'odessa',
    'motorola',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6150-common', module.vendor
    )
    utils.run()
