"""
Factory for generating Build test data.
"""

import factory
import random
from factory.django import DjangoModelFactory
from django.utils import timezone
from kernelCI_app.models import Builds, StatusChoices
from .checkout_factory import CheckoutFactory
from .test_data_mapping import (
    HARDWARE_PLATFORM_DATA,
)


class BuildFactory(DjangoModelFactory):
    """Factory for creating Build instances with realistic test data."""

    class Meta:
        model = Builds

    id = factory.Sequence(lambda n: f"build_{n:08x}")

    checkout = factory.SubFactory(CheckoutFactory)

    origin = factory.LazyAttribute(lambda obj: obj.checkout.origin)

    comment = factory.Faker("text", max_nb_chars=200)

    start_time = factory.LazyAttribute(lambda obj: obj.checkout.start_time)

    duration = factory.Faker("pyfloat", min_value=300.0, max_value=3600.0)  # 5min to 1h

    architecture = factory.LazyAttribute(
        lambda obj: (
            random.choice(
                ["x86_64", "arm64", "arm", "i386", "mips", "powerpc", "riscv", "s390"]
            )
        )
    )

    command = factory.LazyAttribute(
        lambda obj: f"make ARCH={obj.architecture} defconfig all"
    )

    compiler = factory.LazyAttribute(
        lambda obj: (
            ["gcc-12"]
            if obj.checkout.id != "aaeon_checkout_001"
            else ["gcc-11.2.0", "gcc-12.1.0", "clang-14.0.0", "clang-15.0.0"]
        )
    )

    input_files = factory.LazyFunction(
        lambda: [
            {"name": "defconfig", "url": "https://example.com/defconfig"},
            {"name": "kernel.config", "url": "https://example.com/kernel.config"},
        ]
    )

    output_files = factory.LazyFunction(
        lambda: [
            {"name": "vmlinux", "url": "https://example.com/vmlinux"},
            {"name": "bzImage", "url": "https://example.com/bzImage"},
            {"name": "modules.tar.gz", "url": "https://example.com/modules.tar.gz"},
        ]
    )

    # Use specific config name for test checkouts, random for others
    config_name = factory.LazyAttribute(
        lambda obj: (
            random.choice(
                [
                    "defconfig",
                    "defconfig+CONFIG_DEBUG_INFO=y",
                    "defconfig+CONFIG_MODULE_COMPRESS=n+CONFIG_MODULE_COMPRESS_NONE=y",
                    "allmodconfig",
                    "allnoconfig",
                    "tinyconfig",
                ]
            )
        )
    )

    config_url = factory.LazyAttribute(
        lambda obj: f"https://configs.kernelci.org/{obj.origin}/{obj.config_name}"
    )
    log_url = factory.LazyAttribute(
        lambda obj: f"https://logs.kernelci.org/{obj.origin}/{obj.checkout.git_commit_hash[:8]}/{obj.id}.log"
    )
    log_excerpt = factory.Faker("text", max_nb_chars=2000)

    misc = factory.LazyAttribute(
        lambda obj: {
            "build_environment": "docker",
            "kernel_version": "6.1.0",
            "build_time": "2024-01-15T10:30:00Z",
            "memory_usage": "2.5GB",
            "disk_usage": "1.2GB",
            "hardware": (
                HARDWARE_PLATFORM_DATA[obj.checkout.id]
                if obj.checkout.id in HARDWARE_PLATFORM_DATA
                else "fake-hardware"
            ),
        }
    )

    status = factory.LazyAttribute(
        lambda obj: (
            StatusChoices.FAIL
            if obj.id
            in [
                "maestro:67b62592f7707533c0ff7a95",  # ARM64_TREE
            ]
            else (
                StatusChoices.PASS
                if obj.checkout.id
                in [
                    "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba",  # ANDROID_MAESTRO_MAINLINE
                    "33040a50cdaec186c13ef3f7b9c9b668d8e32637",  # NEXT_PENDING_FIXES_BROONIE
                    "4b60a3c25e8793adfb1d92f8e4888321ae416fed",  # BROONIE_MISC_BROONIE
                    "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE
                    "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e",  # ALLWINNER_HARDWARE
                    "0704a15b930cf97073ce091a0cd7ad32f2304329",  # ALLWINNER_HARDWARE
                    "aaeon_checkout_001",  # AAEON_HARDWARE
                    "asus_checkout_001",  # ASUS_HARDWARE
                ]
                else random.choice(
                    [
                        StatusChoices.PASS,
                        StatusChoices.PASS,
                        StatusChoices.PASS,  # Mostly pass for other cases
                        StatusChoices.FAIL,
                        StatusChoices.ERROR,
                    ]
                )
            )
        )
    )

    field_timestamp = factory.LazyFunction(lambda: timezone.now())
