# AIApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
| ------------- | ------------- | ------------- |
| [**askAiApiV1AiAskPost**](AIApi.md#askAiApiV1AiAskPost) | **POST** api/v1/ai/ask | Ask Ai |
| [**completeApiV1AiCompletePost**](AIApi.md#completeApiV1AiCompletePost) | **POST** api/v1/ai/complete | Complete |
| [**createNewSessionApiV1AiNewSessionGet**](AIApi.md#createNewSessionApiV1AiNewSessionGet) | **GET** api/v1/ai/new_session | Create New Session |
| [**deleteSessionApiV1AiSessionsSessionIdDelete**](AIApi.md#deleteSessionApiV1AiSessionsSessionIdDelete) | **DELETE** api/v1/ai/sessions/{session_id} | Delete Session |
| [**getHistoryApiV1AiHistoryGet**](AIApi.md#getHistoryApiV1AiHistoryGet) | **GET** api/v1/ai/history | Get History |
| [**getModelsApiV1AiModelsGet**](AIApi.md#getModelsApiV1AiModelsGet) | **GET** api/v1/ai/models | Get Models |
| [**getSingleSessionApiV1AiSessionsSessionIdGet**](AIApi.md#getSingleSessionApiV1AiSessionsSessionIdGet) | **GET** api/v1/ai/sessions/{session_id} | Get Single Session |
| [**inferenceApiV1AiInferencePost**](AIApi.md#inferenceApiV1AiInferencePost) | **POST** api/v1/ai/inference | Inference |
| [**setPreferredModelApiV1AiSetModelPreferenceModelNamePut**](AIApi.md#setPreferredModelApiV1AiSetModelPreferenceModelNamePut) | **PUT** api/v1/ai/set_model_preference/{model_name} | Set Preferred Model |



Ask Ai

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val aiAskRequestDto : AIAskRequestDto =  // AIAskRequestDto | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.askAiApiV1AiAskPost(aiAskRequestDto)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **aiAskRequestDto** | [**AIAskRequestDto**](AIAskRequestDto.md)|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Complete

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val inferenceRequest : InferenceRequest =  // InferenceRequest | 

launch(Dispatchers.IO) {
    val result : InferenceResponse = webService.completeApiV1AiCompletePost(inferenceRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **inferenceRequest** | [**InferenceRequest**](InferenceRequest.md)|  | |

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Create New Session

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)

launch(Dispatchers.IO) {
    val result : NewSessionResponseDto = webService.createNewSessionApiV1AiNewSessionGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NewSessionResponseDto**](NewSessionResponseDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Delete Session

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val sessionId : kotlin.String = sessionId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.Any = webService.deleteSessionApiV1AiSessionsSessionIdDelete(sessionId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sessionId** | **kotlin.String**|  | |

### Return type

[**kotlin.Any**](kotlin.Any.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get History

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<AISessionByUserIdDto> = webService.getHistoryApiV1AiHistoryGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;AISessionByUserIdDto&gt;**](AISessionByUserIdDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Models

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<AIModelInfoDto> = webService.getModelsApiV1AiModelsGet()
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**kotlin.collections.List&lt;AIModelInfoDto&gt;**](AIModelInfoDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Get Single Session

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val sessionId : kotlin.String = sessionId_example // kotlin.String | 

launch(Dispatchers.IO) {
    val result : kotlin.collections.List<AIHistoriesDto> = webService.getSingleSessionApiV1AiSessionsSessionIdGet(sessionId)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **sessionId** | **kotlin.String**|  | |

### Return type

[**kotlin.collections.List&lt;AIHistoriesDto&gt;**](AIHistoriesDto.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


Inference

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val inferenceRequest : InferenceRequest =  // InferenceRequest | 

launch(Dispatchers.IO) {
    val result : InferenceResponse = webService.inferenceApiV1AiInferencePost(inferenceRequest)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **inferenceRequest** | [**InferenceRequest**](InferenceRequest.md)|  | |

### Return type

[**InferenceResponse**](InferenceResponse.md)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")
Configure BearerAuth:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


Set Preferred Model

### Example
```kotlin
// Import classes:
//import org.openapitools.client.*
//import org.openapitools.client.infrastructure.*
//import org.openapitools.client.models.*

val apiClient = ApiClient()
apiClient.setBearerToken("TOKEN")
val webService = apiClient.createWebservice(AIApi::class.java)
val modelName : kotlin.String = modelName_example // kotlin.String | 

launch(Dispatchers.IO) {
    webService.setPreferredModelApiV1AiSetModelPreferenceModelNamePut(modelName)
}
```

### Parameters
| Name | Type | Description  | Notes |
| ------------- | ------------- | ------------- | ------------- |
| **modelName** | **kotlin.String**|  | |

### Return type

null (empty response body)

### Authorization


Configure HTTPBearer:
    ApiClient().setBearerToken("TOKEN")

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

