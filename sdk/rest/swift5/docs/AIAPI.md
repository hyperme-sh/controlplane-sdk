# AIAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**askAiApiV1AiAskPost**](AIAPI.md#askaiapiv1aiaskpost) | **POST** /api/v1/ai/ask | Ask Ai
[**completeApiV1AiCompletePost**](AIAPI.md#completeapiv1aicompletepost) | **POST** /api/v1/ai/complete | Complete
[**createNewSessionApiV1AiNewSessionGet**](AIAPI.md#createnewsessionapiv1ainewsessionget) | **GET** /api/v1/ai/new_session | Create New Session
[**deleteSessionApiV1AiSessionsSessionIdDelete**](AIAPI.md#deletesessionapiv1aisessionssessioniddelete) | **DELETE** /api/v1/ai/sessions/{session_id} | Delete Session
[**getHistoryApiV1AiHistoryGet**](AIAPI.md#gethistoryapiv1aihistoryget) | **GET** /api/v1/ai/history | Get History
[**getModelsApiV1AiModelsGet**](AIAPI.md#getmodelsapiv1aimodelsget) | **GET** /api/v1/ai/models | Get Models
[**getSingleSessionApiV1AiSessionsSessionIdGet**](AIAPI.md#getsinglesessionapiv1aisessionssessionidget) | **GET** /api/v1/ai/sessions/{session_id} | Get Single Session
[**inferenceApiV1AiInferencePost**](AIAPI.md#inferenceapiv1aiinferencepost) | **POST** /api/v1/ai/inference | Inference
[**setPreferredModelApiV1AiSetModelPreferenceModelNamePut**](AIAPI.md#setpreferredmodelapiv1aisetmodelpreferencemodelnameput) | **PUT** /api/v1/ai/set_model_preference/{model_name} | Set Preferred Model


# **askAiApiV1AiAskPost**
```swift
    open class func askAiApiV1AiAskPost(aIAskRequestDto: AIAskRequestDto, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Ask Ai

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let aIAskRequestDto = AIAskRequestDto(question: "question_example", modelName: "modelName_example", sessionId: "sessionId_example") // AIAskRequestDto | 

// Ask Ai
AIAPI.askAiApiV1AiAskPost(aIAskRequestDto: aIAskRequestDto) { (response, error) in
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
 **aIAskRequestDto** | [**AIAskRequestDto**](AIAskRequestDto.md) |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **completeApiV1AiCompletePost**
```swift
    open class func completeApiV1AiCompletePost(inferenceRequest: InferenceRequest, completion: @escaping (_ data: InferenceResponse?, _ error: Error?) -> Void)
```

Complete

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let inferenceRequest = InferenceRequest(prompt: "prompt_example", model: "model_example", maxTokens: 123, billingMode: "billingMode_example", budgetId: 123, stripeCustomerId: "stripeCustomerId_example") // InferenceRequest | 

// Complete
AIAPI.completeApiV1AiCompletePost(inferenceRequest: inferenceRequest) { (response, error) in
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
 **inferenceRequest** | [**InferenceRequest**](InferenceRequest.md) |  | 

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **createNewSessionApiV1AiNewSessionGet**
```swift
    open class func createNewSessionApiV1AiNewSessionGet(completion: @escaping (_ data: NewSessionResponseDto?, _ error: Error?) -> Void)
```

Create New Session

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Create New Session
AIAPI.createNewSessionApiV1AiNewSessionGet() { (response, error) in
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
This endpoint does not need any parameter.

### Return type

[**NewSessionResponseDto**](NewSessionResponseDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deleteSessionApiV1AiSessionsSessionIdDelete**
```swift
    open class func deleteSessionApiV1AiSessionsSessionIdDelete(sessionId: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Delete Session

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sessionId = "sessionId_example" // String | 

// Delete Session
AIAPI.deleteSessionApiV1AiSessionsSessionIdDelete(sessionId: sessionId) { (response, error) in
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
 **sessionId** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getHistoryApiV1AiHistoryGet**
```swift
    open class func getHistoryApiV1AiHistoryGet(completion: @escaping (_ data: [AISessionByUserIdDto]?, _ error: Error?) -> Void)
```

Get History

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get History
AIAPI.getHistoryApiV1AiHistoryGet() { (response, error) in
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
This endpoint does not need any parameter.

### Return type

[**[AISessionByUserIdDto]**](AISessionByUserIdDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getModelsApiV1AiModelsGet**
```swift
    open class func getModelsApiV1AiModelsGet(completion: @escaping (_ data: [AIModelInfoDto]?, _ error: Error?) -> Void)
```

Get Models

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient


// Get Models
AIAPI.getModelsApiV1AiModelsGet() { (response, error) in
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
This endpoint does not need any parameter.

### Return type

[**[AIModelInfoDto]**](AIModelInfoDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getSingleSessionApiV1AiSessionsSessionIdGet**
```swift
    open class func getSingleSessionApiV1AiSessionsSessionIdGet(sessionId: String, completion: @escaping (_ data: [AIHistoriesDto]?, _ error: Error?) -> Void)
```

Get Single Session

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let sessionId = "sessionId_example" // String | 

// Get Single Session
AIAPI.getSingleSessionApiV1AiSessionsSessionIdGet(sessionId: sessionId) { (response, error) in
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
 **sessionId** | **String** |  | 

### Return type

[**[AIHistoriesDto]**](AIHistoriesDto.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inferenceApiV1AiInferencePost**
```swift
    open class func inferenceApiV1AiInferencePost(inferenceRequest: InferenceRequest, completion: @escaping (_ data: InferenceResponse?, _ error: Error?) -> Void)
```

Inference

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let inferenceRequest = InferenceRequest(prompt: "prompt_example", model: "model_example", maxTokens: 123, billingMode: "billingMode_example", budgetId: 123, stripeCustomerId: "stripeCustomerId_example") // InferenceRequest | 

// Inference
AIAPI.inferenceApiV1AiInferencePost(inferenceRequest: inferenceRequest) { (response, error) in
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
 **inferenceRequest** | [**InferenceRequest**](InferenceRequest.md) |  | 

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **setPreferredModelApiV1AiSetModelPreferenceModelNamePut**
```swift
    open class func setPreferredModelApiV1AiSetModelPreferenceModelNamePut(modelName: String, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Set Preferred Model

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let modelName = "modelName_example" // String | 

// Set Preferred Model
AIAPI.setPreferredModelApiV1AiSetModelPreferenceModelNamePut(modelName: modelName) { (response, error) in
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
 **modelName** | **String** |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

