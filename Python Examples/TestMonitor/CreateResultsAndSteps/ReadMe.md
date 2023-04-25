Test Monitor Create Results And Steps Example
=================

This is a python example demonstrating how to use the
SystemLink Enterprise Test Monitor APIs to create test results and steps.

How to run the example?
-----------------------

1. Clone _or_ download and extract the [repository source](https://github.com/ni/systemlink-enterprise-examples/archive/master.zip).
2. Install the [Python SDK](https://www.python.org/downloads/) version 3.8 or higher.
3. Install all the libraries mentioned in the [requirements.txt](../requirements.txt) by running `pip install requirements.txt` in command prompt.
4. To run the example, use the following command:

    ```
    python <filename.py> --server <url> <api_key>
    ```

    For example: `python create_results_and_steps.py --server https://my_server apiKey`.

How to generate API key?
------------------------
Please refer to this [link](https://www.ni.com/docs/en-US/bundle/systemlink-enterprise/page/creating-an-api-key.html) for generating the API key

About the Example
-----------------

This is an example of uploading test results to the SystemLink Enterprise Test Monitor service.
It simulates measuring the power output from a device and tests the measured power
to ensure it is within a specified upper and lower limit.  The power is simulated using
the simple electrical equation `P=VI` (power=voltage*current).  In this example, a random
amount of current loss and voltage loss are induced to simulate a non-ideal device.

A top level result is created containing metadata about the overall test.

The example sweeps across a range of input currents and voltages and takes measurements
for each combination. It then stores each single measurement within each test step.  The test
steps are associated with the test result, and in some cases, as child relationships
to other test steps.  Each step is uploaded to the SystemLink Enterprise server as it is generated.

At the end, the step status is evaluated to set the status of the parent step and
ultimately sets the status of the top-level test result.