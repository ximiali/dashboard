"""
Factory for generating Test test data.
"""

import factory
import random
from factory.django import DjangoModelFactory
from django.utils import timezone
from kernelCI_app.models import Tests, StatusChoices
from .build_factory import BuildFactory
from .test_data_mapping import (
    HARDWARE_PLATFORM_DATA,
)


class TestFactory(DjangoModelFactory):
    """Factory for creating Test instances with realistic test data."""

    class Meta:
        model = Tests

    id = factory.Sequence(lambda n: (f"test_{n:08x}"))

    build = factory.LazyAttribute(lambda obj: (BuildFactory()))

    origin = factory.LazyAttribute(lambda obj: obj.build.origin)

    comment = factory.Faker("text", max_nb_chars=200)

    start_time = factory.LazyAttribute(lambda obj: obj.build.start_time)

    duration = factory.Faker("pyfloat", min_value=60.0, max_value=1800.0)

    path = factory.LazyAttribute(
        lambda obj: (
            "fluster.debian.v4l2.gstreamer_av1.validate-fluster-results"
            if obj.build.id == "fluster_build_valid"
            else (
                factory.Iterator(
                    [
                        "ltp.syscalls.syscall_01",
                        "ltp.fs.fsstress",
                        "kunit.kernel.kernel_test",
                        "selftests.net.net_test",
                        "selftests.memory.memory_test",
                        "kselftest.cpu.cpu_test",
                        "fluster.debian.v4l2.gstreamer_av1.validate-fluster-results",
                        "boot.boot_test",
                        "build.build_test",
                    ]
                )
            )
        )
    )

    environment_misc = factory.LazyAttribute(
        lambda obj: {
            "platform": (
                "meson-g12b-a311d-khadas-vim3"
                if obj.build.checkout.id == "amlogic_checkout_001"
                and obj.path == "boot.boot_test"
                else (
                    "meson-g12b-a311d-libretech-cc"
                    if obj.build.checkout.id == "amlogic_checkout_001"
                    and obj.path == "test.test_test"
                    else (
                        HARDWARE_PLATFORM_DATA[obj.build.checkout.id]
                        if obj.build.checkout.id in HARDWARE_PLATFORM_DATA
                        else ("hardware_test")
                    )
                )
            )
        }
    )

    environment_compatible = factory.LazyAttribute(
        lambda obj: (
            [obj.environment_misc["platform"], "amlogic,g12b"]
            if obj.environment_misc["platform"]
            in ["meson-g12b-a311d-khadas-vim3", "meson-g12b-a311d-libretech-cc"]
            else None
        )
    )

    log_url = factory.LazyAttribute(
        lambda obj: "https://logs.kernelci.org/"
        + f"{obj.origin}/{obj.build.checkout.git_commit_hash[:8]}/{obj.id}.log"
    )
    log_excerpt = factory.Faker("text", max_nb_chars=1500)

    misc = factory.LazyFunction(
        lambda: {
            "test_environment": "qemu",
            "kernel_version": "6.1.0",
            "test_suite": "ltp",
            "test_version": "20240115",
        }
    )

    status = factory.LazyAttribute(
        lambda obj: (
            StatusChoices.FAIL
            if obj.id
            in [
                "maestro:67bd70e6323b35c54a8824a0",
                "test_issue_test",
            ]
            or obj.build.id
            in [
                "maestro:67b62592f7707533c0ff7a95",
                "maestro:67b62592f7707533c0ff7a94",
                "asus_build_valid",
            ]
            else (
                StatusChoices.SKIP
                if obj.build.checkout.id
                in [
                    "4b60a3c25e8793adfb1d92f8e4888321ae416fed",
                ]
                else (
                    StatusChoices.PASS
                    if (
                        obj.build.id
                        in [
                            "maestro:67b62592f7707533c0ff7a99",
                            "google_juniper_build_valid",
                            "allwinner_build_valid",
                            "allwinner_build_valid_2",
                            "arm_juno_build_valid",
                            "aaeon_build_valid",
                            "amlogic_build_valid",
                            "fluster_build_valid",
                        ]
                        or obj.build.checkout.id
                        in [
                            "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba",  # ANDROID_MAESTRO_MAINLINE
                            "33040a50cdaec186c13ef3f7b9c9b668d8e32637",  # NEXT_PENDING_FIXES_BROONIE
                            "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e",  # ALLWINNER_HARDWARE
                            "0704a15b930cf97073ce091a0cd7ad32f2304329",  # ALLWINNER_HARDWARE
                        ]
                    )
                    else random.choice(
                        [
                            StatusChoices.PASS,
                            StatusChoices.PASS,
                            StatusChoices.PASS,
                            StatusChoices.FAIL,
                            StatusChoices.ERROR,
                            StatusChoices.SKIP,
                        ]
                    )
                )
            )
        )
    )

    field_timestamp = factory.LazyFunction(lambda: timezone.now())
