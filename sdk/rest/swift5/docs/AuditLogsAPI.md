# AuditLogsAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadAuditLogsApiV1AuditLogsDownloadPost**](AuditLogsAPI.md#downloadauditlogsapiv1auditlogsdownloadpost) | **POST** /api/v1/audit-logs/download | Download Audit Logs
[**listAuditLogsApiV1AuditLogsGet**](AuditLogsAPI.md#listauditlogsapiv1auditlogsget) | **GET** /api/v1/audit-logs/ | List Audit Logs


# **downloadAuditLogsApiV1AuditLogsDownloadPost**
```swift
    open class func downloadAuditLogsApiV1AuditLogsDownloadPost(downloadAuditRequestDto: DownloadAuditRequestDto, completion: @escaping (_ data: DownloadResponseDto?, _ error: Error?) -> Void)
```

Download Audit Logs

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let downloadAuditRequestDto = DownloadAuditRequestDto(action: "action_example", totalRecords: 123) // DownloadAuditRequestDto | 

// Download Audit Logs
AuditLogsAPI.downloadAuditLogsApiV1AuditLogsDownloadPost(downloadAuditRequestDto: downloadAuditRequestDto) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **downloadAuditRequestDto** | [**DownloadAuditRequestDto**](DownloadAuditRequestDto.md) |  | 

### Return type

[**DownloadResponseDto**](DownloadResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listAuditLogsApiV1AuditLogsGet**
```swift
    open class func listAuditLogsApiV1AuditLogsGet(limit: Int? = nil, skip: Int? = nil, action: Action_listAuditLogsApiV1AuditLogsGet? = nil, completion: @escaping (_ data: AuditLogListDto?, _ error: Error?) -> Void)
```

List Audit Logs

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let limit = 987 // Int |  (optional) (default to 10)
let skip = 987 // Int |  (optional) (default to 0)
let action = "action_example" // String |  (optional)

// List Audit Logs
AuditLogsAPI.listAuditLogsApiV1AuditLogsGet(limit: limit, skip: skip, action: action) { (response, error) in
    guard error == nil else {
        print(error)
        return
    }

    if (response) {
        dump(response)
    }
}
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **Int** |  | [optional] [default to 10]
 **skip** | **Int** |  | [optional] [default to 0]
 **action** | **String** |  | [optional] 

### Return type

[**AuditLogListDto**](AuditLogListDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

