# Privacy and Security

## Product principle

The agent will potentially know highly personal information. Trust is therefore part of the product.

## Data minimization

Store only information needed for the product.

Do not collect data simply because it is technically available.

## Separation of concerns

Keep:

- authentication data;
- structured product data;
- conversation data;
- derived behavioral metrics

logically separated.

## Sensitive information

The product should avoid unnecessary collection of:

- credentials;
- payment information;
- identity documents;
- sensitive health information;
- precise location.

## Access control

Every database query involving personal data must be scoped to the authenticated user.

## Secrets

API keys and bot tokens must never be committed to Git.

Use environment variables or a secrets manager.

## Logging

Logs should not contain raw private conversations or sensitive payloads by default.

## User transparency

Future UI should support:

- viewing stored memories;
- correcting important memories;
- disabling data sources;
- deleting account data;
- understanding why recommendations were made.

## Threat model — initial

Consider:

- stolen bot token;
- leaked database;
- unauthorized account access;
- accidental logging;
- malicious prompt injection;
- third-party API exposure.

Security work should increase before real external users are invited.
