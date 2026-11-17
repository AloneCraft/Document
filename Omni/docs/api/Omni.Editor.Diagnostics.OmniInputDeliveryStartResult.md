# <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult"></a> Class OmniInputDeliveryStartResult

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

<code>pointer-log-start</code> の応答本文（2 行目以降）の JSON です。

```csharp
[Serializable]
public sealed class OmniInputDeliveryStartResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniInputDeliveryStartResult](Omni.Editor.Diagnostics.OmniInputDeliveryStartResult.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_CurrentSchemaVersion"></a> CurrentSchemaVersion

```csharp
public const int CurrentSchemaVersion = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_filter"></a> filter

省略時は "*" です。

```csharp
public string filter
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_mainWindowRect"></a> mainWindowRect

Unity のメインウィンドウの矩形（物理ピクセル）です。

```csharp
public OmniInputDeliveryRect mainWindowRect
```

#### 値（Field Value）

 [OmniInputDeliveryRect](Omni.Editor.Diagnostics.OmniInputDeliveryRect.md)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_observation"></a> observation

```csharp
public OmniObservationReport observation
```

#### 値（Field Value）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_pixelsPerPoint"></a> pixelsPerPoint

```csharp
public float pixelsPerPoint
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_schemaVersion"></a> schemaVersion

```csharp
public int schemaVersion
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_session"></a> session

開始できたときだけ 32 桁の小文字 16 進です。

```csharp
public string session
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_startedUtcTicks"></a> startedUtcTicks

```csharp
public long startedUtcTicks
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_subscribedRects"></a> subscribedRects

```csharp
public OmniInputDeliveryWindowRect[] subscribedRects
```

#### 値（Field Value）

 [OmniInputDeliveryWindowRect](Omni.Editor.Diagnostics.OmniInputDeliveryWindowRect.md)\[\]

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryStartResult_subscribedWindows"></a> subscribedWindows

```csharp
public string[] subscribedWindows
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]
