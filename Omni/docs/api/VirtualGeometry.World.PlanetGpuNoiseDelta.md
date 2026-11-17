# <a id="VirtualGeometry_World_PlanetGpuNoiseDelta"></a> Class PlanetGpuNoiseDelta

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

GPU生成用のfloat演算参照。中心のノイズ値を引かず、lattice境界で分けた値の差を積分する。

```csharp
public static class PlanetGpuNoiseDelta
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetGpuNoiseDelta](VirtualGeometry.World.PlanetGpuNoiseDelta.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuNoiseDelta_MaximumDisplacement"></a> MaximumDisplacement

```csharp
public const float MaximumDisplacement = 16
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualGeometry_World_PlanetGpuNoiseDelta_MaximumSegments"></a> MaximumSegments

```csharp
public const int MaximumSegments = 52
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuNoiseDelta_TryEvaluate_System_Int64_System_Int64_System_Int64_System_UInt32_UnityEngine_Vector3_UnityEngine_Vector3_System_Single__"></a> TryEvaluate\(long, long, long, uint, Vector3, Vector3, out float\)

fractionは中心の箱内の端数。deltaはlattice単位で各軸±16以下。失敗時は差を公開しない。

```csharp
public static bool TryEvaluate(long ix, long iy, long iz, uint seed, Vector3 fraction, Vector3 delta, out float difference)
```

#### 引数（Parameters）

`ix` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`iy` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`iz` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`seed` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)

`fraction` Vector3

`delta` Vector3

`difference` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
