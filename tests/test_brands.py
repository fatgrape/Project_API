import pytest




#Get All Brands List

def test_get_all_brands(api_client):
    
    response = api_client.get("/brandsList")

    # Check if the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the response JSON structure
    json_data = response.json()

    if "brands" in json_data:
        print("Test passed: 'brands' key is present in the response")
    else:
        assert False, "Test failed: Response does not contain the 'brands' key"

    # Ensure 'brands' is a non-empty list
    brands = json_data["brands"]

    if isinstance(brands, list):
        print("Test passed: 'brands' is a list")
    else:
        assert False, "Test failed: 'brands' should be a list"

    if len(brands) > 0:
        print(f"Test passed: The brand list contains {len(brands)} brands")
    else:
        assert False, "Test failed: The brand list is empty"

    # Validate that each brand contains the required fields
    expected_fields = {"id", "brand"}
    
    for brand in brands:
        missing_fields = expected_fields - brand.keys()
        if not missing_fields:
            print(f"Test passed: Brand {brand['id']} contains all required fields")
        else:
            assert False, f"Test failed: Brand {brand['id']} is missing fields: {missing_fields}"




#PUT To All Brands List
def test_put_brands_not_allowed(api_client):
  

    # Sending a PUT request
    response = api_client.put("/brandsList")  

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
