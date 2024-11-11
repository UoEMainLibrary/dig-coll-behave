import responses, requests

@responses.activate
def get_successful_connection(context, url):
    # Mocking a successful connection to the loading system
    responses.add(responses.GET, url, json={"status": "connected"}, status=200)
    response = requests.get(url)
    assert response.status_code == 200
    context.loading_system_connected = response.json().get("status") == "connected"