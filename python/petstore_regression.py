import requests

def test_get_pet_by_id():
    response = requests.get("https://petstore.swagger.io/v2/pet/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["name"] == "doggie"

def test_create_pet(base_url):
    # Define the payload for creating a pet
    payload = {
        "id": 1001,
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "name": "Rex",
        "photoUrls": [
            "https://example.com/rex.jpg"
        ],
        "tags": [
            {
                "id": 1,
                "name": "Labrador"
            }
        ],
        "status": "available"
    }

    # Send POST request to create a pet
    response = requests.post("{}/pet".format(base_url), json=payload)

    # Assert the response
    assert response.status_code == 200

    # Check if the created pet is the same as the payload
    created_pet = response.json()
    assert created_pet["id"] == payload["id"]
    assert created_pet["name"] == payload["name"]
    # Add more assertions as needed

    # Clean up by deleting the created pet
    pet_id = created_pet["id"]
    requests.delete("{}/pet/{}".format(base_url, pet_id))