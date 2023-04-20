"""
SystemLink Enterprise TestMonitor delete results example

This example creates a single test result and 
deletes this created result by using Delete result Api and 
creates multiple(five) test results and 
deletes all these multiple results at a time by using delete-results Api.
"""

import uuid
import sys
import os
import datetime
from typing import Any, Tuple, Dict, List
import click

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import test_data_manager_client

def get_test_result() -> Dict:
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
        "startedAt": str(datetime.datetime.utcnow()),
        "totalTimeInSeconds": 0.0
    }

    return test_result

def create_multiple_results(result_ids: List, test_result: Dict):
    for i in range(0,5):
        test_result['programName'] = test_result['programName'] + str(i)
        response = test_data_manager_client.create_results(results=[test_result])
        test_result = response["results"][0]
        result_ids.append(test_result["id"])
        print(f"{test_result['id']}")

    return result_ids


@click.command()
@click.option("--server", help = "Enter server url")
@click.argument("api_key")
def main(server, api_key):
    """
    To run the example against a SystemLink Enterprise, the URL should include
    the scheme, host, and port if not default.\n
    For example:\n
    python create_results_and_steps.py --server https://myserver:9091 api_key.\n

    For more information on how to generate API key, please refer to the documentation provided.
    """
    test_data_manager_client.set_base_url_and_api_key(server, api_key)
    
    try:

        test_result = get_test_result()

        # create test result
        response = test_data_manager_client.create_results(results=[test_result])
        test_result = response["results"][0]
        
        print(f"The test result has been created under part number={test_result['partNumber']} with Id = {test_result['id']}")
        print("Press enter to delete the result")
        input()

        # delete test result
        test_data_manager_client.delete_result(test_result['id'], True)
        print(f"\nThe test result with Id = {test_result['id']} has been deleted")
        
        # create multiple test results
        print("\nCreating multiple test results.\nResult Ids are listed down below")
        result_ids = []
        
        result_ids = create_multiple_results(result_ids, test_result)
        
        print("\nMultiple test results has been created successfully")
        print("Please enter to delete these results")
        input()

        # Delete multiple test results
        test_data_manager_client.delete_results(result_ids, True)
        print("\nResults has been deleted successfully")
        
    except Exception as e:
        print(e)
        print("The given URL or API key might be invalid or the server might be down. Please try again after verifying the server is up and the URL or API key is valid")
        print("For more information on how to generate API key, please refer to the documentation provided.")
        print("Try 'create_results_and_steps.py --help' for help.")

if __name__ == "__main__":
    main()