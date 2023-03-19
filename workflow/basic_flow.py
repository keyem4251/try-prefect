from prefect import flow

@flow
def my_favorite_function(number):
    print("What is your favorite number?")
    return number

print(my_favorite_function(42))
