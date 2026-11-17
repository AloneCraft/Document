# <a id="VirtualGeometry_World_PlanetCellNativeBuild"></a> Class PlanetCellNativeBuild

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

1 CellのNative入出力とhandleの所有者。通常回収は完了確認後、取消はRetireへ渡す。

```csharp
public sealed class PlanetCellNativeBuild : IDisposable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellNativeBuild](VirtualGeometry.World.PlanetCellNativeBuild.md)

#### 実装するインターフェース（Implements）

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetCellNativeBuild__ctor_VirtualGeometry_World_PlanetCellFrame__System_Int32_System_Double_System_ReadOnlySpan_System_Double__System_ReadOnlySpan_System_Double__System_Single_UnityEngine_Vector4_System_Boolean_VirtualGeometry_World_PlanetNativeHeightInputs_"></a> PlanetCellNativeBuild\(in PlanetCellFrame, int, double, ReadOnlySpan<double\>, ReadOnlySpan<double\>, float, Vector4, bool, PlanetNativeHeightInputs\)

```csharp
public PlanetCellNativeBuild(in PlanetCellFrame frame, int quads, double radius, ReadOnlySpan<double> heights, ReadOnlySpan<double> shading, float skirt, Vector4 faceRange, bool burst = true, PlanetNativeHeightInputs noise = null)
```

#### 引数（Parameters）

`frame` [PlanetCellFrame](VirtualGeometry.World.PlanetCellFrame.md)

`quads` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`heights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

`shading` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

`skirt` [float](https://learn.microsoft.com/dotnet/api/system.single)

`faceRange` Vector4

`burst` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`noise` [PlanetNativeHeightInputs](VirtualGeometry.World.PlanetNativeHeightInputs.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_MemoryLimit"></a> MemoryLimit

```csharp
public const long MemoryLimit = 16777216
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_RequestLimit"></a> RequestLimit

```csharp
public const int RequestLimit = 24
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_AllocatedBytes"></a> AllocatedBytes

```csharp
public static long AllocatedBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_CanAllocate"></a> CanAllocate

```csharp
public static bool CanAllocate { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_IsCompleted"></a> IsCompleted

```csharp
public bool IsCompleted { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_IsDisposed"></a> IsDisposed

```csharp
public bool IsDisposed { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_OwnerCount"></a> OwnerCount

```csharp
public static int OwnerCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_PeakPayloadBytes"></a> PeakPayloadBytes

```csharp
public static long PeakPayloadBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_PlatformSupported"></a> PlatformSupported

```csharp
public static bool PlatformSupported { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_CompleteAll"></a> CompleteAll\(\)

```csharp
public static void CompleteAll()
```

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_Dispose"></a> Dispose\(\)

```csharp
public void Dispose()
```

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_PumpRetired"></a> PumpRetired\(\)

```csharp
public static void PumpRetired()
```

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_RegisterPump_System_Action_"></a> RegisterPump\(Action\)

```csharp
public static void RegisterPump(Action pump)
```

#### 引数（Parameters）

`pump` [Action](https://learn.microsoft.com/dotnet/api/system.action)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_ResetPeak"></a> ResetPeak\(\)

```csharp
public static void ResetPeak()
```

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_Retire"></a> Retire\(\)

```csharp
public void Retire()
```

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_TryCollect_VirtualizedGeometry_VirtualGeometryPackedVertex____VirtualGeometry_World_PlanetCellNativeResult__VirtualizedGeometry_VirtualGeometryPackedVertex___"></a> TryCollect\(out VirtualGeometryPackedVertex\[\], out PlanetCellNativeResult, VirtualGeometryPackedVertex\[\]\)

```csharp
public bool TryCollect(out VirtualGeometryPackedVertex[] vertices, out PlanetCellNativeResult result, VirtualGeometryPackedVertex[] reuse = null)
```

#### 引数（Parameters）

`vertices` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

`result` [PlanetCellNativeResult](VirtualGeometry.World.PlanetCellNativeResult.md)

`reuse` [VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellNativeBuild_UnregisterPump_System_Action_"></a> UnregisterPump\(Action\)

```csharp
public static void UnregisterPump(Action pump)
```

#### 引数（Parameters）

`pump` [Action](https://learn.microsoft.com/dotnet/api/system.action)
