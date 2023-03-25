from prefect import flow, task


@task(retries=2, retry_delay_seconds=60)
def failure():
    print("Running")
    raise ValueError("bad code")


@flow
def test_retries():
    return failure()
