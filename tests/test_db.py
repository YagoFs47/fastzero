from dataclasses import asdict

from sqlalchemy import select

from fastzero.models import User


def test_create_user(session, mock_db_time):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='Yago Freire', email='freire@gmail.com', password='secret'
        )

        session.add(new_user)
        session.commit()

        user = session.scalar(
            select(User).where(User.username == 'Yago Freire')
        )

    assert asdict(user) == {
        'id': 1,
        'username': 'Yago Freire',
        'email': 'freire@gmail.com',
        'password': 'secret',
        'updated_at': time,
        'created_at': time,
    }
