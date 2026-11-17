# <a id="Omni_BatchRendering_RadialBatchRuntimeCounters"></a> Struct RadialBatchRuntimeCounters

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

BRGのfail-open判断をbenchmark・検証へ渡すための不変カウンターです。
Saturnシーンの複数Camera検証では、A→B→Aの各callback数とstale view数を照合します。

```csharp
public readonly struct RadialBatchRuntimeCounters
```

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_CullingCallbackCount"></a> CullingCallbackCount

UnityがBRG callbackを呼んだ回数です。

```csharp
public int CullingCallbackCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_DrawCommandCount"></a> DrawCommandCount

実際に <xref href="UnityEngine.Rendering.BatchCullingOutputDrawCommands.drawCommandCount" data-throw-if-not-resolved="false"></xref> へ書き込んだDirect draw command数です。

```csharp
public long DrawCommandCount { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_FailOpenCount"></a> FailOpenCount

provider障害等で全Resident可視へ倒した回数です。

```csharp
public int FailOpenCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_FaultCount"></a> FaultCount

回復不能なBRG例外を記録した回数です。

```csharp
public int FaultCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_MacroOnlyCount"></a> MacroOnlyCount

MacroOnlyへ縮退した回数です。

```csharp
public int MacroOnlyCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_StaleViewCount"></a> StaleViewCount

最新frame revisionのview資源が見つからなかった回数です。

```csharp
public int StaleViewCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchRuntimeCounters_UnregisteredViewCount"></a> UnregisteredViewCount

未登録Camera viewを受けた回数です。

```csharp
public int UnregisteredViewCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
