import responses, requests

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