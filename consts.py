# -*- coding: utf-8

from typing_extensions import Final

ONE_HOUR_SECONDS: Final = 3600
ONE_DAY_SECONDS: Final = 24 * ONE_HOUR_SECONDS
TWO_DAYS_SECONDS: Final = 2 * ONE_DAY_SECONDS
FIVE_DAYS_SECONDS: Final = 5 * ONE_DAY_SECONDS
TEN_DAYS_SECONDS: Final = 10 * ONE_DAY_SECONDS
TWENTY_DAYS_SECONDS: Final = 2 * TEN_DAYS_SECONDS

TIME_INTERVALS: Final = (
    ONE_HOUR_SECONDS,
    ONE_DAY_SECONDS,
    TWO_DAYS_SECONDS,
    FIVE_DAYS_SECONDS,
    TEN_DAYS_SECONDS,
    TWENTY_DAYS_SECONDS
)