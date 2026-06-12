from dagster import Definitions
from assets import raw_data, doubled_data, total_sum

# Register assets with Dagster
defs = Definitions(
    assets=[
        raw_data,
        doubled_data,
        total_sum,
    ]
)