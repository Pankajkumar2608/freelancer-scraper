# fetcher/ratelimiter.py

from ratelimit import limits, sleep_and_retry


MAX_CALLS_PER_MINUTE = 30 #retry 30 times
ONE_MINUTE = 60 

@sleep_and_retry
@limits(calls=MAX_CALLS_PER_MINUTE, period=ONE_MINUTE)
def rate_limited_request(func, *args, **kwargs):
    """
    Wrap any Freelancer API call in this function to avoid exceeding rate limits [9].
    """
    return func(*args, **kwargs)
