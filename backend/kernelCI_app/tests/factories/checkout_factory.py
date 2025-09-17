"""
Factory for generating Checkout test data.
"""

import factory
import random
from factory.django import DjangoModelFactory
from django.utils import timezone
from kernelCI_app.models import Checkouts
from .test_data_mapping import TREE_TEST_DATA, HARDWARE_TIMESTAMP_DATA


class CheckoutFactory(DjangoModelFactory):
    """Factory for creating Checkout instances with realistic test data."""

    class Meta:
        model = Checkouts

    # Generate specific IDs that tests expect
    id = factory.Sequence(
        lambda n: (
            [
                "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE
                "ef143cc9d68aecf16ec4942e399e7699266b288f",  # ANDROID_MAINLINE_TREE
                "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba",  # ANDROID_MAESTRO_MAINLINE
                "33040a50cdaec186c13ef3f7b9c9b668d8e32637",  # NEXT_PENDING_FIXES_BROONIE
                "4b60a3c25e8793adfb1d92f8e4888321ae416fed",  # BROONIE_MISC_BROONIE
                "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e",  # ALLWINNER_HARDWARE
                "0704a15b930cf97073ce091a0cd7ad32f2304329",  # ALLWINNER_HARDWARE
                "fb482243c16ebfe8776fcd52223351b4061c1729",  # INVALID_QUERY_PARAMS
                "7e39477098b50156535c8f910fee50d6dac2a793",  # android11-5.4
                "4fd7634f32ffbb4fd4c09b757aa16327626a1749",  # android12-5.10
                "f72ba1ba267f4c42adb82037e8614d7844badeb9",  # android12-5.10-lts
                # Additional IDs for other hardware tests
                "google_juniper_checkout_001",
                "arm_juno_checkout_001",
                "aaeon_checkout_001",
                "asus_checkout_001",
                "amlogic_checkout_001",
                "fluster_checkout_001",
            ][n]
            if n < 17
            else f"checkout_{n:08x}"
        )
    )

    # Use specific origins for test checkouts, random for others
    origin = factory.LazyAttribute(
        lambda obj: (
            TREE_TEST_DATA[obj.id]["origin"]
            if obj.id in TREE_TEST_DATA
            else "fake-origin"
        )
    )

    tree_name = factory.LazyAttribute(
        lambda obj: (
            TREE_TEST_DATA[obj.id]["tree_name"]
            if obj.id in TREE_TEST_DATA
            else f"{obj.origin}-tree"
        )
    )

    git_repository_url = factory.LazyAttribute(
        lambda obj: (
            TREE_TEST_DATA[obj.id]["git_url"]
            if obj.id in TREE_TEST_DATA
            else {
                "maestro": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                "redhat": "https://git.kernel.org/pub/scm/linux/kernel/git/redhat/linux.git",
                "microsoft": "https://github.com/microsoft/WSL2-Linux-Kernel.git",
                "broonie": "https://git.kernel.org/pub/scm/linux/kernel/git/broonie/linux.git",
                "linaro": "https://git.linaro.org/landing-teams/working/arm/kernel-release.git",
                "0dayci": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
                "syzbot": "https://github.com/google/syzkaller.git",
                "android-mainline": "https://android.googlesource.com/kernel/common.git",
                "next-pending-fixes": "https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git",
            }.get(
                obj.origin,
            )
        )
    )

    git_commit_hash = factory.Iterator(
        [
            "a1c24ab822793eb513351686f631bd18952b7870",  # ARM64_TREE - for treeDetailsSummary_test
            "ef143cc9d68aecf16ec4942e399e7699266b288f",  # ANDROID_MAINLINE_TREE
            "fdf4d20b86285d7b4d1c2d3349a1bd1bc41b24ba",  # ANDROID_MAESTRO_MAINLINE
            "33040a50cdaec186c13ef3f7b9c9b668d8e32637",  # NEXT_PENDING_FIXES_BROONIE
            "4b60a3c25e8793adfb1d92f8e4888321ae416fed",  # BROONIE_MISC_BROONIE
            "5b4ec6e1eb7603b6d86a172d77efdf75eb741e7e",  # ALLWINNER_HARDWARE
            "0704a15b930cf97073ce091a0cd7ad32f2304329",  # ALLWINNER_HARDWARE
            "fb482243c16ebfe8776fcd52223351b4061c1729",  # INVALID_QUERY_PARAMS
            "7e39477098b50156535c8f910fee50d6dac2a793",  # android11-5.4
            "4fd7634f32ffbb4fd4c09b757aa16327626a1749",  # android12-5.10
            "f72ba1ba267f4c42adb82037e8614d7844badeb9",  # android12-5.10-lts
            # Additional hardware test hashes
            "google_juniper_checkout_001",
            "arm_juno_checkout_001",
            "aaeon_checkout_001",
            "asus_checkout_001",
            "amlogic_checkout_001",
            "fluster_checkout_001",
        ]
    )

    git_commit_name = factory.LazyAttribute(
        lambda obj: f"commit-{obj.git_commit_hash[:8]}"
    )

    git_repository_branch = factory.LazyAttribute(
        lambda obj: (
            TREE_TEST_DATA[obj.id]["git_branch"]
            if obj.id in TREE_TEST_DATA
            else "fake-branch"
        )
    )

    patchset_files = factory.LazyFunction(
        lambda: [
            {
                "name": "0001-fix-example.patch",
                "url": "https://example.com/patch1.patch",
            },
            {
                "name": "0002-update-config.patch",
                "url": "https://example.com/patch2.patch",
            },
        ]
    )

    patchset_hash = factory.Sequence(lambda n: f"patchset_{n:08x}")

    message_id = factory.Sequence(lambda n: f"<message-{n}@kernelci.org>")

    comment = factory.Faker("text", max_nb_chars=200)

    start_time = factory.LazyAttribute(
        lambda obj: (
            HARDWARE_TIMESTAMP_DATA[obj.id]
            if obj.id in HARDWARE_TIMESTAMP_DATA
            else timezone.now() - timezone.timedelta(days=random.randint(1, 30))
        )
    )

    log_url = factory.LazyAttribute(
        lambda obj: f"https://logs.kernelci.org/{obj.origin}/{obj.git_commit_hash[:8]}.log"
    )

    log_excerpt = factory.Faker("text", max_nb_chars=1000)

    valid = factory.Iterator([True, True, True, False])

    misc = factory.LazyFunction(
        lambda: {
            "build_environment": "docker",
            "kernel_version": "6.1.0",
            "compiler": "gcc-11.2.0",
        }
    )

    git_commit_message = factory.Faker("text", max_nb_chars=500)
    git_repository_branch_tip = factory.Iterator([True, False])
    git_commit_tags = factory.LazyFunction(lambda: ["v6.1", "stable"])

    origin_builds_finish_time = factory.LazyFunction(
        lambda: timezone.now() - timezone.timedelta(minutes=30)
    )

    origin_tests_finish_time = factory.LazyFunction(
        lambda: timezone.now() - timezone.timedelta(minutes=15)
    )

    field_timestamp = factory.LazyFunction(lambda: timezone.now())
