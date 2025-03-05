import pytest



#POST To Verify Login with valid details

def test_verify_login_valid(api_client):

    # Define valid login credentials 
    login_data = {
        "email": "email",   # valid email
        "password": "password"  # correct password
    }

    # Sending a POST request
    response = api_client.post("/verifyLogin", data=login_data)  

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200 (User exists)")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the correct response message
    json_data = response.json()
    
    expected_message = "User exists!"
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct success message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"





#POST To Verify Login without email parameter
  
def test_verify_login_missing_email(api_client):
    
    # Define request data without email
    login_data = {
        "password": "password"  # valid password
    }

    response = api_client.post("/verifyLogin", data=login_data)  

    # Check that the status code is 400
    if response.status_code == 400:
        print("Test passed: Status code is 400 (Bad Request)")
    else:
        assert False, f"Test failed: Expected 400, but got {response.status_code}"

    # Verify the correct error message
    json_data = response.json()
    
    expected_message = "Bad request, email or password parameter is missing in POST request."
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct error message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

    



#DELETE to verify login

def test_delete_verify_login_not_allowed(api_client):

    response = api_client.delete("/verifyLogin")  # Sending a DELETE request

    # Check that the status code is 405
    if response.status_code == 405:
        print("Test passed: Status code is 405 (Method Not Allowed)")
    else:
        assert False, f"Test failed: Expected 405, but got {response.status_code}"

    # Verify that the correct response message is returned
    json_data = response.json()
    
    expected_message = "This request method is not supported."
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct error message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"






#POST To Verify Login with invalid details

def test_verify_login_invalid_credentials(api_client):

    # Define invalid login credentials
    login_data = {
        "email": "invaliduser@example.com",  # Invalid email
        "password": "wrongpassword"          # Incorrect password
    }

    # Sending a POST request
    response = api_client.post("/verifyLogin", data=login_data) 

    # Check that the status code is 404
    if response.status_code == 404:
        print("Test passed: Status code is 404 (User not found)")
    else:
        assert False, f"Test failed: Expected 404, but got {response.status_code}"

    # Verify the correct response message
    json_data = response.json()
    
    expected_message = "User not found!"
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct error message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

 
