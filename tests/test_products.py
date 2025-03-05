import pytest
import random




#GET all products
def test_get_all_products(api_client):


    #Get All Products List
    response = api_client.get("/productsList")

    # Check that the status code is 200
    if response.status_code == 200:
        print("Test passed: Status code is 200")
    else:
        assert False, f"Test failed: Expected 200, but got {response.status_code}"

    # Verify the response JSON structure
    json_data = response.json()

    if "responseCode" in json_data and json_data["responseCode"] == 200:
        print("Test passed: 'responseCode' is 200")
    else:
        assert False, f"Test failed: 'responseCode' is missing or incorrect, got {json_data.get('responseCode')}"

    if "products" in json_data:
        print("Test passed: 'products' key is present in the response")
    else:
        assert False, "Test failed: Response does not contain the 'products' key"

    # Ensure that 'products' is a non-empty list
    products = json_data["products"]

    if isinstance(products, list):
        print("Test passed: 'products' is a list")
    else:
        assert False, "Test failed: 'products' should be a list"

    if len(products) > 0:
        print(f"Test passed: The product list contains {len(products)} products")
    else:
        assert False, "Test failed: The product list is empty"

    # Validate that each product contains the required fields
    expected_product_fields = {"id", "name", "price", "brand", "category"}
    expected_category_fields = {"usertype", "category"}
    expected_usertype_fields = {"usertype"}

    for product in products:
        # Check main product fields
        missing_product_fields = expected_product_fields - product.keys()
        if not missing_product_fields:
            print(f"Test passed: Product {product['id']} contains all required fields")
        else:
            assert False, f"Test failed: Product {product['id']} is missing fields: {missing_product_fields}"

        # Check if 'category' is a dictionary
        if isinstance(product["category"], dict):
            print(f"Test passed: 'category' in product {product['id']} is a dictionary")
        else:
            assert False, f"Test failed: 'category' in product {product['id']} should be a dictionary"

        # Validate category fields
        missing_category_fields = expected_category_fields - product["category"].keys()
        if not missing_category_fields:
            print(f"Test passed: 'category' in product {product['id']} contains all required fields")
        else:
            assert False, f"Test failed: 'category' in product {product['id']} is missing fields: {missing_category_fields}"

        # Check if 'usertype' is a dictionary inside 'category'
        if isinstance(product["category"]["usertype"], dict):
            print(f"Test passed: 'usertype' in product {product['id']} is a dictionary")
        else:
            assert False, f"Test failed: 'usertype' in product {product['id']} should be a dictionary"

        # Validate 'usertype' fields
        missing_usertype_fields = expected_usertype_fields - product["category"]["usertype"].keys()
        if not missing_usertype_fields:
            print(f"Test passed: 'usertype' in product {product['id']} contains all required fields")
        else:
            assert False, f"Test failed: 'usertype' in product {product['id']} is missing fields: {missing_usertype_fields}"





# POST To All Products List

def test_post_real_product(api_client):

    # Define product details
    new_product = {
        "id": random.randint(100, 999),  
        "name": "Blue Top",
        "price": "Rs. 500",
        "brand": "Polo",
        "category": {
            "usertype": {"usertype": "Women"},
            "category": "Tops"
        }
    }
    # Sending a POST request
    response = api_client.post("/productsList", data=new_product)  

    # Check response status
    if response.status_code == 201:
        print("Test passed: Status code is 201 (Product added successfully)")
    elif response.status_code == 405:
        print("Test passed: Status code is 405 (Method Not Allowed)")
    else:
        assert False, f"Test failed: Expected 201 or 405, but got {response.status_code}"

    # Print the API response for debugging
    json_data = response.json()
    print(f"API Response: {json_data}")

    # Verify API response contains expected fields
    if response.status_code == 201:
        expected_message = "Product added successfully!"
        if "message" in json_data and json_data["message"] == expected_message:
            print("Test passed: Correct success message received")
        else:
            assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"

    elif response.status_code == 405:
        expected_message = "This request method is not supported."
        if "message" in json_data and json_data["message"] == expected_message:
            print("Test passed: API does not support POST (405)")
        else:
            assert False, f"Test failed: Expected message '{expected_message}', but got '{json_data.get('message')}'"
