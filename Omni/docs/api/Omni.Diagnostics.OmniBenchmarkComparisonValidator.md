# <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator"></a> Class OmniBenchmarkComparisonValidator

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

Saturn Large ResidentのFrustumOnly/Omni計測JSONを、同一コンテンツ・同一環境の
比較として成立させられるか判定します。

```csharp
public static class OmniBenchmarkComparisonValidator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniBenchmarkComparisonValidator](Omni.Diagnostics.OmniBenchmarkComparisonValidator.md)

## 補足（Remarks）

この型は<code>Assets/Omni/Development/Legacy/Saturn/Saturn.unity</code>の性能測定成果物だけを読む純粋な
バリデータです。Scene、GPU、Player設定、入力JSONを変更せず、計測値の補完や
閾値緩和も行いません。

## フィールド（Fields）

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredMaximumLimitMs"></a> RequiredMaximumLimitMs

CPU/GPU最大値の絶対性能ゲート（ms）です。

```csharp
public const float RequiredMaximumLimitMs = 33.3
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredP95LimitMs"></a> RequiredP95LimitMs

CPU/GPU P95の絶対性能ゲート（ms）です。

```csharp
public const float RequiredP95LimitMs = 16.67
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredSampleFrames"></a> RequiredSampleFrames

比較対象に必要な有効FrameTiming標本数です。

```csharp
public const int RequiredSampleFrames = 600
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredSchemaVersion"></a> RequiredSchemaVersion

比較対象に必要なベンチマークJSON schemaです。

```csharp
public const int RequiredSchemaVersion = 6
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredScreenHeight"></a> RequiredScreenHeight

比較対象に必要な画面高です。

```csharp
public const int RequiredScreenHeight = 1080
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredScreenWidth"></a> RequiredScreenWidth

比較対象に必要な画面幅です。

```csharp
public const int RequiredScreenWidth = 1920
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredSequenceTimeSeconds"></a> RequiredSequenceTimeSeconds

比較対象に必要な固定SequenceTime（秒）です。

```csharp
public const double RequiredSequenceTimeSeconds = 156
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredVSyncCount"></a> RequiredVSyncCount

比較対象に必要なvSync設定値です。

```csharp
public const int RequiredVSyncCount = 0
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RequiredWarmupFrames"></a> RequiredWarmupFrames

比較対象に必要なwarmupフレーム数です。

```csharp
public const int RequiredWarmupFrames = 120
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_RingCullingMarkerName"></a> RingCullingMarkerName

リングのカリング処理を示すProfiler marker名です。

```csharp
public const string RingCullingMarkerName = "Omni.Saturn.BRG.Culling"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Diagnostics_OmniBenchmarkComparisonValidator_ValidateJson_System_String_System_String_"></a> ValidateJson\(string, string\)

FrustumOnlyとOmniのschema v4 JSONを比較し、性能比較として有効かを判定します。

```csharp
public static OmniBenchmarkComparisonResult ValidateJson(string frustumOnlyJson, string omniJson)
```

#### 引数（Parameters）

`frustumOnlyJson` [string](https://learn.microsoft.com/dotnet/api/system.string)

<code>FrustumOnly</code>で取得したJSON本文です。null、空、schema不一致は不合格です。

`omniJson` [string](https://learn.microsoft.com/dotnet/api/system.string)

<code>Omni</code>で取得したJSON本文です。null、空、schema不一致は不合格です。

#### 戻り値（Returns）

 [OmniBenchmarkComparisonResult](Omni.Diagnostics.OmniBenchmarkComparisonResult.md)

判定と機械可読な不合格理由です。入力内容や外部状態を変更しません。
