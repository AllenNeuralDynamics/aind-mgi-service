# MgiSummaryRow

Model of Summary Row dictionary returned

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail_uri** | **str** |  | [optional] 
**feature_type** | **str** |  | [optional] 
**strand** | **str** |  | [optional] 
**chromosome** | **str** |  | [optional] 
**stars** | **str** |  | [optional] 
**best_match_text** | **str** |  | [optional] 
**best_match_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**symbol** | **str** |  | [optional] 

## Example

```python
from aind_mgi_service_client.models.mgi_summary_row import MgiSummaryRow

# TODO update the JSON string below
json = "{}"
# create an instance of MgiSummaryRow from a JSON string
mgi_summary_row_instance = MgiSummaryRow.from_json(json)
# print the JSON string representation of the object
print(MgiSummaryRow.to_json())

# convert the object into a dict
mgi_summary_row_dict = mgi_summary_row_instance.to_dict()
# create an instance of MgiSummaryRow from a dict
mgi_summary_row_from_dict = MgiSummaryRow.from_dict(mgi_summary_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


