# <a id="Omni_Diagnostics_OmniGpuImageMetricResult"></a> Struct OmniGpuImageMetricResult

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

```csharp
public readonly struct OmniGpuImageMetricResult
```

## コンストラクター（Constructors）

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult__ctor_System_Int64_System_Double_System_Double_UnityEngine_Vector2_UnityEngine_Vector2_System_Boolean_System_Boolean_System_Boolean_"></a> OmniGpuImageMetricResult\(long, double, double, Vector2, Vector2, bool, bool, bool\)

```csharp
public OmniGpuImageMetricResult(long comparedPixelCount, double meanAbsoluteRgbError, double ssim, Vector2 referenceLuminanceCentroid, Vector2 candidateLuminanceCentroid, bool hasNonFinite, bool hasBlackClipping, bool hasWhiteClipping)
```

#### 引数（Parameters）

`comparedPixelCount` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`meanAbsoluteRgbError` [double](https://learn.microsoft.com/dotnet/api/system.double)

`ssim` [double](https://learn.microsoft.com/dotnet/api/system.double)

`referenceLuminanceCentroid` Vector2

`candidateLuminanceCentroid` Vector2

`hasNonFinite` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasBlackClipping` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`hasWhiteClipping` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_CandidateLuminanceCentroid"></a> CandidateLuminanceCentroid

```csharp
public Vector2 CandidateLuminanceCentroid { get; }
```

#### 値（Property Value）

 Vector2

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_ComparedPixelCount"></a> ComparedPixelCount

```csharp
public long ComparedPixelCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_HasBlackClipping"></a> HasBlackClipping

```csharp
public bool HasBlackClipping { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_HasNonFinite"></a> HasNonFinite

```csharp
public bool HasNonFinite { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_HasWhiteClipping"></a> HasWhiteClipping

```csharp
public bool HasWhiteClipping { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_LuminanceCentroidDistance"></a> LuminanceCentroidDistance

```csharp
public float LuminanceCentroidDistance { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_MeanAbsoluteRgbError"></a> MeanAbsoluteRgbError

```csharp
public double MeanAbsoluteRgbError { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_ReferenceLuminanceCentroid"></a> ReferenceLuminanceCentroid

```csharp
public Vector2 ReferenceLuminanceCentroid { get; }
```

#### 値（Property Value）

 Vector2

### <a id="Omni_Diagnostics_OmniGpuImageMetricResult_Ssim"></a> Ssim

```csharp
public double Ssim { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
