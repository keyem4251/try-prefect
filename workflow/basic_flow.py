import requests
import os
from prefect import flow, task


@task
def call_api(url):
    response = requests.get(url)
    print(response.status_code)
    return response.json()


@task
def parse_fact(response):
    fact = response("fact")
    print(fact)
    return fact


@flow(
    name="My Example Flow",
    description="An example flow for a tutorial.",
    version=os.getenv("GIT_COMMIT_SHA")
)
def api_flow(url):
    fact_json = call_api(url)
    fact_text = parse_fact(fact_json)
    return fact_text


print(api_flow("https://catfact.ninja/fact"))
