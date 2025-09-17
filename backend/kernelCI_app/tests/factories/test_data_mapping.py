"""
Centralized mapping of test data expected by integration tests.
This ensures consistency across all factories and eliminates random failures.
"""

from datetime import datetime, timezone

# Tree test data mappings - based on integration tests
TREE_TEST_DATA = {
    "a1c24ab822793eb513351686f631bd18952b7870": {  # ARM64_TREE
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux.git",
        "git_branch": "for-kernelci",
        "tree_name": "arm64",
    },
    "ef143cc9d68aecf16ec4942e399e7699266b288f": {  # ANDROID_MAINLINE_TREE
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android-mainline",
        "tree_name": "android",
    },
    "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba": {  # ANDROID_MAESTRO_MAINLINE
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android-mainline",
        "tree_name": "android",
    },
    "33040a50cdaec186c13ef3f7b9c9b668d8e32637": {  # NEXT_PENDING_FIXES_BROONIE
        "origin": "broonie",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git",
        "git_branch": "pending-fixes",
        "tree_name": "next",
    },
    "4b60a3c25e8793adfb1d92f8e4888321ae416fed": {  # BROONIE_MISC_BROONIE
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/broonie/misc.git",
        "git_branch": "for-kernelci",
        "tree_name": "broonie-misc",
    },
    "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e": {  # ALLWINNER_HARDWARE
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux.git",
        "git_branch": "for-kernelci",
        "tree_name": "arm64",
    },
    "0704a15b930cf97073ce091a0cd7ad32f2304329": {  # ALLWINNER_HARDWARE
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux.git",
        "git_branch": "for-kernelci",
        "tree_name": "arm64",
    },
    "fb482243c16ebfe8776fcd52223351b4061c1729": {  # INVALID_QUERY_PARAMS
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android-mainline",
        "tree_name": "android",
    },
    "google_juniper_checkout_001": {  # google_juniper_checkout_001
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
        "git_branch": "master",
        "tree_name": "mainline",
    },
    "amlogic_checkout_001": {  # amlogic_checkout_001
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/amlogic/linux.git",
        "git_branch": "master",
        "tree_name": "amlogic",
    },
    "7e39477098b50156535c8f910fee50d6dac2a793": {  # android11-5.4
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android11-5.4",
        "tree_name": "android",
    },
    "4fd7634f32ffbb4fd4c09b757aa16327626a1749": {  # android12-5.10
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android12-5.10",
        "tree_name": "android",
    },
    "f72ba1ba267f4c42adb82037e8614d7844badeb9": {  # android12-5.10-lts
        "origin": "maestro",
        "git_url": "https://android.googlesource.com/kernel/common",
        "git_branch": "android12-5.10-lts",
        "tree_name": "android",
    },
    "fluster_checkout_001": {
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
        "git_branch": "master",
        "tree_name": "mainline",
    },
    "arm_juno_checkout_001": {
        "origin": "maestro",
        "git_url": "https://git.kernel.org/pub/scm/linux/kernel/git/arm64/linux.git",
        "git_branch": "for-kernelci",
        "tree_name": "arm64",
    },
}

