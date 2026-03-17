"""
Configuration — all values come from .env, never hardcoded.
The API key is loaded once at startup and never logged or printed.
"""

from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Required — will raise a clear error at startup if missing
    api_key: SecretStr = Field(..., alias="GTMETRIX_API_KEY")

    # Test defaults
    default_location: int = Field(4, alias="GTMETRIX_DEFAULT_LOCATION")
    # 4 = San Antonio (GTMetrix free default); change to closest AU equivalent

    # Safety
    credit_floor: int = Field(10, alias="GTMETRIX_CREDIT_FLOOR")
    # Abort any run if remaining credits would drop below this

    # Polling
    poll_interval: int = Field(5, alias="GTMETRIX_POLL_INTERVAL")   # seconds between status checks
    max_wait: int = Field(300, alias="GTMETRIX_MAX_WAIT")            # timeout per test (seconds)

    # Bulk job
    bulk_delay_seconds: float = Field(2.0, alias="GTMETRIX_BULK_DELAY")
    # Pause between tests in bulk runs — avoids hammering the API

    # Output
    output_dir: Path = Field(Path("./reports"), alias="GTMETRIX_OUTPUT_DIR")


settings = Settings()
