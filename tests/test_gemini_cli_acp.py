import json

from inspect_swe.acp._agents.gemini_cli.gemini_cli import (
    _GEMINI_DEFAULT_REQUEST_TIMEOUT_FLAG_ID,
    _GEMINI_DEFAULT_REQUEST_TIMEOUT_SECONDS,
    _gemini_experiments_json,
)


def test_gemini_experiments_json_sets_default_request_timeout() -> None:
    experiments = json.loads(_gemini_experiments_json())

    assert experiments == {
        "flags": [
            {
                "flagId": _GEMINI_DEFAULT_REQUEST_TIMEOUT_FLAG_ID,
                "intValue": str(_GEMINI_DEFAULT_REQUEST_TIMEOUT_SECONDS),
            }
        ],
        "experimentIds": [],
    }
