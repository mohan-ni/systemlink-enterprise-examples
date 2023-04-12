import uuid
import sys
import os
import datetime

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import test_data_manager_client

def main():

    try:

        test_result = {
            "programName": "Power Test",
            "status": {
            "statusType": "RUNNING",
            "statusName": "Running"
            },
            "systemId": None,
            "hostName": None,
            "properties":None,
            "serialNumber": str(uuid.uuid4()),
            "operator": "John Smith",
            "partNumber": "NI-ABC-123-PWR1",
            "fileIds":None,
            "startedAt": str(datetime.datetime.now()),
            "totalTimeInSeconds": 0.0
        }

        # create test result
        response = test_data_manager_client.create_results(results=[test_result])
        test_result = response["results"][0]
        
        print(f"The test result has been under part number={test_result['partNumber']} with Id = {test_result['id']}")
        print("Press enter to delete the result")
        input()

        # delete test result
        test_data_manager_client.delete_result(test_result['id'], True)
        print(f"\nThe test result with Id = {test_result['id']} has been deleted")
        
        # create multiple test results
        print("\nCreating multiple test results.\nResult Ids has been listed down below")
        result_ids = []
        for i in range(0,5):
            test_result['programName'] = test_result['programName'] + str(i)
            response = test_data_manager_client.create_results(results=[test_result])
            test_result = response["results"][0]
            result_ids.append(test_result["id"])
            print(f"{test_result['id']}")
        
        print("\nThe multiple results has been created successfully")
        print("Please enter to delete these results")
        input()

        # Delete multiple test results
        test_data_manager_client.delete_results(result_ids, True)
        print("\nResults has been deleted successfully")
        
    except Exception as e:
        print(e)
        print("The given URL or API key might be invalid or the server might be down. Please try again after verifying the server is up and the URL or API key is valid")
        print("For more information on how to generate API key, please refer to the documentation provided.")


if __name__ == "__main__":
    main()