def should_retry(failed, attempts, limit):
  return failed and (attempts < limit)