# <a id="VirtualizedGeometry_VirtualGeometryGpuBudget"></a> Class VirtualGeometryGpuBudget

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

ビルド済みmeshのGPU geometry(頂点・index の pool)の、全 asset を合わせた上限。asset ごとの予算(<xref href="VirtualizedGeometry.VirtualGeometryStreamingSettings.GpuGeometryBudgetBytes" data-throw-if-not-resolved="false"></xref>)は
asset の数だけ足し合わさるので、種類の多いシーンで VRAM が際限なく増える。作る pool の大きさを、この上限の残りで抑える。
残りが root の page(最小)にも足りないときは作らず(呼び出し側が Proxy へ退避する)、理由を返す。

```csharp
public static class VirtualGeometryGpuBudget
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryGpuBudget](VirtualizedGeometry.VirtualGeometryGpuBudget.md)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_DefaultLimitBytes"></a> DefaultLimitBytes

既定: Windows は 1 GiB、WebGL は 256 MiB。

```csharp
public static long DefaultLimitBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_LimitBytes"></a> LimitBytes

上限(byte)。設定していなければ <xref href="VirtualizedGeometry.VirtualGeometryGpuBudget.DefaultLimitBytes" data-throw-if-not-resolved="false"></xref>。

```csharp
public static long LimitBytes { get; set; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_ReservedBytes"></a> ReservedBytes

いま確保済みの量(byte)。

```csharp
public static long ReservedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_Release_System_Int64_"></a> Release\(long\)

```csharp
public static void Release(long bytes)
```

#### 引数（Parameters）

`bytes` [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_Reset"></a> Reset\(\)

設定を既定へ戻し、確保の記録を捨てる(試験とドメイン再読み込みの前)。

```csharp
[RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.SubsystemRegistration)]
public static void Reset()
```

### <a id="VirtualizedGeometry_VirtualGeometryGpuBudget_TryReserve_System_Int64_System_Int64_System_Int64__"></a> TryReserve\(long, long, out long\)

wanted を確保する。残りが wanted に足りなければ、残りの分だけ(wanted を超えない範囲で)確保して granted に返す。残りが minimum に満たなければ何も確保せず false。

```csharp
public static bool TryReserve(long wanted, long minimum, out long granted)
```

#### 引数（Parameters）

`wanted` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`minimum` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`granted` [long](https://learn.microsoft.com/dotnet/api/system.int64)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
