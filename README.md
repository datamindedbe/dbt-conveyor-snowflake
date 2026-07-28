# ConveyorSnowflake

The dbt-conveyorsnowflake adapter plugin is a small extension on top of the dbt-snowflake adapter plugin for DBT.

It handles authentication from dbt to Snowflake when using it on Conveyor IDE's.

## Local development setup with uv

Create and activate a virtual environment, then sync dependencies from `uv.lock`:

```bash
uv venv .venv
source .venv/bin/activate
uv sync --locked
```

For more information on how to use it, check out our
[how-to-guide](https://docs.conveyordata.com/how-to-guides/conveyor-ides/dbt-snowflake) in the Conveyor docs.