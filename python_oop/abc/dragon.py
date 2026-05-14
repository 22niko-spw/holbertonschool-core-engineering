#!/usr/bin/env python3
"""Mixin pattern example with SwimMixin, FlyMixin, and Dragon."""


class SwimMixin:
    """Mixin that grants swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that grants flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim, fly, and roar."""

    def roar(self):
        print("The dragon roars!")
