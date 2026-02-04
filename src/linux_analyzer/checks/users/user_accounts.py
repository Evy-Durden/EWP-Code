# linux_analyzer/analysis/checks/users/accounts.py
from linux_analyzer.core.context import ExecutionContext
from linux_analyzer.core.models import Finding
from linux_analyzer.checks.base import BaseCheck
from linux_analyzer.system.users.accounts import get_local_users


class UserAccountsCheck(BaseCheck):

  def run(self, context: ExecutionContext) -> list[Finding]:
    findings: list[Finding] = []

    users = get_local_users()

    for user in users:
      username = user["username"]

      # UID 0 accounts other than root
      if user["uid"] == 0 and username != "root":
        findings.append(
          Finding(
            id="USER-001",
            title="Additional UID 0 account detected",
            description="A non-root account has UID 0.",
            category="user",
            source="static.user_accounts",
            location=username,
            evidence=user,
          )
        )

      # Accounts with no password set (when known)
      if user["password_set"] is False:
        findings.append(
          Finding(
            id="USER-002",
            title="User account without password",
            description="A local user account has no password set.",
            category="user",
            source="static.user_accounts",
            location=username,
            evidence=user,
          )
        )

      return findings

