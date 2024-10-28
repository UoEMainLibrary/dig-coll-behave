from behave import *

import subprocess

def get_backends():
    try:
        # Run the curl command to get backends
        result = subprocess.run(
            ['curl', 'http://127.0.0.1:5000/backends'],
            capture_output=True, text=True, check=True
        )
        return result.stdout  # Return the output of the curl command
    except subprocess.CalledProcessError as e:
        return None  # Return None if curl fails

import requests
from requests.exceptions import HTTPError, Timeout, RequestException


def load_volume(ids):
    url = 'http://127.0.0.1:5000/Lac/manual_ingest'
    print(f"Sending request with IDs: {ids}")

    try:
        # Send a POST request with 'ids' as form data
        response = requests.post(url, data={'ids': ids})

        # Check if the request was successful
        response.raise_for_status()  # This raises HTTPError for 4xx/5xx responses

        # Return the response object if everything is fine
        return response

    except HTTPError as http_err:
        # Check if response is None (failed request) and handle gracefully
        if response is not None:
            error_message = (
                f"HTTP error occurred: {http_err}\n"
                f"URL: {url}\n"
                f"Status Code: {response.status_code}\n"
                f"Response Headers: {response.headers}\n"
                f"Response Body: {response.text}"
            )
        else:
            error_message = (
                f"HTTP error occurred: {http_err}\n"
                f"URL: {url}\n"
                f"Response is None: No status code, headers, or body available."
            )
        print(error_message)
        raise

    except Timeout:
        print(f"Request timed out for URL: {url}")
        raise

    except RequestException as req_err:
        print(f"An error occurred during the request: {req_err}")
        raise

from pathlib import Path

def is_media_present(file_path):
    # Use Path to check if the file exists
    file = Path(file_path).expanduser()  # Expands the "~" to the user's home directory
    return file.is_file()  # Returns True if file exists, otherwise False

def are_all_media_present(file_paths):
    return all(Path(f).expanduser().is_file() for f in file_paths)


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is not False


@given('the system is fully initialised with the relevant backends')
def system_initialised(context):
    # Call the helper function
    backends = get_backends()

    # Store result in context for later use in other steps (optional)
    context.backends = backends

    # Check if the system initialization failed
    assert backends is not None, "System initialization failed: could not retrieve backends"
    assert 'failed' not in backends.lower(), "Backend system reports failure"

@given('we have all the necessary media')
def check_media_present(context):
    # Specify the file path you want to check
    media_path = '~/Pictures/bookcase.jpg'

    # Call the helper function to check if the file exists
    file_exists = is_media_present(media_path)

    # Store the result in context for later steps if needed
    context.file_exists = file_exists

    # Assert that the file exists
    assert file_exists, f"Media file {media_path} is missing"


@when('we execute the media ingest process')
def execute(context):
    ids = "126437071"  # Example ID, you can modify this or make it dynamic
    try:
        # Call the load_volume function with the given IDs
        ingest_response = load_volume(ids)

        # Store the response in the context for use in later steps
        context.ingest_response = ingest_response

        # Check if the request succeeded (status code 200)
        assert ingest_response.status_code == 200, (
            f"Media ingest failed with status code {ingest_response.status_code}. "
            f"Response body: {ingest_response.text}, Headers: {ingest_response.headers}"
        )

        # Additional assertion on response content
        assert 'failed' not in ingest_response.text.lower(), (
            f"Media ingest process returned failure response. "
            f"Response body: {ingest_response.text}"
        )

    except AssertionError as ae:
        print(f"Assertion Error: {ae}")
        raise

    except RequestException as e:
        # Catch and re-raise any errors from load_volume for better visibility
        print(f"An error occurred during media ingest: {e}")
        raise


@then('the item will appear in Archipelago')
def appear(context):
    assert not context.failed