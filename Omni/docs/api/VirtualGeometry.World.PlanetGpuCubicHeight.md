# <a id="VirtualGeometry_World_PlanetGpuCubicHeight"></a> Class PlanetGpuCubicHeight

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

固定64 quad配列へ依存せず、量子化したsource格子からGPU用のimmutableな係数をコピーする。

```csharp
public static class PlanetGpuCubicHeight
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuCubicHeight](VirtualGeometry.World.PlanetGpuCubicHeight.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuCubicHeight_TryBuild_System_ReadOnlySpan_System_Int16__System_Int32_System_Single_System_Int32_System_Double_System_Double_System_Double_System_Double_System_Int32_VirtualGeometry_World_PlanetGpuCubicPatch____"></a> TryBuild\(ReadOnlySpan<short\>, int, float, int, double, double, double, double, int, out PlanetGpuCubicPatch\[\]\)

haloを含む[-1,N+1]の全格子点を覆う。未対応・無効・patch予算超過ではfalseを返し、部分snapshotを公開しない。

```csharp
public static bool TryBuild(ReadOnlySpan<short> heights, int sourceSide, float quantizationStep, int n, double centerU, double centerV, double sourceStepPerQuad, double referenceHeight, int maximumPatches, out PlanetGpuCubicPatch[] patches)
```

#### 引数（Parameters）

`heights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[short](https://learn.microsoft.com/dotnet/api/system.int16)\>

`sourceSide` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`quantizationStep` [float](https://learn.microsoft.com/dotnet/api/system.single)

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`centerU` [double](https://learn.microsoft.com/dotnet/api/system.double)

`centerV` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sourceStepPerQuad` [double](https://learn.microsoft.com/dotnet/api/system.double)

`referenceHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumPatches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`patches` [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuCubicHeight_TryBuildRegion_System_ReadOnlySpan_System_Int16__System_Int32_System_Single_System_Int32_System_Double_System_Double_System_Double_System_Double_System_Int32_System_Int32_System_Int32_System_Int32_System_Int32_VirtualGeometry_World_PlanetGpuCubicPatch____"></a> TryBuildRegion\(ReadOnlySpan<short\>, int, float, int, double, double, double, double, int, int, int, int, int, out PlanetGpuCubicPatch\[\]\)

指定した整数矩形だけを覆う。隣tileの異なるclampを、主tileごとの矩形として維持する。

```csharp
public static bool TryBuildRegion(ReadOnlySpan<short> heights, int sourceSide, float quantizationStep, int n, double centerU, double centerV, double sourceStepPerQuad, double referenceHeight, int maximumPatches, int minI, int minJ, int maxIExclusive, int maxJExclusive, out PlanetGpuCubicPatch[] patches)
```

#### 引数（Parameters）

`heights` [ReadOnlySpan](https://learn.microsoft.com/dotnet/api/system.readonlyspan\-1)<[short](https://learn.microsoft.com/dotnet/api/system.int16)\>

`sourceSide` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`quantizationStep` [float](https://learn.microsoft.com/dotnet/api/system.single)

`n` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`centerU` [double](https://learn.microsoft.com/dotnet/api/system.double)

`centerV` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sourceStepPerQuad` [double](https://learn.microsoft.com/dotnet/api/system.double)

`referenceHeight` [double](https://learn.microsoft.com/dotnet/api/system.double)

`maximumPatches` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`minI` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`minJ` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maxIExclusive` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maxJExclusive` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`patches` [PlanetGpuCubicPatch](VirtualGeometry.World.PlanetGpuCubicPatch.md)\[\]

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
