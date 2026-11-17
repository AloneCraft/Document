# <a id="VirtualGeometry_World_PlanetCellBurstKernel"></a> Struct PlanetCellBurstKernel

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

高さ配列からの計算専用。全Native領域は外側のleaseが所有する。

```csharp
public struct PlanetCellBurstKernel
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_AssembleMarker"></a> AssembleMarker

```csharp
public static readonly ProfilerMarker AssembleMarker
```

#### 値（Field Value）

 ProfilerMarker

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_DetailMarker"></a> DetailMarker

```csharp
public static readonly ProfilerMarker DetailMarker
```

#### 値（Field Value）

 ProfilerMarker

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_NoiseLayers"></a> NoiseLayers

```csharp
[ReadOnly]
public NativeArray<PlanetHeightNoiseLayer> NoiseLayers
```

#### 値（Field Value）

 NativeArray<[PlanetHeightNoiseLayer](VirtualGeometry.World.PlanetHeightNoiseLayer.md)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_NoiseOctaves"></a> NoiseOctaves

```csharp
[ReadOnly]
public NativeArray<PlanetHeightNoiseOctave> NoiseOctaves
```

#### 値（Field Value）

 NativeArray<[PlanetHeightNoiseOctave](VirtualGeometry.World.PlanetHeightNoiseOctave.md)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_RingMarker"></a> RingMarker

```csharp
public static readonly ProfilerMarker RingMarker
```

#### 値（Field Value）

 ProfilerMarker

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_cellQuads"></a> cellQuads

```csharp
public int cellQuads
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_heightScratch"></a> heightScratch

```csharp
public NativeArray<double> heightScratch
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_nx"></a> nx

```csharp
public NativeArray<double> nx
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_ny"></a> ny

```csharp
public NativeArray<double> ny
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_nz"></a> nz

```csharp
public NativeArray<double> nz
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_offsetU"></a> offsetU

```csharp
public NativeArray<double> offsetU
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_offsetV"></a> offsetV

```csharp
public NativeArray<double> offsetV
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_px"></a> px

```csharp
public NativeArray<double> px
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_py"></a> py

```csharp
public NativeArray<double> py
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_pz"></a> pz

```csharp
public NativeArray<double> pz
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_ring"></a> ring

```csharp
public int ring
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_rx"></a> rx

```csharp
public NativeArray<double> rx
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_ry"></a> ry

```csharp
public NativeArray<double> ry
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_rz"></a> rz

```csharp
public NativeArray<double> rz
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_shadingScratch"></a> shadingScratch

```csharp
public NativeArray<double> shadingScratch
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_side"></a> side

```csharp
public int side
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_sx"></a> sx

```csharp
public NativeArray<double> sx
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_sy"></a> sy

```csharp
public NativeArray<double> sy
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_sz"></a> sz

```csharp
public NativeArray<double> sz
```

#### 値（Field Value）

 NativeArray<[double](https://learn.microsoft.com/dotnet/api/system.double)\>

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellBurstKernel_Build_VirtualGeometry_World_PlanetCellBuildFrame__System_Double_System_Boolean_System_Single_UnityEngine_Vector4_Unity_Collections_NativeArray_VirtualizedGeometry_VirtualGeometryPackedVertex__UnityEngine_Vector4__System_Double__System_Double__"></a> Build\(in PlanetCellBuildFrame, double, bool, float, Vector4, NativeArray<VirtualGeometryPackedVertex\>, out Vector4, out double, out double\)

```csharp
public bool Build(in PlanetCellBuildFrame frame, double radius, bool hasShading, float skirtDepth, Vector4 faceRange, NativeArray<VirtualGeometryPackedVertex> vertices, out Vector4 bounds, out double min, out double max)
```

#### 引数（Parameters）

`frame` [PlanetCellBuildFrame](VirtualGeometry.World.PlanetCellBuildFrame.md)

`radius` [double](https://learn.microsoft.com/dotnet/api/system.double)

`hasShading` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`skirtDepth` [float](https://learn.microsoft.com/dotnet/api/system.single)

`faceRange` Vector4

`vertices` NativeArray<[VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\>

`bounds` Vector4

`min` [double](https://learn.microsoft.com/dotnet/api/system.double)

`max` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
