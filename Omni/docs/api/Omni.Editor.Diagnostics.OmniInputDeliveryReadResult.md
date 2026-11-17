# <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult"></a> Class OmniInputDeliveryReadResult

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

<code>pointer-log-read</code> の応答本文（2 行目以降）の JSON です。

```csharp
[Serializable]
public sealed class OmniInputDeliveryReadResult
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniInputDeliveryReadResult](Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.md)

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_CurrentSchemaVersion"></a> CurrentSchemaVersion

```csharp
public const int CurrentSchemaVersion = 1
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_capacity"></a> capacity

```csharp
public int capacity
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_downElements"></a> downElements

Down の記録の element を重複なく並べたものです（Overlay などに吸われたかの手掛かりです）。

```csharp
public string[] downElements
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_dropped"></a> dropped

```csharp
public long dropped
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_events"></a> events

<xref href="Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.sinceUtcTicks" data-throw-if-not-resolved="false"></xref> 以降の記録です（古い順）。

```csharp
public OmniInputDeliveryRecord[] events
```

#### 値（Field Value）

 [OmniInputDeliveryRecord](Omni.Editor.Diagnostics.OmniInputDeliveryRecord.md)\[\]

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_eventsSince"></a> eventsSince

<xref href="Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.sinceUtcTicks" data-throw-if-not-resolved="false"></xref> 以降に記録されたイベントの数です（filter に一致しないものを含みます）。

```csharp
public int eventsSince
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_expectations"></a> expectations

```csharp
public string expectations
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_filter"></a> filter

```csharp
public string filter
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_focusedWindow"></a> focusedWindow

```csharp
public string focusedWindow
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_matchingSince"></a> matchingSince

判定に使った数です。filter に一致し、期待した操作に一致する、<xref href="Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.sinceUtcTicks" data-throw-if-not-resolved="false"></xref> 以降のイベントです。

```csharp
public int matchingSince
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_observation"></a> observation

```csharp
public OmniObservationReport observation
```

#### 値（Field Value）

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_otherAutomationRequestsDuringSession"></a> otherAutomationRequestsDuringSession

```csharp
public int otherAutomationRequestsDuringSession
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_sceneViewImguiEvents"></a> sceneViewImguiEvents

source が SceneViewImgui のイベントの数です。

```csharp
public int sceneViewImguiEvents
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_schemaVersion"></a> schemaVersion

```csharp
public int schemaVersion
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_session"></a> session

```csharp
public string session
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_sinceUtcTicks"></a> sinceUtcTicks

```csharp
public long sinceUtcTicks
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_state"></a> state

<xref href="Omni.Editor.Diagnostics.OmniInputDeliverySessionState" data-throw-if-not-resolved="false"></xref> の名前です。

```csharp
public string state
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_subscribedWindows"></a> subscribedWindows

```csharp
public string[] subscribedWindows
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_testRunDuringSession"></a> testRunDuringSession

```csharp
public bool testRunDuringSession
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryReadResult_totalRecorded"></a> totalRecorded

```csharp
public long totalRecorded
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)
