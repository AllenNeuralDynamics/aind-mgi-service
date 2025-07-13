# aind_mgi_service_async_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allele_info**](DefaultApi.md#get_allele_info) | **GET** /allele_info/{allele_name} | Get Allele Info


# **get_allele_info**
> List[MgiSummaryRow] get_allele_info(allele_name)

Get Allele Info

## Allele Info
Retrieve MGI allele information.

### Example


```python
import aind_mgi_service_async_client
from aind_mgi_service_async_client.models.mgi_summary_row import MgiSummaryRow
from aind_mgi_service_async_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = aind_mgi_service_async_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with aind_mgi_service_async_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aind_mgi_service_async_client.DefaultApi(api_client)
    allele_name = 'Parvalbumin-IRES-Cre' # str | 

    try:
        # Get Allele Info
        api_response = api_instance.get_allele_info(allele_name)
        print("The response of DefaultApi->get_allele_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_allele_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allele_name** | **str**|  | 

### Return type

[**List[MgiSummaryRow]**](MgiSummaryRow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

