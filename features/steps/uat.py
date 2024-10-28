from behave import *

import subprocess
def setup_connection():
    try:
        # Run the curl command to get backends
        result = subprocess.run(
            ['curl', 'http://127.0.0.1:5000/backends'],
            capture_output=True, text=True, check=True
        )
        return result.stdout  # Return the output of the curl command
    except subprocess.CalledProcessError as e:
        return None  # Return None if curl fails


@given('I have a connection to the loading system')
def step_1(context):
    context.connection = setup_connection()


@given('I have a connection to Archipelago')
def step_2(context):
    pass

@when('I load an Alma object from its backend')
def step_3(context):
    pass

@then('Then it reaches Archipelago')
def step_4(context):
    pass