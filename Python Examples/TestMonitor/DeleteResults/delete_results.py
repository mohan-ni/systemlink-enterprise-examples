import uuid
import sys
import os
import datetime

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import test_data_manager_client

def main():

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
    request_response = test_data_manager_client.delete_result(test_result['id'], True)
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
    print("Please any key to delete these results")
    input()

    # Delete multiple test results
    request_response = test_data_manager_client.delete_results(result_ids, True)
    print("\nResults has been deleted successfully")


if __name__ == "__main__":
    main()