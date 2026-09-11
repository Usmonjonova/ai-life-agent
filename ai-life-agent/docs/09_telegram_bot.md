# Telegram Bot Specification

## Philosophy

The user should not need to remember commands. Natural conversation is the primary interface.

Commands are shortcuts, not the product itself.

## Initial commands

- `/start` — onboarding
- `/today` — today's plan
- `/goals` — active goals
- `/progress` — progress summary
- `/review` — start reflection/review
- `/focus` — start a focus session
- `/settings` — preferences

## Natural language examples

User:

> I want to finish my SQL project by the end of this month.

Agent:

- recognizes a goal;
- asks only necessary clarifying questions;
- creates structured goal state;
- proposes milestones.

User:

> I finished the first part.

Agent:

- identifies the relevant task;
- records completion;
- updates progress.

User:

> Move today's Python task to tomorrow.

Agent:

- finds task;
- reschedules it;
- confirms the change.

## Buttons

Where useful:

`[Start] [Done] [Move] [Skip]`

Buttons should reduce typing for frequent actions.

## Conversation state

Short-lived conversation state should be stored separately from long-term memory.

Example:

```text
ONBOARDING_GOAL_1
WAITING_FOR_GOAL_WHY
WAITING_FOR_TARGET_DATE
```

State should expire when no longer relevant.

## Error handling

If intent is ambiguous, ask a short clarification question.

Do not silently create important goals or delete data based on uncertain interpretation.