# Issue test data with specific build/test mappings
# If an issue is in this dictionary, it should have incidents
# No need for has_incidents field - presence in dict implies it should have incidents
ISSUE_TEST_DATA = {
    "maestro:2ff8fe94f6d53f39321d4a37fe15801cedc93573": {
        "version": 1,
        "build_ids": ["maestro:67b62592f7707533c0ff7a95"],  # Only this specific build
    },
    "maestro:87244933628a2612f39e6096115454f1e8bb3e1c": {
        "version": 0,
        "build_ids": [
            "maestro:dummy_67cb759a180183719578307e_x86_64"
        ],  # Only this specific build
    },
    "maestro:ee1cba21ee3fe47f21061725de689b638a9c431a": {
        "version": 1,
        "build_ids": ["maestro:67ce32e418018371957d36b1"],  # Only this specific build
    },
    "maestro:cb38e75d16f267781d5b085b9b2dbb390e2885c4": {
        "version": 1,
        "build_ids": ["redhat:1701576995-x86_64-kernel"],  # Only this specific build
    },
    "maestro:ae160f6f27192c3527b2e88faba35d85d27c285f": {
        "version": 1,
        "test_ids": [
            "test_issue_test",
            "maestro:67bd70e6323b35c54a8824a0",  # This test will be created by TestFactory with FAIL status
        ],
    },
    "maestro:e602fca280d85d8e603f7c0aff68363bb0cd7993": {
        "version": 0,
        "build_ids": [],  # Can be used by any build that needs it
    },
    "broonie:bb2eb9603973cb353faa8e780b304d3537220228": {
        "version": 0,
        "build_ids": [],  # Can be used by any build that needs it
    },
    "linaro:30MeoIqiN9rKm6s2lQLaThEnGHF": {
        "version": 0,
        "build_ids": [],  # Can be used by any build that needs it
    },
}

