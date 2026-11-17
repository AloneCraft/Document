# <a id="VirtualizedGeometry_VirtualGeometryStreamingController"></a> Class VirtualGeometryStreamingController

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

小容量要求queue、実async I/O、CPU cache、chunk転送、GPU完了後のslot再利用を管理する。
GPU poolはslot(metadataの割り当て単位)に区切り、pageは自分の大きさに要る数だけ連続したslotを使う。root(page 0)は先頭のslotに置く。

```csharp
public sealed class VirtualGeometryStreamingController : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryStreamingController](VirtualizedGeometry.VirtualGeometryStreamingController.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController__ctor_VirtualizedGeometry_VirtualGeometryStreamMetadata_VirtualizedGeometry_VirtualGeometryStreamingSettings_VirtualizedGeometry_IVirtualGeometryPageStore_"></a> VirtualGeometryStreamingController\(VirtualGeometryStreamMetadata, VirtualGeometryStreamingSettings, IVirtualGeometryPageStore\)

```csharp
public VirtualGeometryStreamingController(VirtualGeometryStreamMetadata metadata, VirtualGeometryStreamingSettings settings, IVirtualGeometryPageStore store)
```

#### 引数（Parameters）

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

`settings` [VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)

`store` [IVirtualGeometryPageStore](VirtualizedGeometry.IVirtualGeometryPageStore.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_FreeSlotCount"></a> FreeSlotCount

空いている slot の数(退避中の slot は含めない)。

```csharp
public int FreeSlotCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_IsFullyResident"></a> IsFullyResident

全pageがGPUへ公開済みか。そうなると新しい要求も退避も起きないため、GPU feedbackのreadbackを描画ごとに発行する必要がない。
予算がpage全体より小さい間は常にfalse。値はTickごとに更新される統計から取る。

