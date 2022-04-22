# coding: utf-8

# flake8: noqa

"""
    Supplyframe API

    <h2>Supplyframe API Gateway</h2>  Collection of Supplyframe endpoints exposed through the Supplyframe API Gateway.  <h3>Authorization</h3>  All requests should be authorized with parameter \"token\" set to value provided by Supplyframe. In addition to \"token,\" for routes that are intended to be used by end-user applications, parameter \"uuid\" is required. \"uuid\" should represent a unique identifier of the end-user. It can be generated as a random string that's unique for the duration of the user session, and should not contain any PII information.  <h3>Response</h3>  Response is a JSON object. Response should not be consumed if the status code has a value other than 200.  <h3>Status codes returned by API</h3>  <table>     <tr>         <td>200</td>         <td>valid response, consume body</td>     </tr>     <tr>         <td>400</td>         <td>bad request</td>     </tr>     <tr>         <td>401</td>         <td>unauthorized request</td>     </tr>     <tr>         <td>404</td>         <td>route does not exist</td>     </tr>     <tr>         <td>429</td>         <td>too many requests. Rate limiting is based on token and uuid provided</td>     </tr>     <tr>         <td>500</td>         <td>internal server error</td>     </tr> </table>  <h3>Versioning</h3>  API is versioned. Each route has it's own version counting. For each change in API response, new parameter supported, fields added or removed new version will be released.   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.misc_api import MiscApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package