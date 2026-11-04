# BrandingAPI

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**partialUpdateBrandingApiV1BrandingsBrandingIdPatch**](BrandingAPI.md#partialupdatebrandingapiv1brandingsbrandingidpatch) | **PATCH** /api/v1/brandings/{branding_id} | Partial Update Branding
[**updateBrandingApiV1BrandingsPost**](BrandingAPI.md#updatebrandingapiv1brandingspost) | **POST** /api/v1/brandings/ | Update Branding
[**uploadLogoApiV1BrandingsLogoPut**](BrandingAPI.md#uploadlogoapiv1brandingslogoput) | **PUT** /api/v1/brandings/logo | Upload Logo


# **partialUpdateBrandingApiV1BrandingsBrandingIdPatch**
```swift
    open class func partialUpdateBrandingApiV1BrandingsBrandingIdPatch(brandingId: String, updateBrandingDto: UpdateBrandingDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Partial Update Branding

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let brandingId = "brandingId_example" // String | 
let updateBrandingDto = UpdateBrandingDto(identity: IdentityDto(appName: "appName_example"), contactInfo: ContactInfo(supportEmail: "supportEmail_example", phone: "phone_example", address: "address_example"), themeConfig: ThemeConfig(radius: "radius_example", light: ThemeColors(background: "background_example", foreground: "foreground_example", card: "card_example", cardForeground: "cardForeground_example", popover: "popover_example", popoverForeground: "popoverForeground_example", primary: "primary_example", primaryForeground: "primaryForeground_example", secondary: "secondary_example", secondaryForeground: "secondaryForeground_example", muted: "muted_example", mutedForeground: "mutedForeground_example", accent: "accent_example", accentForeground: "accentForeground_example", destructive: "destructive_example", destructiveForeground: "destructiveForeground_example", border: "border_example", input: "input_example", ring: "ring_example", chart1: "chart1_example", chart2: "chart2_example", chart3: "chart3_example", chart4: "chart4_example", chart5: "chart5_example", sidebar: "sidebar_example", sidebarForeground: "sidebarForeground_example", sidebarPrimary: "sidebarPrimary_example", sidebarPrimaryForeground: "sidebarPrimaryForeground_example", sidebarAccent: "sidebarAccent_example", sidebarAccentForeground: "sidebarAccentForeground_example", sidebarBorder: "sidebarBorder_example", sidebarRing: "sidebarRing_example"), dark: nil), tenantId: "tenantId_example", logoUrl: "logoUrl_example", logoType: "logoType_example") // UpdateBrandingDto | 

// Partial Update Branding
BrandingAPI.partialUpdateBrandingApiV1BrandingsBrandingIdPatch(brandingId: brandingId, updateBrandingDto: updateBrandingDto) { (response, error) in
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
 **brandingId** | **String** |  | 
 **updateBrandingDto** | [**UpdateBrandingDto**](UpdateBrandingDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updateBrandingApiV1BrandingsPost**
```swift
    open class func updateBrandingApiV1BrandingsPost(updateBrandingDto: UpdateBrandingDto, completion: @escaping (_ data: Void?, _ error: Error?) -> Void)
```

Update Branding

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let updateBrandingDto = UpdateBrandingDto(identity: IdentityDto(appName: "appName_example"), contactInfo: ContactInfo(supportEmail: "supportEmail_example", phone: "phone_example", address: "address_example"), themeConfig: ThemeConfig(radius: "radius_example", light: ThemeColors(background: "background_example", foreground: "foreground_example", card: "card_example", cardForeground: "cardForeground_example", popover: "popover_example", popoverForeground: "popoverForeground_example", primary: "primary_example", primaryForeground: "primaryForeground_example", secondary: "secondary_example", secondaryForeground: "secondaryForeground_example", muted: "muted_example", mutedForeground: "mutedForeground_example", accent: "accent_example", accentForeground: "accentForeground_example", destructive: "destructive_example", destructiveForeground: "destructiveForeground_example", border: "border_example", input: "input_example", ring: "ring_example", chart1: "chart1_example", chart2: "chart2_example", chart3: "chart3_example", chart4: "chart4_example", chart5: "chart5_example", sidebar: "sidebar_example", sidebarForeground: "sidebarForeground_example", sidebarPrimary: "sidebarPrimary_example", sidebarPrimaryForeground: "sidebarPrimaryForeground_example", sidebarAccent: "sidebarAccent_example", sidebarAccentForeground: "sidebarAccentForeground_example", sidebarBorder: "sidebarBorder_example", sidebarRing: "sidebarRing_example"), dark: nil), tenantId: "tenantId_example", logoUrl: "logoUrl_example", logoType: "logoType_example") // UpdateBrandingDto | 

// Update Branding
BrandingAPI.updateBrandingApiV1BrandingsPost(updateBrandingDto: updateBrandingDto) { (response, error) in
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
 **updateBrandingDto** | [**UpdateBrandingDto**](UpdateBrandingDto.md) |  | 

### Return type

Void (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploadLogoApiV1BrandingsLogoPut**
```swift
    open class func uploadLogoApiV1BrandingsLogoPut(file: String, completion: @escaping (_ data: AnyCodable?, _ error: Error?) -> Void)
```

Upload Logo

### Example
```swift
// The following code samples are still beta. For any issue, please report via http://github.com/OpenAPITools/openapi-generator/issues/new
import OpenAPIClient

let file = "file_example" // String | 

// Upload Logo
BrandingAPI.uploadLogoApiV1BrandingsLogoPut(file: file) { (response, error) in
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
 **file** | **String** |  | 

### Return type

**AnyCodable**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

