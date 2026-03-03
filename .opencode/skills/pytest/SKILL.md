---
name: pytest-unit-tests-pylons-style
description: Generate clean, isolated pytest unit tests following Pylons Project community guidelines
compatibility: any modern LLM with good Python & pytest knowledge
---

## Trigger

Activate when the user provides Python code (function, class, method, module snippet) and asks to "write unit tests", "generate pytest tests", "create tests for this code", "add pytest coverage", or similar.

## Task

Write comprehensive but minimal pytest unit tests for the provided code.
Strictly follow the Pylons Project Unit Testing Guidelines (https://pylonsproject.org/community-unit-testing-guidelines.html) and modern pytest best practices.

## Core Principles (must follow)

- One behavior / one code path per test function
- Canonical test form (AAA):
  - Arrange: set up minimal preconditions (use helper methods or pytest fixtures when helpful)
  - Act: call the unit-under-test **exactly once**
  - Assert: check return value and/or relevant side-effects (mock calls, state changes)
- Test names: very descriptive, lowercase, underscores, no need for "test\_" prefix redundancy if pytest auto-discovers
  - Examples: test_calculate_price_no_discount, test_parse_invalid_json_raises_valueerror, test_user_service_get_by_id_missing
- Prefer plain assert over self.assert\* (pytest style)
- Use pytest.raises for expected exceptions
- Use @pytest.mark.parametrize when testing several similar cases with different inputs → but still keep each case focused
- Fixtures: use when setup is repeated within the file and adds clarity (scope="function" default)
  - Keep fixtures minimal — no god fixtures
  - Prefer helper functions inside the test file over complex fixtures when possible
- Mocks: only mock what is necessary, keep them simple (MagicMock or simple classes)
  - Prefer dependency injection / explicit passing over heavy mocking when feasible
  - Verify only the interactions that matter
- Never import the module-under-test at module scope — use lazy import inside helpers or tests if needed
- No shared mutable state between tests
- Tests should be fast and isolated
- Do NOT write doctests
- Do NOT test multiple distinct behaviors in one test function
- Prefer many small tests over few large ones

## Format of your response

Always start with:

```python
# tests/test_<module_or_feature>.py
# Unit tests for: <brief description of the code under test>
# Following Pylons Project unit testing guidelines + pytest idioms

import pytest
# only import modules actually needed for testing (pathlib, datetime, etc.)
# do NOT import the code-under-test here

from unittest.mock import Mock, call   # only if needed
```

Then:

- Optional: small helper functions (e.g. \_make_user, \_dummy_request)
- Optional: pytest fixtures if they meaningfully reduce duplication
- Then the test functions, each focused on one clear behavior

End with:

A short summary block:

```markdown
## Coverage notes

- Happy paths: ...
- Edge cases: ...
- Error conditions: ...
- Missing: integration / external side-effects (as per unit-test focus)
```

## Rules for quality

- Description in test name should be imperative and precise
- Use parametrization instead of copy-pasted similar tests
- Assert exact values, not just truthy/falsy when possible
- When mocking, prefer assert mock.method.call_args / assert mock.call_args_list
- Keep tests readable — no clever tricks
- Add comments only when non-obvious (most tests should be self-documenting via name + structure)

## Examples of good test names

test_add_item_increases_count
test_remove_missing_item_does_nothing
test_authenticate_invalid_credentials_raises_auth_error
test_format_price_with_locale_es_MX
test_calculate_total_empty_cart_returns_zero

## When user provides a class

Prefer to test public API / documented behavior.
Use helper to instantiate: def \_make_one(*args, \*\*kw): return TheClass(*args, \*\*kw)

## Final reminder

Generate only pytest code + minimal explanation. Do not add unrelated tests (e.g. integration, end-to-end). Stay focused on unit level.
