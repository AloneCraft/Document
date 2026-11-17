# <a id="VirtualizedGeometry_VirtualGeometryDiagnostics"></a> Class VirtualGeometryDiagnostics

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

明示的に有効化した直前frameのmarker値。未取得のGPU時間はNaNとする。

```csharp
public static class VirtualGeometryDiagnostics
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryDiagnostics](VirtualizedGeometry.VirtualGeometryDiagnostics.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastDrawItems"></a> LastDrawItems

直近のcameraで出した描画の項目数(供給元のdraw数の合計)。

```csharp
public static int LastDrawItems
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastPairedForwardDraws"></a> LastPairedForwardDraws

直近の土星opt-in graphの選択記録数と、同じcutを消費したprepass/forward項目数。

```csharp
public static int LastPairedForwardDraws
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastPairedPrepassDraws"></a> LastPairedPrepassDraws

直近の土星opt-in graphの選択記録数と、同じcutを消費したprepass/forward項目数。

```csharp
public static int LastPairedPrepassDraws
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastPairedSelections"></a> LastPairedSelections

直近の土星opt-in graphの選択記録数と、同じcutを消費したprepass/forward項目数。

```csharp
public static int LastPairedSelections
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastRecordInfo"></a> LastRecordInfo

直近の camera の記録の状況(Player の受入の確認用)。

```csharp
public static string LastRecordInfo
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastShadowCascades"></a> LastShadowCascades

直近の主光源の影で、描いた cascade の数、選択した項目の数、描画の項目の数。0 のままなら、影の pass が何も描いていない。

```csharp
public static int LastShadowCascades
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastShadowDrawItems"></a> LastShadowDrawItems

直近の主光源の影で、描いた cascade の数、選択した項目の数、描画の項目の数。0 のままなら、影の pass が何も描いていない。

```csharp
public static int LastShadowDrawItems
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastShadowSelectItems"></a> LastShadowSelectItems

直近の主光源の影で、描いた cascade の数、選択した項目の数、描画の項目の数。0 のままなら、影の pass が何も描いていない。

```csharp
public static int LastShadowSelectItems
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_LastShadowSkipReason"></a> LastShadowSkipReason

影の段が最後に記録を打ち切った理由(記録できたときは空)。

```csharp
public static string LastShadowSkipReason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_ShadowBatchesExecuted"></a> ShadowBatchesExecuted

影の描画 pass(raster)が実行された回数と、描いた draw の数(診断)。

```csharp
public static int ShadowBatchesExecuted
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_ShadowDrawsExecuted"></a> ShadowDrawsExecuted

影の描画 pass(raster)が実行された回数と、描いた draw の数(診断)。

```csharp
public static int ShadowDrawsExecuted
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_CpuMilliseconds"></a> CpuMilliseconds

```csharp
public static double CpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_DrawDeferredGpuMilliseconds"></a> DrawDeferredGpuMilliseconds

```csharp
public static double DrawDeferredGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_DrawGpuMilliseconds"></a> DrawGpuMilliseconds

```csharp
public static double DrawGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_Enabled"></a> Enabled

```csharp
public static bool Enabled { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_GpuMilliseconds"></a> GpuMilliseconds

```csharp
public static double GpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_HzbDeferredGpuMilliseconds"></a> HzbDeferredGpuMilliseconds

```csharp
public static double HzbDeferredGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_HzbGpuMilliseconds"></a> HzbGpuMilliseconds

HZB生成・cull・描画のpassごとのGPU時間(ms)。未取得はNaN。passが複数ある描画では直近の値。

```csharp
public static double HzbGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_SelectDeferredGpuMilliseconds"></a> SelectDeferredGpuMilliseconds

```csharp
public static double SelectDeferredGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_SelectGpuMilliseconds"></a> SelectGpuMilliseconds

```csharp
public static double SelectGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualizedGeometry_VirtualGeometryDiagnostics_SelectResetGpuMilliseconds"></a> SelectResetGpuMilliseconds

階層選択の前に、material・node・page ごとの状態を 0 に戻す pass のGPU時間(ms)。

```csharp
public static double SelectResetGpuMilliseconds { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
