import json
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all():
    response = client.get("/law")
    print(response.json())
    assert response.status_code == 200


def test_create_firm():
    response = client.post("/law", json = {"Law_Firm_Name":"str", "Law_Firm_Email_Address":"firm@gmail.com", "Load_Range":"10000", "Legal_Fee":"200", "Law_Firm_Priority":"str", "Remarks":"str","Law_Firm_Status":"Active",
    "Display_Hierarchy": "5"})
    print(response.json())
    assert response.status_code == 201


def test_create_firm_invalid_json():
    response = client.post("/law", json = {"Law_Firm_Name":"str", "Law_Firm_Email_Address":"firm@gmail.com", "Load_Range":"10000", "Legal_Fee":"200", "Law_Firm_Priority":"str", "Remarks":"str","Law_Firm_Status":"Active"})
    print(response.json())
    assert response.status_code == 422


def test_update_keyfirm():
    test_update= {
        "Display_Hierarchy": 3
    }
    response = client.patch("/law/1", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 200


def test_update_keyfirm_incorrect_key():
    test_update= {
        "Display_Hierarchy": 3
    }
    response = client.patch("/law/8787", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 404


def test_update_keyfirm_invalid_json():
    test_update= {
        "Hierarchy": 3
    }
    response = client.patch("/law/1", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 422


def test_update_firm():
    test_update= {
        "Law_Firm_Name": "string",
        "Law_Firm_Email_Address":"susai@gmail.com",
        "Load_Range": 1000,
        "Legal_Fee": 10,
        "Law_Firm_Priority": "string",
        "Remarks": "string",
        "Law_Firm_Status": "Active",
        "Display_Hierarchy": 0
        }
    response = client.put("/law/1", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 200


def test_update_firm_incorrect_key():
    test_update= {
        "Law_Firm_Name": "string",
        "Law_Firm_Email_Address":"susai@gmail.com",
        "Load_Range": 1000,
        "Legal_Fee": 10,
        "Law_Firm_Priority": "string",
        "Remarks": "string",
        "Law_Firm_Status": "Active",
        "Display_Hierarchy": 0
    }
    response = client.patch("/law/8787", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 404


def test_update_firm_invalid_json():
    test_update= {
        "Law_Firm_Name": "string",
        "Law_Firm_Email_Address":"susai@gmail.com",
        "Load_Range": 1000,
        "Legal_Fee": 10,
        "Law_Firm_Priority": "string",
    }
    response = client.patch("/law/1", data=json.dumps(test_update))
    print(response.json())
    assert response.status_code == 422



def test_delete_firm():
    response = client.post("/law/1")
    print(response.json())

    response = client.delete("/law/1")
    assert response.status_code == 202


def test_delete_firm_incorrect_id():
    response = client.post("/law/5678")
    print(response.json())

    response = client.post("/law5678")
    assert response.status_code == 404