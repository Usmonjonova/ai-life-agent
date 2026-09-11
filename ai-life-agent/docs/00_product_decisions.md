# Product Decisions

## Decision 1 — Start with Telegram

Reason: lowest interaction friction and fast validation.

## Decision 2 — Telegram is an interface, not the architecture

Business logic remains in the backend so web/mobile clients can be added later.

## Decision 3 — Start single-user

The first objective is personal validation, not scale.

## Decision 4 — Build the adaptive loop before screen-time integration

Behavioral data is valuable only after the core planning/reflection system works.

## Decision 5 — AI does not own structured state

Goals, tasks, dates, and statuses live in PostgreSQL.

## Decision 6 — User remains in control

The agent proposes and explains; the user approves meaningful changes.

## Decision 7 — Optimize for usefulness, not engagement

The goal is better life decisions and execution, not more time inside the bot.
