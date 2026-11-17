# <a id="VirtualGeometry_World_PlanetCellBurstJob"></a> Struct PlanetCellBurstJob

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Burst経路。managed fallbackで実行された結果を計測から識別できる。

```csharp
[BurstCompile(FloatMode = FloatMode.Strict, FloatPrecision = FloatPrecision.High, CompileSynchronously = true)]
public struct PlanetCellBurstJob : IJob
```

#### 実装するインターフェース（Implements）

IJob

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetCellBurstJob_FaceRange"></a> FaceRange

```csharp
public Vector4 FaceRange
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Frame"></a> Frame

```csharp
public PlanetCellBuildFrame Frame
```

#### 値（Field Value）

 [PlanetCellBuildFrame](VirtualGeometry.World.PlanetCellBuildFrame.md)

### <a id="VirtualGeometry_World_PlanetCellBurstJob_HasShading"></a> HasShading

```csharp
public bool HasShading
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Kernel"></a> Kernel

```csharp
public PlanetCellBurstKernel Kernel
```

#### 値（Field Value）

 [PlanetCellBurstKernel](VirtualGeometry.World.PlanetCellBurstKernel.md)

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Radius"></a> Radius

```csharp
public double Radius
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Result"></a> Result

```csharp
public NativeArray<PlanetCellNativeResult> Result
```

#### 値（Field Value）

 NativeArray<[PlanetCellNativeResult](VirtualGeometry.World.PlanetCellNativeResult.md)\>

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Skirt"></a> Skirt

```csharp
public float Skirt
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Vertices"></a> Vertices

```csharp
public NativeArray<VirtualGeometryPackedVertex> Vertices
```

#### 値（Field Value）

 NativeArray<[VirtualGeometryPackedVertex](VirtualizedGeometry.VirtualGeometryPackedVertex.md)\>

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellBurstJob_Execute"></a> Execute\(\)

<p>Implement this method to perform work on a worker thread.</p>

```csharp
public void Execute()
```
