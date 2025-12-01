from http import HTTPStatus


def test_create_user(client):

    # DRY -> Não se repita!

    # Action = Ação
    response = client.post(
        '/users/',
        json={
            'username': 'Yago Freire',
            'email': 'freireyago51@gmail.com',
            'password': '123456780',
        },
    )

    # Assert = Garanta que A é Á.
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'Yago Freire',
        'email': 'freireyago51@gmail.com',
        'id': 1,
    }


def test_read_user(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'Yago Freire',
                'email': 'freireyago51@gmail.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Marcos José',
            'email': 'marcosjose@gmail.com',
            'password': '123456780',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Marcos José',
        'email': 'marcosjose@gmail.com',
        'id': 1,
    }


def test_user_not_exists(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'Marcos José',
            'email': 'marcosjose@gmail.com',
            'password': '123456780',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'Marcos José',
        'email': 'marcosjose@gmail.com',
        'id': 1,
    }


def test_user_not_exists_on_delete(client):
    response = client.delete(
        '/users/1',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
