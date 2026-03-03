---
name: conventional-commits
description: Create commits following Conventional Commits specification
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: git
---

## What I do
I create commits following the Conventional Commits specification (https://www.conventionalcommits.org/).

## Commit Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

## Types
- **feat**: A new feature (correlates with MINOR in SemVer)
- **fix**: A bug fix (correlates with PATCH in SemVer)
- **docs**: Documentation changes only
- **style**: Code style changes (formatting, semicolons, etc.)
- **refactor**: Code refactoring
- **perf**: Performance improvements
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, build changes, etc.
- **ci**: CI configuration changes
- **build**: Build system or dependency changes

## Rules
1. Type MUST be lowercase and followed by a colon and space
2. Description MUST be a short summary of changes (max 50 chars ideal)
3. Use scope in parentheses for contextual info (e.g., `feat(api):`)
4. Use `!` before `:` to indicate breaking changes
5. Breaking changes can also be indicated with `BREAKING CHANGE:` footer
6. Body should wrap at 72 characters
7. Footer tokens should use `-` instead of spaces (e.g., `Reviewed-by`)

## Examples
```
feat: add user authentication
fix: resolve memory leak in audio buffer
docs: update API documentation
feat(api)!: change response format
fix: prevent race condition

BREAKING CHANGE: database schema updated
```

## When to use me
Use this skill whenever creating commits to ensure consistent, machine-readable commit messages that enable:
- Automated CHANGELOG generation
- Semantic version determination
- Clear change history
