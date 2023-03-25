import time

from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta


def cache_key_from_sum(context, parameters):
    print(parameters)
    return sum(parameters["nums"])


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=1))
def hello_task(name_input):
    print(f"Saying hello {name_input}")
    return f"hello {name_input}"


@task(cache_key_fn=cache_key_from_sum, cache_expiration=timedelta(minutes=1))
def cached_task(nums):
    print("Running an expensive operation")
    time.sleep(3)
    return sum(nums)


@flow
def hello_flow(name_input):
    hello_task(name_input=name_input)
    cached_task([3, 1])