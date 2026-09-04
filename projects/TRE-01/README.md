# TRE-01 — Temporal Reference Engine

**N3USYS Institute experimental project**

TRE-01 is an experimental temporal reference system exploring how time can be represented through measurable physical phenomena rather than conventional clocks.

The project begins with a practical question: **how confident are we that our conventional representation of elapsed time is an adequate representation of physical time across deep temporal scales?**

TRE-01 treats time as a reference problem. Independent physical and astronomical phenomena can be compared, modeled, and assigned uncertainty rather than assuming that a single clock defines time absolutely.

## Current prototype

`tre-01.html` is a self-contained browser prototype. It provides:

- an animated temporal reference core;
- live browser system time as an explicitly undisciplined reference;
- Julian Date calculation;
- approximate Greenwich sidereal time;
- simulated atomic, GNSS, Earth-rotation, and inertial reference channels;
- a simulated temporal-consensus display;
- relativistic-state placeholders;
- reference and observation modes.

The simulation channels are **not measurements** and should not be interpreted as atomic, GNSS, or laboratory-grade timing data.

## Scientific direction

Future TRE-01 development will replace simulated references with physically meaningful models and, where possible, external reference data. Candidate references include:

- atomic frequency standards;
- UTC/TAI relationships;
- GNSS time;
- Earth orientation and UT1;
- Earth rotation;
- orbital velocity;
- gravitational potential;
- special and general relativistic rate corrections;
- NTP/PTP/external timing references;
- eventually, hardware-connected reference sources.

## Related project: CCE-01

TRE-01 is intended to provide the temporal measurement layer for **CCE-01 — Cosmic Computational Epoch**, an N3USYS Institute exploration of cosmic history as an evolving sequence of distinguishable states and computational transitions.

CCE-01 should explicitly distinguish **observed**, **modeled**, **estimated**, and **hypothetical** quantities. The proposed origin point of cosmic computation is a modeling assumption, not an established observation.

## Guiding principle

> **TIME IS NOT OBSERVED. CHANGE IS OBSERVED.**

TRE-01 asks what happens when the measurement of time itself becomes an object of observation.

**Status:** Experimental / Software Prototype

**Designation:** TRE-01

**Organization:** N3USYS Institute
