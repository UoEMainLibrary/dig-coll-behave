from behave import given, when, then
import responses
import requests
import json
from helpers import *

LOADING_SYSTEM_URL = "http://loading-system-dummy:5000"
ARCHIPELAGO_URL = "http://archipelago-dummy:5000"
ALMA_URL = "http://alma-backend:5000/alma-object"
MEDIA_URL = "http://loading-system-dummy-media:5000"


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

# Load an Alma object from its backend
@when('I load a Goobi object through media ingest')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"ids": "123456789"})
    context.goobi_object = response.json()

# Validate that it reaches Archipelago
@then('the Goobi media reaches Archipelago')
@responses.activate
def step_then_it_reaches_archipelago(context):
    post_successful_connection(ARCHIPELAGO_URL, context.goobi_object)
    assert context.goobi_object["ids"] == "123456789"

# Validate that it does not reach Archipelago
@then('the Goobi media does not reach Archipelago')
@responses.activate
def step_then_it_does_not_archipelago(context):
    # Mocking the process of sending the Goobi object to Archipelago
    responses.add(responses.POST, ARCHIPELAGO_URL, status=500)
    response = requests.post(ARCHIPELAGO_URL, json=context.goobi_object)
    assert response.status_code != 201
    assert context.goobi_object is None or response.status_code == 500  # Ensure failure is due to lack of Alma object or server error

@when('I load a CSV object through media ingest')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"csv_id": "test_csv.csv"})
    context.csv_object = response.json()

# Validate that it reaches Archipelago
@then('the CSV media reaches Archipelago')
@responses.activate
def step_then_it_reaches_archipelago(context):
    post_successful_connection(ARCHIPELAGO_URL, context.csv_object)
    assert context.csv_object["csv_id"] == "test_csv.csv"

# Validate that it does not reach Archipelago
@then('the CSV media does not reach Archipelago')
@responses.activate
def step_then_it_does_not_archipelago(context):
    # Mocking the process of sending the Goobi object to Archipelago
    responses.add(responses.POST, ARCHIPELAGO_URL, status=500)
    response = requests.post(ARCHIPELAGO_URL, json=context.csv_object)
    assert response.status_code != 201
    assert context.csv_object is None or response.status_code == 500  # Ensure failure is due to lack of Alma object or server error

@when('I load a Goobi object through media ingest (rights)')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"ids": "123456789", "rights": "Orphan work"})
    context.goobi_object = response.json()

@then('I see the Goobi object with rights information in Archipelago')
@responses.activate
def step_then_validate_rights_info(context):
    rights_info = "Orphan work"
    # Mock sending the media object to Archipelago
    post_successful_connection(ARCHIPELAGO_URL, context.goobi_object)
    assert context.goobi_object["rights"] == rights_info, "Rights information mismatch"

@when('I load a CSV object through media ingest (rights)')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"id": "csv-test.csv",  "rights": "Orphan work"})
    context.csv_object = response.json()

@then('I see the CSV object with rights information in Archipelago')
@responses.activate
def step_then_validate_rights_info(context):
    rights_info = "Orphan work"
    # Mock sending the media object to Archipelago
    post_successful_connection(ARCHIPELAGO_URL, context.csv_object)
    assert context.csv_object["rights"] == rights_info, "Rights information mismatch"

@when('I load a Goobi object through media ingest (licence)')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"ids": "123456789", "licence": "CC-BY"})
    context.goobi_object = response.json()

@then('I see the Goobi object with licence information in Archipelago')
@responses.activate
def step_then_validate_rights_info(context):
    licence = "CC-BY"
    # Mock sending the media object to Archipelago
    post_successful_connection(ARCHIPELAGO_URL, context.goobi_object)
    assert context.goobi_object["licence"] == licence, "Licence mismatch"


@when('I load a CSV object through media ingest (licence)')
@responses.activate
def step_when_loading_goobi_media_object(context):
    response = get_successful_connection(MEDIA_URL,  {"id": "csv-test.csv", "licence": "CC-BY"})
    context.csv_object = response.json()

@then('I see the CSV object with licence information in Archipelago')
@responses.activate
def step_then_validate_rights_info(context):
    licence = "CC-BY"
    # Mock sending the media object to Archipelago
    post_successful_connection(ARCHIPELAGO_URL, context.csv_object)
    assert context.csv_object["licence"] == licence, "Licence mismatch"


@then('the Goobi media reaches Archipelago even though the record already exists')
@responses.activate
def step_then_media_reaches_archipelago_with_existing_record(context):
    context.media_attachment_data = {'catalog_id': 'existing_catalog_id'}
    response = post_successful_connection(
        MEDIA_URL,
        context.media_attachment_data
    )
    assert response.status_code != 201
    assert context.goobi_object is None or response.status_code == 500  # Ensure failure is due to lack of Alma object or server error
