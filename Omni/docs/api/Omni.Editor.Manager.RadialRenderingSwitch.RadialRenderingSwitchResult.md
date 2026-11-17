# <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult"></a> Struct RadialRenderingSwitch.RadialRenderingSwitchResult

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

```csharp
public readonly struct RadialRenderingSwitch.RadialRenderingSwitchResult
```

## コンストラクター（Constructors）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult__ctor_System_Boolean_Omni_Editor_Manager_RadialRenderingSwitch_State_Omni_Editor_Manager_RadialRenderingSwitch_FailureStage_System_String_System_String_System_Boolean_System_Nullable_Omni_Editor_Manager_RadialRenderingSwitch_SwitchOutcome__System_Int32_System_Int32_System_Boolean_System_Boolean_System_Boolean_System_String_"></a> RadialRenderingSwitchResult\(bool, State, FailureStage, string, string, bool, SwitchOutcome?, int, int, bool, bool, bool, string\)

```csharp
public RadialRenderingSwitchResult(bool succeeded, RadialRenderingSwitch.State finalState, RadialRenderingSwitch.FailureStage failureStage, string targetAsset, string reason, bool rollbackSucceeded, RadialRenderingSwitch.SwitchOutcome? outcome = null, int conversionErrorCount = 0, int diagnosticsApplied = 0, bool rollbackAttempted = false, bool requiresStandardRestore = false, bool manifestPersistenceDeferred = false, string manifestPersistenceReason = null)
```

#### 引数（Parameters）

`succeeded` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`finalState` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[State](Omni.Editor.Manager.RadialRenderingSwitch.State.md)

`failureStage` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[FailureStage](Omni.Editor.Manager.RadialRenderingSwitch.FailureStage.md)

`targetAsset` [string](https://learn.microsoft.com/dotnet/api/system.string)

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

`rollbackSucceeded` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`outcome` [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[SwitchOutcome](Omni.Editor.Manager.RadialRenderingSwitch.SwitchOutcome.md)?

`conversionErrorCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`diagnosticsApplied` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`rollbackAttempted` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`requiresStandardRestore` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`manifestPersistenceDeferred` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`manifestPersistenceReason` [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_ConversionErrorCount"></a> ConversionErrorCount

変換できず診断表示にした元Materialの数です（Rendererのスロットの数は<xref href="Omni.Editor.Manager.RadialRenderingSwitch.State" data-throw-if-not-resolved="false"></xref>の
    <code>Materials.DiagnosticSlots</code>）。

```csharp
public int ConversionErrorCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_DiagnosticsApplied"></a> DiagnosticsApplied

```csharp
public int DiagnosticsApplied { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_FailedAt"></a> FailedAt

```csharp
public RadialRenderingSwitch.FailureStage FailedAt { get; }
```

#### 値（Property Value）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[FailureStage](Omni.Editor.Manager.RadialRenderingSwitch.FailureStage.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_FinalState"></a> FinalState

```csharp
public RadialRenderingSwitch.State FinalState { get; }
```

#### 値（Property Value）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[State](Omni.Editor.Manager.RadialRenderingSwitch.State.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_IsCompleted"></a> IsCompleted

切替が完了したか。変換できないMaterialを診断表示にした完了
（<xref href="Omni.Editor.Manager.RadialRenderingSwitch.SwitchOutcome.CompletedWithConversionErrors" data-throw-if-not-resolved="false"></xref>、警告付き）を含みます。

```csharp
public bool IsCompleted { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_ManifestPersistenceDeferred"></a> ManifestPersistenceDeferred

```csharp
public bool ManifestPersistenceDeferred { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_ManifestPersistenceReason"></a> ManifestPersistenceReason

```csharp
public string ManifestPersistenceReason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_Outcome"></a> Outcome

```csharp
public RadialRenderingSwitch.SwitchOutcome Outcome { get; }
```

#### 値（Property Value）

 [RadialRenderingSwitch](Omni.Editor.Manager.RadialRenderingSwitch.md).[SwitchOutcome](Omni.Editor.Manager.RadialRenderingSwitch.SwitchOutcome.md)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_Reason"></a> Reason

```csharp
public string Reason { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_RequiresStandardRestore"></a> RequiresStandardRestore

```csharp
public bool RequiresStandardRestore { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_RollbackAttempted"></a> RollbackAttempted

```csharp
public bool RollbackAttempted { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_RollbackSucceeded"></a> RollbackSucceeded

```csharp
public bool RollbackSucceeded { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_Succeeded"></a> Succeeded

```csharp
public bool Succeeded { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_RadialRenderingSwitchResult_TargetAsset"></a> TargetAsset

```csharp
public string TargetAsset { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
