from app.clients.jira_api import CustomField, IssueType, JiraAPI
from app.config.env_vars import EnvVars
from app.models.automation_task_creation_models import CreateAutomationTaskRequest


jira_labels = [
    'qat:automation',
    'qat:test:create', 'qat:test:update', 'qat:test:delete',
    'qat:util:create', 'qat:util:update', 'qat:util:delete',
    'qat:doc:create', 'qat:doc:update', 'qat:doc:delete',
    'qat:suite:smoke', 'qat:suite:regression',
    'qat:request',
    'qat:blocker',
    'qat:monitoring',
    'qat:support'
]


def create_task(
        data: CreateAutomationTaskRequest
    ):
    jira_api = JiraAPI(
        base_url=EnvVars().JIRA_BASE_URL,
        email=data.email,
        api_token=data.password
    )

    labels = ['qat:automation', data.task_type]
    if data.test_suite != '':
        labels.append(data.test_suite)

    custom_fields = {
        CustomField.TEST_CASE_KEY: data.test_key
    } if data.test_key != '' else None

    response_data = jira_api.create_issue(
        project_key=EnvVars().JIRA_PROJECT_KEY,
        issue_type=IssueType.TASK,
        summary=data.task_name,
        description=data.task_description,
        labels=labels,
        assignee_id=EnvVars().LEAD_JIRA_ID,
        custom_fields=custom_fields
    )

    if 'key' not in response_data.keys():
        return response_data
    
    jira_api.add_issue_watcher(
        issue_key=response_data['key'],
        watcher_id=EnvVars().LEAD_JIRA_ID
    )

    return f'{EnvVars().JIRA_BASE_URL}/browse/{response_data['key']}'
