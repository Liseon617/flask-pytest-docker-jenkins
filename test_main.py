from main import app

def test_home_route():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_get_api_endpoint():
    with app.test_client() as c:
        response = c.get('/api/DemoApiEndpoint')
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'This is a response from a GET request.'}

def test_post_api_endpoint():
    with app.test_client() as c:
        response = c.post('/api/DemoApiEndpoint', json={
            "name": "Brian"
        })
        assert response.status_code == 200
        json_response = response.get_json()
        assert json_response == {'message': 'Nice to meet you, Brian!'}
        