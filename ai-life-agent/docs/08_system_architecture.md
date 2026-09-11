# System Architecture

## MVP architecture

```text
Telegram
   |
   v
Telegram Bot
   |
   v
FastAPI Backend
   |
   +---- Agent Orchestrator
   |        |
   |        +---- Goal Manager
   |        +---- Task Planner
   |        +---- Reflection Engine
   |        +---- Progress Analyzer
   |        +---- Memory Manager
   |        +---- Notification Manager
   |
   +---- PostgreSQL
   |
   +---- LLM API
   |
   +---- Scheduler
```

## Responsibilities

### Telegram layer

Handles:

- incoming messages;
- buttons;
- commands;
- outgoing messages.

It should not contain business logic.

### Backend

Owns:

- authentication/identity;
- business rules;
- persistence;
- orchestration;
- API endpoints.

### Agent Orchestrator

Determines which capability is needed for a user message.

Examples:

- goal creation;
- task update;
- planning;
- reflection;
- explanation;
- general conversation.

### PostgreSQL

Source of truth for structured state.

### LLM

Used for:

- natural-language understanding;
- reasoning over supplied context;
- drafting plans;
- summarization;
- conversational responses.

Critical state changes should be validated by backend code.

### Scheduler

Initially a simple scheduler is acceptable. It can later be replaced with a distributed queue system.

## Future architecture

```text
Telegram ───────┐
Web App ────────┤
Mobile App ─────┤
Android Data ───┤
Calendar ───────┤
                v
          Personal Data Layer
                |
                v
          Agent Orchestrator
                |
        Personal User Model
                |
          Planning Engine
```

The interface should remain replaceable.
