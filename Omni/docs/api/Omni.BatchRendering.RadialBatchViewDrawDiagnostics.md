# <a id="Omni_BatchRendering_RadialBatchViewDrawDiagnostics"></a> Struct RadialBatchViewDrawDiagnostics

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

Camera viewごとの最後に確定したDirect draw command数を表す不変診断値です。
A→B→A検証ではview keyとframe revisionを一緒に比較し、他Cameraの結果が混ざらないことを確認します。

```csharp
public readonly struct RadialBatchViewDrawDiagnostics
```

## コンストラクター（Constructors）

### <a id="Omni_BatchRendering_RadialBatchViewDrawDiagnostics__ctor_Omni_BatchRendering_RadialBatchViewKey__System_UInt64_System_Int32_"></a> RadialBatchViewDrawDiagnostics\(in RadialBatchViewKey, ulong, int\)

診断値を作成します。

```csharp
public RadialBatchViewDrawDiagnostics(in RadialBatchViewKey viewKey, ulong frameRevision, int lastDirectDrawCommandCount)
```

#### 引数（Parameters）

`viewKey` [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)

結果を確定したCamera viewのキーです。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

対応するCamera Snapshot revisionです。

`lastDirectDrawCommandCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

最後に出力したDirect draw command数です。

## プロパティ（Properties）

### <a id="Omni_BatchRendering_RadialBatchViewDrawDiagnostics_FrameRevision"></a> FrameRevision

このdraw command数に対応するCamera Snapshot revisionです。

```csharp
public ulong FrameRevision { get; }
```

#### 値（Property Value）

 [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

### <a id="Omni_BatchRendering_RadialBatchViewDrawDiagnostics_LastDirectDrawCommandCount"></a> LastDirectDrawCommandCount

最後に <xref href="UnityEngine.Rendering.BatchCullingOutputDrawCommands.drawCommandCount" data-throw-if-not-resolved="false"></xref> へ書き込んだDirect command数です。

```csharp
public int LastDirectDrawCommandCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_BatchRendering_RadialBatchViewDrawDiagnostics_ViewKey"></a> ViewKey

Camera viewを一意に表すEntityId由来キーです。

```csharp
public RadialBatchViewKey ViewKey { get; }
```

#### 値（Property Value）

 [RadialBatchViewKey](Omni.BatchRendering.RadialBatchViewKey.md)
