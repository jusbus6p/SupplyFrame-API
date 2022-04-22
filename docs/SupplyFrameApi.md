# supplyframe.SupplyFrameApi

All URIs are relative to *https://api.supplyframe.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documentationv1postman**](SupplyFrameApi.md#documentationv1postman) | **GET** /documentation/v1/postman | /documentation/v1/postman
[**normalizationv1manufacturer**](SupplyFrameApi.md#normalizationv1manufacturer) | **GET** /normalization/v1/manufacturer | /normalization/v1/manufacturer
[**parametricv1query**](SupplyFrameApi.md#parametricv1query) | **GET** /parametric/v1/query | /parametric/v1/query
[**parametricv1schemaquery**](SupplyFrameApi.md#parametricv1schemaquery) | **GET** /parametric/v1/schema/query | /parametric/v1/schema/query


# **documentationv1postman**
> documentationv1postman(token)

/documentation/v1/postman

Retrives documentation in Postman Collection v2.1 format for routes available to consumer with provided token.  Response is JSON conforming to Postman Collection v2.1 schema. 

### Example
```python
from __future__ import print_function
import time
import supplyframe
from supplyframe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = supplyframe.SupplyFrameApi()
token = 'token_example' # str | Access token provided by Supplyframe.

try:
    # /documentation/v1/postman
    api_instance.documentationv1postman(token)
except ApiException as e:
    print("Exception when calling SupplyFrameApi->documentationv1postman: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Access token provided by Supplyframe. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **normalizationv1manufacturer**
> normalizationv1manufacturer(token, uuid, query)

/normalization/v1/manufacturer

Returns normalized manufacturer metadata based on the user-provided manufacturer name or alias.  Response is JSON array containing manufacturer objects. Each manufacturer object has following keys: <table>  <tr>   <td>name</td>   <td>normalized manufacturer name</td>  </tr>  <tr>   <td>id</td>   <td>unique manufacturer id</td>  </tr> </table>  Example request:  <pre> /normalization/v1/manufacturer?query=texas&token=PROVIDED TOKEN&uuid=UNIQUE USER ID </pre>  Example response: <pre> [{  \"name\": \"Texas Instruments\",  \"id\": 2477 }] </pre> 

### Example
```python
from __future__ import print_function
import time
import supplyframe
from supplyframe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = supplyframe.SupplyFrameApi()
token = 'token_example' # str | Access token provided by Supplyframe.
uuid = 'uuid_example' # str | Unique user identifier. Non-empty string.
query = 'query_example' # str | Manufacturer name to be normalized.

try:
    # /normalization/v1/manufacturer
    api_instance.normalizationv1manufacturer(token, uuid, query)
except ApiException as e:
    print("Exception when calling SupplyFrameApi->normalizationv1manufacturer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Access token provided by Supplyframe. | 
 **uuid** | **str**| Unique user identifier. Non-empty string. | 
 **query** | **str**| Manufacturer name to be normalized. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parametricv1query**
> parametricv1query(token, uuid)

/parametric/v1/query

Retrieve part parametric data based on a set of given query constraints.  Response is a JSON object with the following keys:  <table>     <tr>         <td>metadata</td>         <td>Object containing response metadata.</td>     </tr>     <tr>         <td>response</td>         <td>Array of part data objects. Each object contains set of fields corresponding to the part's class and category. For a full list of all available fields as well as the fields specific for particular class and category please consult the /parametric/v1/schema/query route.</td>     </tr>     <tr>         <td>facet</td>         <td>Object representing faceting results (if requested).</td>     </tr> </table>   <b>Constraints</b> Constraints are set by appending query parameters with a name of the field and its expected value (example: \"Manufacturer Part Number=bav99\"). List of fields that are searchable on can be found under the searchFields section in /parametric/v1/schema/query. Multiple constraints can be set and logical AND is used between them.  <b>Multiple values search</b> Logical OR is supported on field level by providing multiple values as constraint. Number of values should not be greater than 100. Example: \"Tolerance=5.0||2.0\".  <b>Range search</b> Range search can be perform by providing lower and upper bound values separated with a dash (example: \"Modified On=2021-02-13 02:10:38-2021-02-13 03:10:38\"). Range values are inclusive. The list of fields for range search is located under the rangeFields section in /parametric/v1/schema/query. Open interval is supported by using \"*\" for upper or lower bound value, example: \"Resistance=150-*\" will return all parts with resistance of 150 and greater.  <b>Sorting</b> Results can be sorted by appending a sort parameter. Results can be sorted in an ascending or descending manner. To sort on a specific field, add parameter \"sort\" with field name as value followed with \"asc\" or \"desc\" to specify the sort order (example \"sort=Modified On desc\"). Consult sortFields in /parametric/v1/schema/query for list of supported fields. Without the sort parameter, results are sorted by default according to their popularity score. Multiple sort parameters can be used.  <b>Faceting</b> To facet on a specific field, use the parameter \"facets\" with a field name as a value. Multiple fields can be used for faceting by separating fields with \"||\". Example \"facets=Class||Category\". Consult facetFields in /parametric/v1/schema/query for list of supported fields. Facets will return up to 50 values per field.  <b>Free text search</b> Results can also be filtered by using a free text search of part descriptions by using the parameter \"term\" (example: \"term=bav99\"). Minimum length of \"term\" is 3 characters. Term value will be ignored if used in combination with parametric filtering on Class, Category, Manufacturer and Manufacturer Part Number fields. When free text search is performed resulting parts could belong to different classes and categories. Class and category fields can be used for classification.  <b>Pagination and results limiting</b> It is possible to limit number of results to be returned in a single query with a \"limit\" parameter. Limit should be a number between 1 and 100. Default value is 10.  In addition to results limiting it is possible to retrieve more than 100 results per query by using pagination. Use the parameter \"start\" to indicate the order of the first result in pagination. Start should have value between 0 and 999. By using pagination and maximum limit it's possible to return up to 1100 results per a specific query.  <b>Classes and categories</b>  Classes and categories represent hierarchy. Each class consists of set of categories. Once new class or category is added or old class or category is removed new version of route will be released.  <b>Unique part identifier</b>  Each part has \"uid\" field which could be threaded as unique identifier of part.  <b>Textual fields case sensitivity</b>  Some textual fields are case sensitive some not. For list of case insensitive textual fields consult /parametric/v1/schema/query route. All other textual fields are case sensitive.  <b>Numeric fields unit</b>  Numeric fields have implicit unit assigned to them. When using numeric fields in constraints values should be provided as number without unit. For numeric field unit consult \"fields\" part of /parametric/v1/schema/query route.  <b>Manufacturer Part Number matching</b>  Manufacturer Part Number matching has advanced logic which tries to match best part based on provided part number, similar to infix search.   <b>Simplified response</b> <pre> {     \"metadata\": {         \"timestamp\": 1643320147413     },     \"response\": [         {             \"Package Body Material\": \"PLASTIC/EPOXY\",             \"Package Image URL\": \"http://content.supplyframe.com/images/process/fit-in/100x100/p/sot23_3.jpg\",             \"Configuration\": \"SERIES CONNECTED, CENTER TAP, 2 ELEMENTS\",             \"Diode Type\": \"RECTIFIER DIODE\",             \"Surface Mount\": \"YES\",             \"Output Current-Max\": 0.2,             \"Forward Voltage-Max (VF)\": 0.715,             \"Source Url\": \"https://www.rocelec.com/part/FAIFSCBAV99?utm_source=Supplyframe&utm_medium=SEP\",             \"Reverse Recovery Time-Max\": 0.006,             \"Terminal Form\": \"GULL WING\",             \"Manufacturer\": \"Fairchild Semiconductor Corporation\",             \"Package Shape\": \"RECTANGULAR\",             \"Number of Elements\": 2,             \"Base Number\": \"BAV99\",             \"HTS Code\": \"8541.10.00.70\",             \"Manufacturer Part Number\": \"BAV99\",             \"Pin Count\": \"3\",             \"FFF Group\": \"N001013270\",             \"Number of Terminals\": \"3\",             \"Package Style\": \"SMALL OUTLINE\",             \"Rohs Code\": \"Yes\",             \"Rep Pk Reverse Voltage-Max\": 70.0,             \"Class\": \"Diodes\",             \"Reach Compliance Code\": \"compliant\",             \"Operating Temperature-Max\": 150.0,             \"Description\": \"Rectifier Diode, 2 Element, 0.2A, 70V V(RRM), Silicon, SOT-23, 3 PIN\",             \"Category\": \"Rectifier Diodes\",             \"Modified On\": \"2019-06-21 03:52:11\",             \"Terminal Finish\": \"Matte Tin (Sn)\",             \"Military Spec\": \"false\",             \"uid\": 1014837,             \"Part Life Cycle Code\": \"Transferred\",             \"Terminal Position\": \"DUAL\",             \"JESD-30 Code\": \"R-PDSO-G3\",             \"Moisture Sensitivity Level\": \"1\",             \"ECCN Code\": \"EAR99\",             \"Clean Description\": \"Diodes Rectifier Diodes\",             \"Qualification Status\": \"Not Qualified\",             \"Pbfree Code\": \"Yes\",             \"Power Dissipation-Max\": 0.35,             \"mfrid\": 1978,             \"Link Tags\": \"[BAV99]\",             \"Current Datasheet Url\": \"https://datasheet.datasheetarchive.com/originals/distributors/Datasheets-DGA14/683951.pdf\",             \"Status Code\": \"active\",             \"Additional Feature\": \"ULTRA FAST\",             \"Category Id\": 157445543,             \"Non-rep Pk Forward Current-Max\": 1.0,             \"JESD-609 Code\": \"e3\",             \"Manufacturer Package Code\": \"3LD, SOT23, JEDEC TO-236, LOW PROFILE\",             \"Time@Peak Reflow Temperature-Max (s)\": \"NOT SPECIFIED\",             \"Brand Name\": \"Fairchild Semiconductor\",             \"Peak Reflow Temperature (Cel)\": \"NOT SPECIFIED\",             \"Package Description\": \"R-PDSO-G3\",             \"Diode Element Material\": \"SILICON\",             \"Subcategory\": \"Rectifier Diodes\",             \"Part Package Code\": \"SOT-23\",             \"Functional Group\": \"A000198499\"         }     ],     \"facet\": {         \"Manufacturer\": {             \"PanJit Semiconductor\": 57,             \"Nexperia\": 46,             \"Diodes Incorporated\": 40,             \"Infineon Technologies AG\": 40,             \"onsemi\": 35         }     } } </pre>  <b>Examples</b>  Lookup for bav99 with active part lifecycle, facet on manufacturer <pre> /parametric/v1/query?Manufacturer Part Number=bav99&Part Life Cycle Code=active&facets=Manufacturer&token=PROVIDED TOKEN&uuid=UNIQUE USER ID </pre>  Free text search for 1206VA and results sorted by Capacitance in descending order <pre> /parametric/v1/query?term=1206VA&sort=Capacitance desc&token=PROVIDED TOKEN&uuid=UNIQUE USER ID </pre> 

### Example
```python
from __future__ import print_function
import time
import supplyframe
from supplyframe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = supplyframe.SupplyFrameApi()
token = 'token_example' # str | Access token provided by Supplyframe.
uuid = 'uuid_example' # str | Unique user identifier. Non-empty string.

try:
    # /parametric/v1/query
    api_instance.parametricv1query(token, uuid)
except ApiException as e:
    print("Exception when calling SupplyFrameApi->parametricv1query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Access token provided by Supplyframe. | 
 **uuid** | **str**| Unique user identifier. Non-empty string. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parametricv1schemaquery**
> parametricv1schemaquery(token)

/parametric/v1/schema/query

Describes a set of fields that can be returned by the /parametric/v1/query route and parameters that can be used for querying.  Response is a JSON object with the following keys: <table>  <tr>   <td>fields</td>   <td>name, type and unit of field that can be returned. Unit is set for some numeric fields.</td>  </tr>  <tr>   <td>classCategoryFields</td>   <td>list of fields that can be returned for each class and category</td>  </tr>  <tr>   <td>searchFields</td>   <td>list of fields that can be used for searching</td>  </tr>  <tr>   <td>sortFields</td>   <td>list of fields that can be used for sorting</td>  </tr>  <tr>   <td>rangeFields</td>   <td>list of fields that can be used for range search</td>  </tr>  <tr>   <td>facetFields</td>   <td>list of fields on which facets can be computed</td>  </tr>  <tr>   <td>caseInsensitiveFields</td>   <td>list of case-insensitive textual fields</td>  </tr> </table>   <b>Simplified response</b></br> <pre> {  \"caseInsensitiveFields\": [\"Window Dimension\", \"Circuit Protection Type\", \"Inductor Type\"],  \"classCategoryFields\": [{    \"class\": \"Amplifier Circuits\",    \"category\": \"Sample and Hold Circuits\",    \"fields\": [\"Source Sample Url\", \"Supply Current-Max\", \"Terminal Form\"]   },   {    \"class\": \"Circuit Protection\",    \"category\": \"Electric Fuses\",    \"fields\": [\"Built-in Feature\", \"Fuse Size\", \"Source Url Status Check Date\"]   },   {    \"class\": \"Connectors\",    \"category\": \"Fiber Optic Adapters\",    \"fields\": [\"Source Sample Url\", \"Manufacturer Series\", \"Manufacturer\"]   }  ],  \"searchFields\": [\"Window Dimension\", \"Circuit Protection Type\", \"Insertion Loss (Tx)\"],  \"rangeFields\": [\"Insertion Loss (Tx)\", \"Body Length\", \"Input Voltage Absolute-Max\"],  \"sortFields\": [\"Number of LEDs in Array\", \"Communication Standard\", \"Number of Outputs\"],  \"fields\": [{    \"name\": \"Circuit Protection Type\",    \"type\": \"string\"   },   {    \"name\": \"Insertion Loss (Tx)\",    \"type\": \"number\",    \"unit\": \"dB\"   },   {    \"name\": \"Body Length\",    \"type\": \"number\",    \"unit\": \"inch\"   }  ],  \"facetFields\": [\"Window Dimension\", \"Circuit Protection Type\", \"Insertion Loss (Tx)\"] } </pre> 

### Example
```python
from __future__ import print_function
import time
import supplyframe
from supplyframe.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = supplyframe.SupplyFrameApi()
token = 'token_example' # str | Access token provided by Supplyframe.

try:
    # /parametric/v1/schema/query
    api_instance.parametricv1schemaquery(token)
except ApiException as e:
    print("Exception when calling SupplyFrameApi->parametricv1schemaquery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Access token provided by Supplyframe. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

