# Data Model

## Core entities

### users

- id
- telegram_id
- name
- timezone
- created_at
- updated_at

### goals

- id
- user_id
- title
- description
- why
- priority
- status
- target_date
- created_at
- updated_at

### milestones

- id
- goal_id
- title
- description
- target_date
- status

### projects

- id
- user_id
- goal_id
- title
- status

### tasks

- id
- user_id
- goal_id
- milestone_id
- project_id
- title
- description
- priority
- status
- estimated_minutes
- scheduled_for
- completed_at
- postponed_count

### habits

- id
- user_id
- title
- frequency
- target
- status

### daily_logs

- id
- user_id
- date
- planned_minutes
- completed_minutes
- reflection
- created_at

### weekly_reviews

- id
- user_id
- week_start
- summary
- wins
- blockers
- plan_accuracy
- recommendations

### memories

- id
- user_id
- category
- content
- source
- confidence
- expires_at
- created_at
- updated_at

### notifications

- id
- user_id
- task_id
- scheduled_at
- sent_at
- status
- action_taken

## Design principle

The database stores structured state. The LLM should not be treated as the source of truth for goals, tasks, deadlines, or user state.

## Initial relationship

User 1—N Goals

Goal 1—N Milestones

Goal 1—N Tasks

User 1—N Tasks

User 1—N Daily Logs

User 1—N Weekly Reviews

User 1—N Memories
