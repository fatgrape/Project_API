import pytest
import random





#POST To Create/Register User Account

def test_create_user_account(api_client):

    # Generate a unique email to avoid duplication
    unique_email = f"testuser{random.randint(1000, 9999)}@example.com"

    # Define user details
    user_data = {
        "name": "Test User",
        "email": unique_email,
        "password": "Test123321",
        "title": "Mr",
        "birth_date": "22",
        "birth_month": "Dec",
        "birth_year": "1474",
        "firstname": "Nikita",
        "lastname": "Smith",
        "company": "Wallester",
        "address1": "F. R. Kreutzwaldi tn 4",
        "address2": "007",
        "country": "Tallinn",
        "zipcode": "10120",
        "state": "Harjumaa",
        "city": "Tallinn",
        "mobile_number": "1234567890"
    }

    # Sending a POST request
    response = api_client.post("/createAccount", data=user_data)  

    # Check that the status code is 201
    if response.status_code == 201:
        print("Test passed: Status code is 201 (User created successfully)")
    else:
        assert False, f"Test failed: Expected 201, but got {response.status_code}"

    # Verify the correct response message
    json_data = response.json()
    
    expected_message = "User created!"
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct success message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"





#DELETE METHOD To Delete User Account

def test_delete_user_account(api_client):
    
    #User's email and password
    existing_email = "testuser@example.com"  # Replace with a real existing email
    existing_password = "Test@1234"  # Use the correct password for deletion

    #Define deletion request data
    delete_data = {
        "email": existing_email,
        "password": existing_password
    }

    # Sending a DELETE request
    response = api_client.delete("/deleteAccount", data=delete_data)  

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200 (Account deleted successfully)")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the correct response message
    json_data = response.json()
    
    expected_message = "Account deleted!"
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct success message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

    print(f"User account deleted for email: {existing_email}")





#PUT METHOD To Update User Account

def test_update_user_account(api_client):

    # Define an existing user’s email (This email should already exist)
    existing_email = "testuser@example.com"  # Replace with a real existing email

    # Define updated user details
    updated_user_data = {
        "name": "AAAAA",
        "email": existing_email,  #  Using an existing email to update details
        "password": "Test1234567",
        "title": "Mrs",
        "birth_date": "20",
        "birth_month": "June",
        "birth_year": "1992",
        "firstname": "Enzo",
        "lastname": "Ferrari",
        "company": "Google",
        "address1": "Narva 1",
        "address2": "666",
        "country": "United States",
        "zipcode": "54321",
        "state": "Ida-Vurimaa",
        "city": "Narva",
        "mobile_number": "112"
    }

    response = api_client.put("/updateAccount", data=updated_user_data)  # Sending a PUT request

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200 (User updated successfully)")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the correct response message
    json_data = response.json()
    
    expected_message = "User updated!"
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct success message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

    # Print the updated email for reference
    print(f"User updated successfully for email: {existing_email}")





#GET user account detail by email

def test_get_user_details_by_email(api_client):

    # Define an existing user's email 
    existing_email = "testuser@example.com"  # Replace with a real existing email

    # Send GET request to retrieve user details
    response = api_client.get("/getUserDetailByEmail", params={"email": existing_email})

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200 (User details retrieved successfully)")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify that the response contains user details
    json_data = response.json()

    expected_fields = {
        "id", "name", "email", "title", "birth_date", "birth_month", "birth_year",
        "firstname", "lastname", "company", "address1", "address2", "country",
        "zipcode", "state", "city", "mobile_number"
    }

    missing_fields = expected_fields - json_data.keys()
    if not missing_fields:
        print("Test passed: All required user details are present in the response")
    else:
        assert False, f"Test failed: Missing fields in response: {missing_fields}"

    # Print retrieved user details for debugging
    print(f"Retrieved user details: {json_data}")