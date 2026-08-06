from dataclasses import dataclass, field
import dbt.exceptions  # noqa
import subprocess
from dbt.adapters.snowflake import SnowflakeCredentials
import json

@dataclass
class ConveyorSnowflakeAdapterCredentials(SnowflakeCredentials):
    # We need to set the default to empty string, otherwise dbt run will complain user is not set and fail
    user: str = field(default='')
    def __post_init__(self):
        if self.oauth_client_id is None:
            raise Exception("OAuth client ID is required")
        if self.oauth_client_secret is None:
            raise Exception("OAuth client secret is required")
        args = [
            "conveyor", "ide", "snowflake-token",
            f"--snowflake-client-id={self.oauth_client_id}",
            f"--snowflake-client-secret={self.oauth_client_secret}",
            f"--snowflake-account={self.account}",
            "--quiet",
        ]
        if self.role:
            args.append(f"--snowflake-role={self.role}")
        token_output = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        last_line = token_output.stdout.rstrip().decode().splitlines()[-1]
        self.token = json.loads(last_line)["refresh_token"]
        self.user = json.loads(last_line)["username"]
        super().__post_init__()

    @property
    def type(self):
        return "conveyorsnowflake"
