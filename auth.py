MOCK_USERS = {
    "support": {
        "password": "support123",
        "role": "support",
        "display_name": "Support Medewerker",
        "jira_account": "support.user"
    },
    "developer": {
        "password": "dev123",
        "role": "developer",
        "display_name": "Developer",
        "jira_account": "developer.user"
    },
    "manager": {
        "password": "manager123",
        "role": "manager",
        "display_name": "Manager",
        "jira_account": "manager.user"
    }
}

def check_credentials(username: str, password: str) -> bool:
    user = MOCK_USERS.get(username)
    return user is not None and user["password"] == password

def get_user(username: str) -> dict | None:
    return MOCK_USERS.get(username)
