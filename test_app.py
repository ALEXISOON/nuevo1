from app import app

def test_home():
    cliente = app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"Hola Mundo desde Flask" in respuesta.data

