import pytest
from rest_framework.test import APIClient
from radio.models import Artist, Hit


# Test for checking POST request
@pytest.mark.django_db
def test_create_hit():
    # Create a new Artist instance in the database
    artist = Artist.objects.create(first_name="DJ", last_name="TiESTo")

    # Create an API client to simulate HTTP requests
    client = APIClient()

    # Prepare the data payload for the new Hit
    data = {
        "artist_id": artist.id,
        "title": "Test Hit"
    }

    # Send a POST request to the API to create a new Hit
    response = client.post('/api/v1/hits', data, format='json')

    # Assert that the response has HTTP status 201 (Created)
    assert response.status_code == 201

    # Assert that the Hit with the given title was actually created in the database
    assert Hit.objects.filter(title="Test Hit").exists()


# Test for checking GET request
@pytest.mark.django_db
def test_get_hit_list():
    # Create a new Artist instance
    artist = Artist.objects.create(first_name="Włodzimierz", last_name="Żółtowski")

    # Create 3 Hit instances associated with the created artist
    for i in range(3):
        Hit.objects.create(title=f"Track {i}", artist=artist, title_url=f"track-{i}")

    # Create an API client to simulate HTTP requests
    client = APIClient()

    # Send a GET request to retrieve the list of Hits
    response = client.get('/api/v1/hits')

    # Assert that the response has HTTP status 200 (OK)
    assert response.status_code == 200

    # Assert that the API returned exactly 3 hits
    assert len(response.data) == 3


@pytest.mark.django_db
def test_delete_hit():
    # Create a new Artist instance
    artist = Artist.objects.create(first_name="Arctic", last_name="Monkeys")

    # Create a Hit instance associated with the artist
    hit = Hit.objects.create(title="Track to delete", artist=artist, title_url="track-to-delete")

    # Create an API client to simulate HTTP requests
    client = APIClient()

    # Send a DELETE request to remove the Hit by its title_url
    response = client.delete('/api/v1/hits/track-to-delete')

    # Assert that the response has HTTP status 200 (OK) or 204 (No Content)
    assert response.status_code in [200, 204]

    # Assert that the Hit no longer exists in the database
    assert not Hit.objects.filter(title_url="track-to-delete").exists()


