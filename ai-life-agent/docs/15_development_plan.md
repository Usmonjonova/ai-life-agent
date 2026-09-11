# Development Plan

## Principle

Build vertically, not horizontally.

Instead of building every database table first, create one complete user journey and make it work end-to-end.

## Milestone 1 — Project setup

Stack:

- Python
- FastAPI
- PostgreSQL
- Telegram Bot API
- LLM API
- SQLAlchemy
- Alembic
- Docker
- Git

Recommended project structure:

```text
app/
├── main.py
├── config.py
├── bot/
│   ├── handlers.py
│   └── keyboards.py
├── agent/
│   ├── orchestrator.py
│   ├── planner.py
│   ├── memory.py
│   └── prompts.py
├── db/
│   ├── models.py
│   ├── session.py
│   └── repositories/
├── services/
│   ├── goals.py
│   ├── tasks.py
│   ├── notifications.py
│   └── reviews.py
└── schemas/
```

## Milestone 2 — Telegram connection

Implement:

- `/start`;
- message receiving;
- message sending;
- environment-based bot token.

## Milestone 3 — Database

Implement first:

- users;
- goals;
- tasks.

Then add:

- milestones;
- daily logs;
- memories;
- notifications.

## Milestone 4 — Goal conversation

User says:

> I want to finish my SQL project this month.

System:

1. LLM extracts candidate goal.
2. Backend validates structure.
3. Agent asks missing question(s).
4. Goal is saved only after sufficient confirmation.

## Milestone 5 — Daily plan

Implement:

`/today`

Return:

- top priority;
- supporting actions;
- estimated effort;
- reminder options.

## Milestone 6 — Task lifecycle

Support:

- create;
- start;
- complete;
- postpone;
- skip.

Record enough information to learn from behavior.

## Milestone 7 — Scheduler

Add:

- reminders;
- evening reflection;
- weekly review.

Start with a simple scheduler.

## Milestone 8 — Personal pilot

Use the system personally for 2–3 weeks.

Measure:

- usage frequency;
- completion rate;
- reminder usefulness;
- planning accuracy;
- repeated postponements;
- user satisfaction.

Do not add major features merely because they are technically interesting.

## Milestone 9 — Adaptive logic

Only after enough real data exists:

- detect patterns;
- modify workload;
- improve estimates;
- personalize reminders.

## First coding target

The first usable vertical slice should be:

```text
/start
   ↓
Create user
   ↓
Tell me your main goal
   ↓
Save goal
   ↓
Create one task
   ↓
/today
   ↓
Reminder
   ↓
Done
   ↓
Evening reflection
```

If this loop works reliably, the project has a real foundation.
