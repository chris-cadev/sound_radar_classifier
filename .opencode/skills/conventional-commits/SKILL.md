---
name: conventional-commits
description: Generate commit messages using Conventional Commits
compatibility: opencode
---

## Trigger

Activate when the user asks to create or write a commit message.

## Task

Generate a commit message following the Conventional Commits specification.

## Format

<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]

## Types

feat # new feature (MINOR)
fix # bug fix (PATCH)
docs # documentation only
style # formatting, no logic changes
refactor # code restructuring, no behavior change
perf # performance improvement
test # tests added/updated
chore # maintenance, tooling, deps
ci # CI/CD config
build # build system/deps
revert # revert commit
merge # merge branches

## Rules

- type must be lowercase
- format: `type: description`
- one space after colon
- description: short, imperative, lowercase, no period
- optional scope: `(scope)`
- breaking change: add `!` before `:` or `BREAKING CHANGE:` footer
- wrap body at ~72 characters
- footer tokens use hyphens (e.g., `Reviewed-by`)

## Examples

feat(auth): add OAuth2 login  
fix(api): resolve null pointer error  
docs: update README  
refactor(player): simplify state logic  
feat(api)!: change response format

BREAKING CHANGE: response structure updated
