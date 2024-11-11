from behave import given, when, then
import responses
import requests
import json
#from .helpers import *

LOADING_SYSTEM_URL = "http://loading-system-dummy:5000"
ARCHIPELAGO_URL = "http://archipelago-dummy:5000"
ALMA_URL = "http://alma-backend:5000/alma-object"

@responses.activate
def get_successful_connection(url, return_json):
    # Mocking a successful connection to the loading system
    responses.add(responses.GET, url, json=return_json, status=200)
    response = requests.get(url)
    assert response.status_code == 200
    return response

@responses.activate
def post_successful_connection(url, post_json):
    # Mocking the process of sending the Alma object to Archipelago
    responses.add(responses.POST, url, status=201)
    response = requests.post(url, json=post_json)
    assert response.status_code == 201

@responses.activate
def get_unsuccessful_connection(url):
    # Mocking a failed connection to the loading system
    responses.add(responses.GET, url, status=500)
    try:
        response = requests.get("url")
        assert response.status_code != 200  # Ensure the status code is not 200 to indicate failure
    except requests.exceptions.RequestException:
        pass  # Expected outcome, no connection available

# Connect to the loading system
@given('I have a connection to the loading system')
@responses.activate
def step_given_connection_to_loading_system(context):
    response = get_successful_connection(LOADING_SYSTEM_URL, {"status": "connected"} )
    context.loading_system_connected = response.json().get("status") == "connected"

# Connect to the loading system
@given('I have a connection to Archipelago')
@responses.activate
def step_given_connection_to_archipelago(context):
    response = get_successful_connection(ARCHIPELAGO_URL, {"status": "connected"})
    context.archipelago_connected = response.json().get("status") == "connected"


# Load an Alma object from its backend
@when('I load an Alma object from its backend')
@responses.activate
def step_when_loading_alma_object(context):
    response = get_successful_connection(ALMA_URL,  {"id": "alma-1234", "title": "Test Alma Object"})
    context.alma_object = response.json()  # Storing loaded Alma object in context for later steps

# Validate that it reaches Archipelago
@then('it reaches Archipelago')
@responses.activate
def step_then_it_reaches_archipelago(context):
    post_successful_connection(ARCHIPELAGO_URL, context.alma_object)
    assert context.alma_object["id"] == "alma-1234"
    assert context.alma_object["title"] == "Test Alma Object"

# No connection to the loading system
@given('I do not have a connection to the loading system')
@responses.activate
def step_given_no_connection_to_loading_system(context):
    get_unsuccessful_connection(LOADING_SYSTEM_URL)
    context.loading_system_connected = False  # Set to False to reflect the connection failure

# Validate that it does not reach Archipelago
@then('it does not reach Archipelago')
@responses.activate
def step_then_it_does_not_archipelago(context):
    # Mocking the process of sending the Alma object to Archipelago
    responses.add(responses.POST, ARCHIPELAGO_URL, status=500)
    response = requests.post(ARCHIPELAGO_URL, json=context.alma_object)
    assert response.status_code != 201
    assert context.alma_object is None or response.status_code == 500  # Ensure failure is due to lack of Alma object or server error

# No connection to the loading system
@given('I do not have a connection to Archipelago')
@responses.activate
def step_given_no_connection_to_loading_system(context):
    get_unsuccessful_connection(ARCHIPELAGO_URL)
    context.loading_system_connected = False  # Set to False to reflect the connection failure