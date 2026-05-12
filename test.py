import pytest
from app import app
@pytest.fixture 
def client():
    app.config['TESTING'] =True
    with app.test_client() as client:
        yield client 
#test 1
def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    data= response.get_json()
    assert data['staus'] == 'ok'
#TEST 2
def test_get_students(client):
    response = client.get('/api/students')
    assert response .status_code == 200
    data = response.get_json()
    assert isinstance(data,list)
def test_add_student(client):
    new_student = {
        'name': 'John Doe',
        'age': 20,
        'grade': 'A'
    }
    response = client.post('/api/students', json=new_student)
    assert response.status_code == 201
    data= response.get_json()
    assert data['name'] == 'John Doe'
    assert data['age'] == 20
    assert data['grade'] == 'A'
def test_add_student_missing_field(client):
    response = client.post('/api/students', json={'name': 'Jane Doe'})
    assert response.status_code == 400
    