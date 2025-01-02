from pydantic_settings import BaseSettings


class EnvVars(BaseSettings):
    JIRA_BASE_URL: str
    JIRA_PROJECT_KEY: str
    LEAD_JIRA_ID: str

    class Config:
        env_file = '.env'
