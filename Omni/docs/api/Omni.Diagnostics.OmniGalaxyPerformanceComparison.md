# <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison"></a> Class OmniGalaxyPerformanceComparison

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

Galaxy Player の 300 warm-up + 1,000 sample を、同一環境の baseline と比較する
専用ゲートです。既存の Saturn 用 600 sample 比較器とは契約を分離します。

```csharp
public static class OmniGalaxyPerformanceComparison
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniGalaxyPerformanceComparison](Omni.Diagnostics.OmniGalaxyPerformanceComparison.md)

## フィールド（Fields）

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_AbsoluteMaximumLimitMs"></a> AbsoluteMaximumLimitMs

```csharp
public const float AbsoluteMaximumLimitMs = 33.3
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_AbsoluteP95LimitMs"></a> AbsoluteP95LimitMs

```csharp
public const float AbsoluteP95LimitMs = 16.67
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_RelativeRegressionLimit"></a> RelativeRegressionLimit

```csharp
public const float RelativeRegressionLimit = 1.05
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_RequiredSampleFrames"></a> RequiredSampleFrames

```csharp
public const int RequiredSampleFrames = 1000
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_RequiredWarmupFrames"></a> RequiredWarmupFrames

```csharp
public const int RequiredWarmupFrames = 300
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Diagnostics_OmniGalaxyPerformanceComparison_ValidateJson_System_String_System_String_"></a> ValidateJson\(string, string\)

```csharp
public static OmniGalaxyPerformanceComparisonResult ValidateJson(string baselineJson, string candidateJson)
```

#### 引数（Parameters）

`baselineJson` [string](https://learn.microsoft.com/dotnet/api/system.string)

`candidateJson` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniGalaxyPerformanceComparisonResult](Omni.Diagnostics.OmniGalaxyPerformanceComparisonResult.md)
