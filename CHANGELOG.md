# Changelog

## Unreleased

### Security fixes

- **Tool name allowlist** — The execution server now only accepts tool names matching known CLI wrappers (`aws`, `az`, `gh`, `git`, `kubectl`, `psql`, `terraform`). Previously, any binary on the host PATH could be invoked (e.g. `/bin/sh`, `curl`, `python3`). Additional tools can be added via `EXTRA_ALLOWED_TOOLS` in `deploy/server.env`. Tool names containing path separators (`/`, `\`) are rejected outright.

- **Environment scrubbing** — The default `execution_env()` in `AuthBackend` now strips env vars whose names contain `secret`, `token`, `password`, `api_key`, or `private_key`. The handler also scrubs `EXEC_TOKEN`, `AUTH_WEBHOOK_TOKEN`, `AUTH_WEBHOOK_SECRET`, `OUTHORA_AGENT_SECRET`, and `OUTHORA_API_KEY` before every execution. Previously, the full host environment (including all credentials and the shared exec token) was passed to every executed command.

- **Git config-driven code execution mitigated** — Git commands now run with `-c core.hooksPath=/dev/null -c core.fsmonitor= -c core.pager=cat`, preventing agent-written git hooks, fsmonitor scripts, or pager commands from executing arbitrary code on the host.

- **Request body size limit** — The execution server now rejects request bodies larger than 1 MB (HTTP 413). Previously, there was no limit, allowing a malicious container to exhaust host memory.

- **Concurrency limit** — A semaphore limits concurrent command executions to 20. Requests beyond this limit receive HTTP 503 after a 5-second wait.

- **Rate limiting** — The server rejects requests exceeding 50 per 10-second window (HTTP 429), preventing request flooding from exhausting host resources.

- **Temp credential cleanup** — Temporary kubeconfig files created for kubectl credential injection are now deleted after command execution.
