import requests
import time

def testEndpoint():
    time.sleep(5)
    payload = {"str1": "I love orange", "str2": "I hate orange"}
    home_ = "http://localhost:8000/predict"
    response = requests.post(home_, json=payload)
    assert response.status_code == 200
    json_resp = response.json()
    assert isinstance(json_resp, list)
    assert 0 <= json_resp[0] <= 1
    print (response.json())

# def testPredictFailure():
#     time.sleep(5)
#     payload = {"str1": "I love orange", "str2": "I hate orange"}
#     home_ = "http://localhost:8000/predict"
#     response = requests.post(home_, json=payload)

#     print (f"Status code: {response.status_code}")
#     print (f"response: {response.text}")

#     assert response.status_code != 200
           
# testEndpoint()