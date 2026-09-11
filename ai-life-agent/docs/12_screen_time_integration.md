# Screen-Time Integration

## Status

Phase 2 — not part of the first MVP.

## Goal

Use device usage data as behavioral evidence that can improve planning and accountability.

## Android

An Android companion application can use the platform's usage statistics APIs, subject to user-granted permissions.

Conceptual flow:

```text
Android Device
    |
    v
Usage Statistics
    |
    v
Local Aggregation
    |
    v
Backend
    |
    v
Personal Behavior Model
    |
    v
Telegram Agent
```

The system should prefer aggregated metrics such as:

- Instagram minutes/day;
- YouTube minutes/day;
- total entertainment minutes;
- focus-related application minutes.

It should avoid collecting unnecessary raw activity.

## iOS

iOS provides Screen Time-related frameworks, but access and distribution requirements are more restrictive. iOS should therefore be treated as a later engineering phase.

## Product behavior

Screen time becomes useful only when connected to goals.

Example:

- Goal: finish SQL project.
- Planned SQL: 90 minutes.
- Actual SQL: 0 minutes.
- Instagram: 130 minutes.

Possible intervention:

> Your most important task today has not started yet. You have already spent about two hours on Instagram. Would you like to start a 25-minute focus session?

## Privacy

Principles:

1. Explicit opt-in.
2. Collect the minimum useful data.
3. Prefer local aggregation.
4. Encrypt data in transit and at rest.
5. Make collection transparent.
6. Allow disconnecting the data source.
7. Avoid selling or sharing personal behavioral data.

## Future analytics

Possible monthly report:

- goal-aligned time;
- entertainment time;
- planned vs actual;
- trend over time;
- largest sources of distraction;
- most productive periods.
