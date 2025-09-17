"""
Factory for generating Issue test data.
"""

import factory
from factory.django import DjangoModelFactory
from django.utils import timezone
from kernelCI_app.models import Issues
from .test_data_mapping import ISSUE_TEST_DATA


class IssueFactory(DjangoModelFactory):
    """Factory for creating Issue instances with realistic test data."""

    class Meta:
        model = Issues

    id = factory.Sequence(
        lambda n: (
            [
                "maestro:2ff8fe94f6d53f39321d4a37fe15801cedc93573",
                "maestro:87244933628a2612f39e6096115454f1e8bb3e1c",
                "maestro:ee1cba21ee3fe47f21061725de689b638a9c431a",
                "maestro:cb38e75d16f267781d5b085b9b2dbb390e2885c4",
                "maestro:ae160f6f27192c3527b2e88faba35d85d27c285f",
                "maestro:b9856de6a9d2099f438c8946f3ba192e046bda35",
                "maestro:e602fca280d85d8e603f7c0aff68363bb0cd7993",
                "broonie:bb2eb9603973cb353faa8e780b304d3537220228",
                "linaro:30MeoIqiN9rKm6s2lQLaThEnGHF",
            ][n]
            if n < 9
            else f"issue_{n:08x}"
        )
    )

    version = factory.LazyAttribute(
        lambda obj: (
            ISSUE_TEST_DATA[obj.id]["version"] if obj.id in ISSUE_TEST_DATA else 0
        )
    )

    origin = factory.Sequence(lambda n: (f"origin-fake-{n:08x}"))

    report_url = factory.LazyAttribute(
        lambda obj: f"https://reports.kernelci.org/{obj.origin}/{obj.id}.html"
    )
    report_subject = factory.Faker("sentence", nb_words=6)

    culprit_code = factory.Iterator([True, False, False])
    culprit_tool = factory.Iterator([False, True, False])
    culprit_harness = factory.Iterator([False, False, True])

    comment = factory.Faker("text", max_nb_chars=500)

    categories = factory.LazyFunction(
        lambda: ["build", "boot", "test", "regression", "performance"]
    )

    misc = factory.LazyFunction(
        lambda: {
            "severity": "medium",
            "priority": "normal",
            "assigned_to": "kernel-team@example.com",
            "created_by": "bot@kernelci.org",
        }
    )

    field_timestamp = factory.LazyFunction(lambda: timezone.now())
