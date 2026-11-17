# <a id="Omni_Diagnostics_OmniGpuImageMetrics"></a> Class OmniGpuImageMetrics

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

実GPU比較で共通利用する、割り当てを発生させない画素統計です。
mask が false の画素は背景・UIとして比較から除外します。

```csharp
public static class OmniGpuImageMetrics
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniGpuImageMetrics](Omni.Diagnostics.OmniGpuImageMetrics.md)

## メソッド（Methods）

### <a id="Omni_Diagnostics_OmniGpuImageMetrics_TryCompute_UnityEngine_Color32___UnityEngine_Color32___System_Boolean___System_Int32_System_Int32_Omni_Diagnostics_OmniGpuImageMetricResult__"></a> TryCompute\(Color32\[\], Color32\[\], bool\[\], int, int, out OmniGpuImageMetricResult\)

```csharp
public static bool TryCompute(Color32[] reference, Color32[] candidate, bool[] mask, int width, int height, out OmniGpuImageMetricResult result)
```

#### 引数（Parameters）

`reference` Color32\[\]

`candidate` Color32\[\]

`mask` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\[\]

`width` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`height` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`result` [OmniGpuImageMetricResult](Omni.Diagnostics.OmniGpuImageMetricResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
