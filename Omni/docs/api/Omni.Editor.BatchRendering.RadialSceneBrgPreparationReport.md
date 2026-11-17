# <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport"></a> Class RadialSceneBrgPreparationReport

Namespace: [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)  
Assembly: Omni.Editor.dll  

1回のsidecar準備の結果です。

```csharp
public sealed class RadialSceneBrgPreparationReport
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialSceneBrgPreparationReport](Omni.Editor.BatchRendering.RadialSceneBrgPreparationReport.md)

## コンストラクター（Constructors）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport__ctor_System_Int32_System_DateTime_Omni_Editor_BatchRendering_RadialSceneBrgPreparationTrigger_Omni_Editor_BatchRendering_RadialSceneBrgPreparationScope_Omni_BatchRendering_RadialSceneBatchBackendMode_System_Collections_Generic_IReadOnlyList_System_String__System_Int32_System_Int32_Omni_Editor_BatchRendering_RadialSceneBrgPreparationFailure_"></a> RadialSceneBrgPreparationReport\(int, DateTime, RadialSceneBrgPreparationTrigger, RadialSceneBrgPreparationScope, RadialSceneBatchBackendMode, IReadOnlyList<string\>, int, int, RadialSceneBrgPreparationFailure\)

結果を作成します。

```csharp
public RadialSceneBrgPreparationReport(int sequence, DateTime completedAtUtc, RadialSceneBrgPreparationTrigger trigger, RadialSceneBrgPreparationScope scope, RadialSceneBatchBackendMode backendMode, IReadOnlyList<string> scenes, int requiredMaterials, int updatedSidecars, RadialSceneBrgPreparationFailure failure)
```

#### 引数（Parameters）

`sequence` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`completedAtUtc` [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)

`trigger` [RadialSceneBrgPreparationTrigger](Omni.Editor.BatchRendering.RadialSceneBrgPreparationTrigger.md)

`scope` [RadialSceneBrgPreparationScope](Omni.Editor.BatchRendering.RadialSceneBrgPreparationScope.md)

`backendMode` RadialSceneBatchBackendMode

`scenes` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`requiredMaterials` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`updatedSidecars` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`failure` [RadialSceneBrgPreparationFailure](Omni.Editor.BatchRendering.RadialSceneBrgPreparationFailure.md)

## プロパティ（Properties）

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_BackendMode"></a> BackendMode

準備時点のScene Mesh backendです。

```csharp
public RadialSceneBatchBackendMode BackendMode { get; }
```

#### 値（Property Value）

 RadialSceneBatchBackendMode

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_CompletedAtUtc"></a> CompletedAtUtc

完了時刻（UTC）です。

```csharp
public DateTime CompletedAtUtc { get; }
```

#### 値（Property Value）

 [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Failure"></a> Failure

失敗内容です。成功時はnullです。

```csharp
public RadialSceneBrgPreparationFailure Failure { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationFailure](Omni.Editor.BatchRendering.RadialSceneBrgPreparationFailure.md)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_RequiredMaterials"></a> RequiredMaterials

sidecarが必要な元Material数です。失敗時は判明した分だけです。

```csharp
public int RequiredMaterials { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Scenes"></a> Scenes

対象にしたロード済みSceneです。

```csharp
public IReadOnlyList<string> Scenes { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Scope"></a> Scope

対象範囲です。

```csharp
public RadialSceneBrgPreparationScope Scope { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationScope](Omni.Editor.BatchRendering.RadialSceneBrgPreparationScope.md)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Sequence"></a> Sequence

このEditorセッション内の単調増加番号です。

```csharp
public int Sequence { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Succeeded"></a> Succeeded

準備が成功したかどうかです。

```csharp
public bool Succeeded { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_Trigger"></a> Trigger

開始契機です。

```csharp
public RadialSceneBrgPreparationTrigger Trigger { get; }
```

#### 値（Property Value）

 [RadialSceneBrgPreparationTrigger](Omni.Editor.BatchRendering.RadialSceneBrgPreparationTrigger.md)

### <a id="Omni_Editor_BatchRendering_RadialSceneBrgPreparationReport_UpdatedSidecars"></a> UpdatedSidecars

今回作成・更新したsidecar数です。

```csharp
public int UpdatedSidecars { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
