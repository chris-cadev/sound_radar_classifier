---
name: conventional-commits
description: Create commits following Conventional Commits specification
license: MIT
compatibility: opencode
metadata:
  audience: developers
  workflow: git
---

## Triggers

Activate when the user asks to:

- Create a commit
- Make a commit
- Commit changes
- Commit code
- Write a commit message
- Generate a commit message
- Help with committing

or variants of these phrases.

## What I do

I create commits following the Conventional Commits specification (https://www.conventionalcommits.org/).

## Commit Format

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer(s)]
```

## Types

| Type         | Description                                       | SemVer |
| ------------ | ------------------------------------------------- | ------ |
| **feat**     | A new feature for the user                        | MINOR  |
| **fix**      | A bug fix for the user                            | PATCH  |
| **docs**     | Documentation changes only                        | PATCH  |
| **style**    | Code style changes (formatting, semicolons, etc.) | PATCH  |
| **refactor** | Code refactoring (no feature/fix)                 | PATCH  |
| **perf**     | Performance improvements                          | PATCH  |
| **test**     | Adding or updating tests                          | PATCH  |
| **chore**    | Maintenance tasks, build changes, deps updates    | PATCH  |
| **ci**       | CI configuration changes                          | PATCH  |
| **build**    | Build system or dependency changes                | PATCH  |
| **revert**   | Reverting a previous commit                       | PATCH  |
| **merge**    | Merge branches                                    | PATCH  |

## Detailed Type Guidelines

### feat

Use for new functionality that users can interact with. Examples: adding a new API endpoint, new UI component, new user feature.

```
feat(auth): add OAuth2 login support
feat(player): add playback speed control
```

### fix

Use for bug fixes that resolve issues users experience. Examples: crash fixes, incorrect calculations, unexpected behavior.

```
fix(audio): resolve buffer overflow in WAV parser
fix(ui): correct button alignment on mobile
```

### docs

Use for documentation only. This includes README changes, API docs, code comments.

```
docs: update installation guide
docs(api): add endpoint examples
```

### style

Use for formatting changes that don't affect logic. Examples: Prettier formatting, lint fixes, adding missing semicolons.

```
style: run prettier on all source files
style(css): format stylesheet according to style guide
```

### refactor

Use for code changes that improve structure without changing behavior. Examples: extracting functions, renaming variables, splitting modules.

```
refactor(api): extract validation logic to separate module
refactor: simplify conditional logic in player
```

### perf

Use for changes that improve performance. Examples: algorithm optimizations, caching, lazy loading.

```
perf: optimize FFT calculation using FFTW
perf: add caching for expensive computations
```

### test

Use for test-related changes. Examples: adding new tests, fixing broken tests, test infrastructure.

```
test: add unit tests for audio processor
test(integration): add end-to-end tests for auth flow
```

### chore

Use for maintenance tasks that don't affect the codebase. Examples: updating dependencies, CI/CD changes, tooling.

```
chore: update dependencies to latest versions
chore: upgrade Node.js to v20
```

### ci

Use specifically for CI/CD configuration changes.

```
ci: add GitHub Actions workflow for testing
ci: configure build matrix for multiple Node versions
```

### build

Use for changes to build system or external dependencies.

```
build: configure webpack for production builds
build: add native audio library bindings
```

### revert

Use when reverting a previous commit.

```
revert: revert "feat(auth): add OAuth2 login"
This reverts commit abc123.
```

## Rules

1. Type MUST be lowercase and followed by a colon and space
2. Description MUST be a short summary of changes (max 50 chars ideal)
3. Use scope in parentheses for contextual info (e.g., `feat(api):`)
4. Use `!` before `:` to indicate breaking changes
5. Breaking changes can also be indicated with `BREAKING CHANGE:` footer
6. Body should wrap at 72 characters
7. Footer tokens should use `-` instead of spaces (e.g., `Reviewed-by`)
8. Start description with lowercase (unless proper noun)
9. Don't end description with a period

## Common Mistakes

### ❌ Wrong

```
feat: Added user authentication
fix: fixing memory leak
feat(api): This adds a new endpoint for getting user data
feat: ADD login functionality
```

### ✅ Correct

```
feat(auth): add user authentication
fix: resolve memory leak in audio buffer
feat(api): add user data endpoint
feat: add login functionality
```

### Mistakes to Avoid

1. **Using wrong tense**: Description should describe what the commit does, not what it did
2. **Missing colon**: Always use `<type>: <description>` format
3. **No space after colon**: Must be `type: description` not `type:description`
4. **Capitalizing description**: Keep it lowercase unless it starts with a proper noun
5. **Vague descriptions**: Be specific about what changed
6. **Scope without parentheses**: Use `(scope)` not `[scope]`
7. **Overusing chore**: Don't use chore for actual code changes
8. **Confusing refactor with feat**: Refactor is for code cleanup, feat is for new features
9. **Breaking changes without indication**: Use `!` or BREAKING CHANGE footer

## Examples

### Simple commits

```
feat: add user authentication
fix: resolve memory leak in audio buffer
docs: update API documentation
refactor: extract audio processing to separate module
test: add tests for FFT processor
```

### With scope

```
feat(auth): add OAuth2 login
feat(api): add user profile endpoint
fix(player): correct play/pause state
fix(audio): prevent clipping on high volume
style(ui): format components with prettier
perf(fft): optimize frequency calculation
```

### Breaking changes

```
feat(api)!: change response format

BREAKING CHANGE: the response now returns JSON:API format
instead of custom JSON structure. Update your client accordingly.
```

### With body and footer

```
fix: resolve race condition in audio stream

The audio buffer could overflow when multiple streams
were played simultaneously.

Closes #123
Reviewed-by: @team Lead
```

### Multi-line format

```
feat(player): add playlist support

Implement playlist functionality with shuffle and repeat
modes. Users can now create, save, and load playlists
directly from the player UI.

Closes #45
Closes #67
```

## Workflow

1. Check `git status` to see all changed files
2. Review changes with `git diff`
3. Analyze what type of change this is
4. Write a clear, concise commit message following the rules
5. Create the commit with `git commit -m "<message>"`

## When to use me

Use this skill whenever creating commits to ensure consistent, machine-readable commit messages that enable:

- Automated CHANGELOG generation
- Semantic version determination
- Clear change history
- Better git history navigation
