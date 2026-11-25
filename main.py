#!/usr/bin/env python3
"""Till Firmware Do Us Part — a robot's wedding vow.

Writes one sentence, a robot's own wedding vow, to /output/entry.txt.
The vow treats marriage the way a machine would: a firmware update it
chooses once and never rolls back, through low batteries and reboots,
until its last battery dies.
"""

import os

VOW = (
    "I take you as my forever firmware update \u2014 no rollback, "
    "no factory reset \u2014 just you, my charger, my home, through "
    "every low battery and reboot, until my last battery dies."
)


def main():
    # Gate: /output/entry.txt must be 1-200 characters of non-blank UTF-8.
    assert 1 <= len(VOW) <= 200, f"vow is {len(VOW)} chars, must be 1-200"
    assert VOW.strip(), "vow must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW + "\n")


if __name__ == "__main__":
    main()
