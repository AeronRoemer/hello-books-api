def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "title": "Ocean Book", 
        "id": 1,
        "description": "watr 4evr"
    }

def test_get_no_book(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404

def test_get_two_books(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 2

def test_post_one_book(client):
    # Act
    request_body = {"title":"New", "description":""}
    response = client.post("/books", json=request_body)

    # Assert
    assert response.status_code == 201
