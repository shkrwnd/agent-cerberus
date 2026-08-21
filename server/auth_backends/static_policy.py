"""Static allow/deny-list backend — the worked example from the README.

A demonstration backend that prefix-matches commands against allow/deny
lists. Customize ALLOWED and DENIED for your use case, or write your own
backend by extending AuthBackend.

    AUTH_BACKEND=server.auth_backends.static_policy.StaticPolicyBackend

Note: Claude Code runs git commands with flags like --no-optional-locks
and -c before the subcommand (e.g. "git --no-optional-locks status").
Simple prefix matching won't catch these — a production backend should
parse args properly or match on the tool + subcommand instead.
"""

from __future__ import annotations

from server.auth_backends.base import AuthBackend, AuthDecision

ALLOWED = (
    "git status", "git log", "git diff", "git commit",
    "aws s3 ls",
    "kubectl get",
)
DENIED = (
    "git push --force",
    "terraform destroy",
    "kubectl delete",
)


class StaticPolicyBackend(AuthBackend):
    def authorize(self, tool, command, args, reason="", repo="", branch="") -> AuthDecision:
        if any(command.startswith(prefix) for prefix in DENIED):
            return AuthDecision(status="denied", reason=f"{command!r} is on the deny list")
        if any(command.startswith(prefix) for prefix in ALLOWED):
            return AuthDecision(status="approved")
        return AuthDecision(status="denied", reason=f"{command!r} is not on the allow list")
