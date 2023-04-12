Test Monitor Results Example
=================

This is an python example demonstrating how to use the
SystemLink Test Monitor API to create test results and steps.

Running the Example
-------------------

1. Clone _or_ download and extract the [repository source](https://github.com/ni/systemlink-enterprise-examples/archive/master.zip).
2. Install the [Python SDK](https://www.python.org/downloads/).

To run the example, use the following command:

```
python <filename.py> <url> <api_key>
```

For example: `python Delete_Results.py https://my_server apiKey`.

About the Example
-----------------

This example creates a single test result and deletes this created result by using Delete result Api and creates multiple(five) test results and deletes all these multiple results at a time by using delete-results POST Api.