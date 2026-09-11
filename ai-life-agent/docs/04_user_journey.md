# User Journey

## Day 0 — Onboarding

User starts the bot.

1. Agent explains its role.
2. Agent asks about current goals.
3. User identifies important goals.
4. Agent asks why each goal matters.
5. Agent identifies constraints and commitments.
6. Agent proposes a first priority structure.
7. User confirms or edits it.

Output:

- initial user profile;
- goals;
- first milestones;
- planning preferences.

## Daily flow

### Morning

Agent:

- reviews current goals;
- considers existing commitments;
- proposes 1–3 important actions;
- asks for confirmation when necessary.

### During the day

Agent:

- sends only useful reminders;
- offers a low-friction way to start;
- accepts natural-language updates;
- records completion, postponement, or blockage.

### Evening

Agent asks for a short reflection.

It should prefer evidence over generic motivational questions.

Example:

> You planned 90 minutes of SQL today and completed 40. What made the remaining 50 minutes difficult?

## Weekly flow

At the end of the week:

1. Compare plan vs actual.
2. Identify completed priorities.
3. Identify repeated misses.
4. Detect planning errors.
5. Review goal progress.
6. Suggest changes.
7. Ask the user to approve the next week's priorities.

## Exceptional flow

If the user says:

> “I can't do this today.”

The agent should not simply mark the task as failed.

It should determine whether to:

- move it;
- shrink it;
- split it;
- replace it;
- deprioritize it;
- or question whether it still matters.

## Long-term loop

Every week contributes evidence to a personal model:

**Goal → Plan → Behavior → Outcome → Pattern → Adaptation**