```csharp
public bool IsFullyResident { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_IsShrinking"></a> IsShrinking

縮小の途中か。

```csharp
public bool IsShrinking { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_MaximumSlotCount"></a> MaximumSlotCount

この asset の全 page を同時に置くのに要る slot 数(これ以上には増やさない)。

```csharp
public int MaximumSlotCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_MinimumSlotCount"></a> MinimumSlotCount

root と固定 page を置いたまま、これ以上小さくできない slot の数(固定 page の最も後ろの slot の次)。

```csharp
public int MinimumSlotCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_PagesWaitingForSlots"></a> PagesWaitingForSlots

読み込み済みで要求されているのに、置く slot を得られず待っている page の数(pool が足りない、または連続した空きが無い)。

```csharp
public int PagesWaitingForSlots { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_RootReady"></a> RootReady

root と、Proxyと同じ段までの常駐pageがすべてGPUへ公開済みか。専用描画への切替条件。

```csharp
public bool RootReady { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_SlotCount"></a> SlotCount

```csharp
public int SlotCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Statistics"></a> Statistics

```csharp
public VirtualGeometryStreamingStatistics Statistics { get; }
```

#### 値（Property Value）

 [VirtualGeometryStreamingStatistics](VirtualizedGeometry.VirtualGeometryStreamingStatistics.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_UsableSlotCount"></a> UsableSlotCount

縮小の途中は、縮小の後に残る slot の数。新しい page は、この範囲だけに置く。

```csharp
public int UsableSlotCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_BeginShrink_System_Int32_"></a> BeginShrink\(int\)

slot を target 個まで減らし始める。target の後ろの slot にある page は退避(常駐のもの)または返却(転送前のもの)し、全部空いて GPU が使い終えたら <xref href="VirtualizedGeometry.VirtualGeometryStreamingController.Shrunk" data-throw-if-not-resolved="false"></xref> を呼んで減らす。
固定 page が target の後ろにあるときは始めない(false)。

```csharp
public bool BeginShrink(int target)
```

#### 引数（Parameters）

`target` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Cancel_System_Int32_"></a> Cancel\(int\)

```csharp
public void Cancel(int page)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_GetState_System_Int32_"></a> GetState\(int\)

```csharp
public VirtualGeometryPageState GetState(int page)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [VirtualGeometryPageState](VirtualizedGeometry.VirtualGeometryPageState.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Grow_System_Int32_"></a> Grow\(int\)

slot を extra 個増やす(pool の buffer を大きくした後に呼ぶ。増えた slot は空き)。pool が全 page を同時に置ける数(<xref href="VirtualizedGeometry.VirtualGeometryStreamMetadata.TotalPageSlots" data-throw-if-not-resolved="false"></xref>)以上には増やさず、増えた数を返す。
縮小の途中は増やさない(0)。

```csharp
public int Grow(int extra)
```

#### 引数（Parameters）

`extra` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_IsPinned_System_Int32_"></a> IsPinned\(int\)

```csharp
public bool IsPinned(int page)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_RefinementReserveSlots_VirtualizedGeometry_VirtualGeometryStreamMetadata_"></a> RefinementReserveSlots\(VirtualGeometryStreamMetadata\)

1 nodeを細分化するのに要るslot数の最大。細分化には全ての子のpageが要るため、子のpageのslot数の和で数える。

```csharp
public static int RefinementReserveSlots(VirtualGeometryStreamMetadata metadata)
```

#### 引数（Parameters）

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Request_System_Int32_System_Single_System_Int64_"></a> Request\(int, float, long\)

```csharp
public void Request(int page, float priority, long frame)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`frame` [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_RetryFailures"></a> RetryFailures\(\)

```csharp
public void RetryFailures()
```

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_SelectPinnedPages_VirtualizedGeometry_VirtualGeometryStreamMetadata_System_Int32_"></a> SelectPinnedPages\(VirtualGeometryStreamMetadata, int\)

起動時から常駐させ退避しないpage。rootのpageと、rootの入力を出力するgroup(1段下)のpage。
固定pageだけで予算を埋めると詳細を読めず粗いまま止まるため、1 nodeを細分化するのに要るslotを空け、入る分だけrootに近い段から固定する。

```csharp
public static bool[] SelectPinnedPages(VirtualGeometryStreamMetadata metadata, int slotCount)
```

#### 引数（Parameters）

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

`slotCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\[\]

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_SlotCountFor_VirtualizedGeometry_VirtualGeometryStreamMetadata_VirtualizedGeometry_VirtualGeometryStreamingSettings_"></a> SlotCountFor\(VirtualGeometryStreamMetadata, VirtualGeometryStreamingSettings\)

予算から確保するslot数。全pageを同時に置ける数より多くは確保しない。

```csharp
public static int SlotCountFor(VirtualGeometryStreamMetadata metadata, VirtualGeometryStreamingSettings settings)
```

#### 引数（Parameters）

`metadata` [VirtualGeometryStreamMetadata](VirtualizedGeometry.VirtualGeometryStreamMetadata.md)

`settings` [VirtualGeometryStreamingSettings](VirtualizedGeometry.VirtualGeometryStreamingSettings.md)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Tick_System_Int64_System_Int64_System_Int64_VirtualizedGeometry_IVirtualGeometryPageUploader_"></a> Tick\(long, long, long, IVirtualGeometryPageUploader\)

```csharp
public void Tick(long frame, long lastSubmitted, long completedSubmission, IVirtualGeometryPageUploader uploader)
```

#### 引数（Parameters）

`frame` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`lastSubmitted` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`completedSubmission` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`uploader` [IVirtualGeometryPageUploader](VirtualizedGeometry.IVirtualGeometryPageUploader.md)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Touch_System_Int32_System_Single_System_Int64_"></a> Touch\(int, float, long\)

```csharp
public void Touch(int page, float priority, long frame)
```

#### 引数（Parameters）

`page` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`priority` [float](https://learn.microsoft.com/dotnet/api/system.single)

`frame` [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryStreamingController_Shrunk"></a> Shrunk

縮小が終わって slot が減った frame の通知(pool の buffer を小さくする側が使う)。減った後の slot の数。

```csharp
public event Action<int> Shrunk
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>
