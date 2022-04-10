import requests
from jsonschema import validate
from schemas import SINGLE_USER, SINGLE_RESOURCE, DELAYED_RESPONSE
from Resp import Resp

url = "https://reqres.in/api"


def test_list_users():
    r = requests.get(url + "/users?page=2")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json(), DELAYED_RESPONSE)
    for resp in r.json()['data']:
        validate(resp, SINGLE_USER)
    response.assert_support()


def test_single_user():
    r = requests.get(url + "/users/2")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json()['data'], SINGLE_USER)
    response.assert_support()


def test_single_user_not_found():
    r = requests.get(url + "/users/23")
    response = Resp(r)
    response.assert_status_code(404)
    assert isinstance(r.json(), dict)


def test_list_resource():
    r = requests.get(url + "/unknown")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json(), DELAYED_RESPONSE)
    for resp in r.json()['data']:
        validate(resp, SINGLE_RESOURCE)
    response.assert_support()


def test_single_resource():
    r = requests.get(url + "/unknown/2")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json()["data"], SINGLE_RESOURCE)
    response.assert_support()


def test_single_resource_not_found():
    r = requests.get(url + "/unknown/23")
    response = Resp(r)
    response.assert_status_code(404)
    assert isinstance(r.json(), dict)


def test_create():
    r = requests.post(url + "/users", json={"name": "morpheus", "job": "leader"})
    response = Resp(r)
    response.assert_status_code(201)


def test_put_update():
    r = requests.put(url + "/users/2", json={"name": "morpheus", "job": "zion resident"})
    response = Resp(r)
    response.assert_status_code(200)


def test_patch_update():
    r = requests.put(url + "/users/2", json={"name": "morpheus", "job": "zion resident"})
    response = Resp(r)
    response.assert_status_code(200)


def test_delete():
    r = requests.delete(url + "/users/2")
    assert r.status_code == 204


def test_register_successful():
    r = requests.post(url + "/register",
                             json={"email": "eve.holt@reqres.in", "password": "pistol"})
    response = Resp(r)
    response.assert_status_code(200)


def test_register_unsuccessful():
    r = requests.post(url + "/register", json={"email": "sydney@fife"})
    response = Resp(r)
    response.assert_status_code(400)


def test_login_successful():
    r = requests.post(url + "/login",
                             json={"email": "eve.holt@reqres.in", "password": "cityslicka"})
    response = Resp(r)
    response.assert_status_code(200)


def test_login_unsuccessful():
    r = requests.post(url + "/login", json={"email": "peter@klaven"})
    response = Resp(r)
    response.assert_status_code(400)


def test_delayed_response():
    r = requests.get(url + "/users?delay=3")
    response = Resp(r)
    response.assert_status_code(200)
    validate(r.json(), DELAYED_RESPONSE)
    for resp in r.json()['data']:
        validate(resp, SINGLE_USER)
    response.assert_support()