# Specific build IDs expected by buildDetails_test.py
EXPECTED_BUILD_IDS = {
    "maestro:67b62592f7707533c0ff7a77": {
        "checkout_id": "ef143cc9d68aecf16ec4942e399e7699266b288f",  # ANDROID_MAINLINE_TREE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "maestro:67b62592f7707533c0ff7a99": {
        "checkout_id": "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "maestro:67b62592f7707533c0ff7a95": {
        "checkout_id": "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "FAIL",
        "config_name": "defconfig",
    },
    "maestro:67b62592f7707533c0ff7a94": {
        "checkout_id": "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "FAIL",
        "config_name": "defconfig",
    },
    "maestro:dummy_67cb759a180183719578307e_x86_64": {
        "checkout_id": "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba",  # ANDROID_MAESTRO_MAINLINE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "FAIL",
        "config_name": "defconfig",
    },
    "maestro:67ce32e418018371957d36b1": {
        "checkout_id": "33040a50cdaec186c13ef3f7b9c9b668d8e32637",  # NEXT_PENDING_FIXES_BROONIE
        "origin": "broonie",
        "architecture": "arm64",
        "status": "FAIL",
        "config_name": "defconfig",
    },
    "redhat:1701576995-x86_64-kernel": {
        "checkout_id": "4b60a3c25e8793adfb1d92f8e4888321ae416fed",  # BROONIE_MISC_BROONIE
        "origin": "maestro",
        "architecture": "x86_64",
        "status": "FAIL",
        "config_name": "defconfig",
    },
    "google_juniper_build_valid": {
        "checkout_id": "google_juniper_checkout_001",
        "origin": "maestro",
        "architecture": "google,juniper",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "allwinner_build_valid": {
        "checkout_id": "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e",  # ALLWINNER_HARDWARE
        "origin": "maestro",
        "architecture": "allwinner,sun50i-a64",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "allwinner_build_valid_2": {
        "checkout_id": "0704a15b930cf97073ce091a0cd7ad32f2304329",  # ALLWINNER_HARDWARE
        "origin": "maestro",
        "architecture": "allwinner,sun50i-a64",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "arm_juno_build_valid": {
        "checkout_id": "arm_juno_checkout_001",
        "origin": "maestro",
        "architecture": "arm,juno",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "aaeon_build_valid": {
        "checkout_id": "aaeon_checkout_001",
        "origin": "maestro",
        "architecture": "i386",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "asus_build_valid": {
        "checkout_id": "asus_checkout_001",
        "origin": "maestro",
        "architecture": "asus-CM1400CXA-dalboz",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "amlogic_build_valid": {
        "checkout_id": "amlogic_checkout_001",
        "origin": "maestro",
        "architecture": "amlogic,g12b",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "android11-5.4": {
        "checkout_id": "7e39477098b50156535c8f910fee50d6dac2a793",  # android11-5.4
        "origin": "maestro",
        "architecture": "android11-5.4",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "android12-5.10": {
        "checkout_id": "4fd7634f32ffbb4fd4c09b757aa16327626a1749",  # android12-5.10
        "origin": "maestro",
        "architecture": "android12-5.10",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "android12-5.10-lts": {
        "checkout_id": "f72ba1ba267f4c42adb82037e8614d7844badeb9",  # android12-5.10-lts
        "origin": "maestro",
        "architecture": "android12-5.10-lts",
        "status": "PASS",
        "config_name": "defconfig",
    },
    "fluster_build_valid": {
        "checkout_id": "fluster_checkout_001",
        "origin": "maestro",
        "architecture": "arm64",
        "status": "PASS",
        "config_name": "defconfig+lab-setup+arm64-chromebook"
        + "CONFIG_MODULE_COMPRESS=n+CONFIG_MODULE_COMPRESS_NONE=y",
    },
}


# Hardware platform mappings for specific test cases
HARDWARE_PLATFORM_DATA = {
    "asus_checkout_001": "asus-CM1400CXA-dalboz",
    "google_juniper_checkout_001": "google,juniper",
    "arm_juno_checkout_001": "arm,juno",
    "aaeon_checkout_001": "aaeon-UPN-EHLX4RE-A10-0864",
    "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e": "allwinner,sun50i-a64",
    "0704a15b930cf97073ce091a0cd7ad32f2304329": "allwinner,sun50i-a64",
    "4b60a3c25e8793adfb1d92f8e4888321ae416fed": "fsl,imx6q-sabrelite",
    "7e39477098b50156535c8f910fee50d6dac2a793": "android11-5.4",
    "4fd7634f32ffbb4fd4c09b757aa16327626a1749": "android12-5.10",
    "f72ba1ba267f4c42adb82037e8614d7844badeb9": "android12-5.10-lts",
    "fluster_checkout_001": "mt8195-cherry-tomato-r2",
}

# Timestamps for hardware tests - based on integration tests
HARDWARE_TIMESTAMP_DATA = {
    "asus_checkout_001": datetime.fromtimestamp(
        1741356000, timezone.utc
    ),  # asus-CM1400CXA-dalboz
    "amlogic_checkout_001": datetime.fromtimestamp(
        1741359600, timezone.utc
    ),  # amlogic,g12b
    "google_juniper_checkout_001": datetime.fromtimestamp(
        1740227400, timezone.utc
    ),  # google,juniper
    "arm_juno_checkout_001": datetime.fromtimestamp(
        1740232800, timezone.utc
    ),  # arm,juno
    "aaeon_checkout_001": datetime.fromtimestamp(
        1740241800, timezone.utc
    ),  # aaeon-UPN-EHLX4RE-A10-0864
    "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e": datetime.fromtimestamp(
        1741449600, timezone.utc
    ),  # allwinner,sun50i-a64
    "0704a15b930cf97073ce091a0cd7ad32f2304329": datetime.fromtimestamp(
        1741449600, timezone.utc
    ),  # allwinner,sun50i-a64
    "7e39477098b50156535c8f910fee50d6dac2a793": datetime.fromtimestamp(
        1737487800, timezone.utc
    ),  # android11-5.4
    "4fd7634f32ffbb4fd4c09b757aa16327626a1749": datetime.fromtimestamp(
        1737487800, timezone.utc
    ),  # android12-5.10
    "f72ba1ba267f4c42adb82037e8614d7844badeb9": datetime.fromtimestamp(
        1737487800, timezone.utc
    ),  # android12-5.10-lts
    "fluster_checkout_001": datetime.fromtimestamp(
        1741571363, timezone.utc  # 2025-03-10T01:49:23.064000Z
    ),  # fluster_checkout_001
}
