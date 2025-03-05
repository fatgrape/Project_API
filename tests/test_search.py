import pytest




# POST To Search Product

def test_search_specific_product(api_client):

    # Define search parameters
    search_data = {"search_product": "Blue Top"}  # Searching for "Blue Top"

    response = api_client.post("/searchProduct", data=search_data)  # Sending a POST request

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the response JSON structure
    json_data = response.json()

    if "products" in json_data:
        print("Test passed: 'products' key is present in the response")
    else:
        assert False, "Test failed: Response does not contain the 'products' key"

    # Ensure 'products' is a non-empty list
    products = json_data["products"]

    if isinstance(products, list):
        print("Test passed: 'products' is a list")
    else:
        assert False, "Test failed: 'products' should be a list"

    if len(products) > 0:
        print(f"Test passed: {len(products)} products found for search term 'Blue Top'")
    else:
        assert False, "Test failed: No products found for search term 'Blue Top'"

    # Check if "Blue Top" is in the response
    found_product = None
    for product in products:
        if product.get("name") == "Blue Top":
            found_product = product
            break

    if found_product:
        print("Test passed: 'Blue Top' found in search results")
    else:
        assert False, "Test failed: 'Blue Top' not found in search results"

    # Validate product details
    expected_fields = {"id", "name", "price", "brand", "category"}

    missing_fields = expected_fields - found_product.keys()
    if not missing_fields:
        print("Test passed: 'Blue Top' contains all required fields")
    else:
        assert False, f"Test failed: 'Blue Top' is missing fields: {missing_fields}"





# POST To Search Product without search_product parameter
def test_search_product_missing_param(api_client):
    
    response = api_client.post("/searchProduct", data={})  

    # Check that the status code is 400
    if response.status_code == 400:
        print("Test passed: Status code is 400 (Bad Request)")
    else:
        assert False, f"Test failed: Expected 400, but got {response.status_code}"

    # Verify that the correct response message is returned
    json_data = response.json()
    
    expected_message = "Bad request, search_product parameter is missing in POST request."
    if "message" in json_data and json_data["message"] == expected_message:
        print("Test passed: Correct error message received")
    else:
        assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

