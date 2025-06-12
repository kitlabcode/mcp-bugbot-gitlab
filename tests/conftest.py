import pytest

@pytest.fixture(autouse=True)
def mock_gitlab_client(monkeypatch):
    class DummyGitLabClient:
        def post_comment(self, *args, **kwargs):
            class DummyNote:
                id = 123
            return DummyNote()
        def get_merge_request(self, *args, **kwargs):
            class DummyMR:
                id = 1
                iid = 1
                title = "Dummy MR"
                author = type('Author', (), {'name': 'dummy'})
                state = "opened"
                web_url = "http://example.com"
                created_at = "2024-01-01"
                description = "Test"
            return DummyMR()
        def get_merge_request_diff(self, *args, **kwargs):
            return []
        def list_project_files(self, *args, **kwargs):
            return ["file1.py", "file2.py"]
        def get_ticket(self, *args, **kwargs):
            class DummyTicket:
                key = "TICKET-1"
                fields = type('Fields', (), {
                    'summary': 'Summary',
                    'description': 'Description',
                    'status': type('Status', (), {'name': 'Open'})(),
                    'priority': type('Priority', (), {'name': 'High'})(),
                    'assignee': type('Assignee', (), {'displayName': 'Assignee'})(),
                    'reporter': type('Reporter', (), {'displayName': 'Reporter'})(),
                    'issuetype': type('IssueType', (), {'name': 'Bug'})(),
                    'labels': [],
                    'comment': type('Comment', (), {'comments': []})(),
                    'issuelinks': []
                })
            return DummyTicket()
    monkeypatch.setattr("mcp_bugbot_gitlab.resources.get_gitlab_client", lambda: DummyGitLabClient()) 