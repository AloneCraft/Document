# <a id="VirtualGeometry_World_PlanetGpuCubicPatch"></a> Struct PlanetGpuCubicPatch

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

整数の格子範囲と、Cell中心からの格子差で評価する高さの三次係数。定数項は基準高さからの差。

```csharp
public struct PlanetGpuCubicPatch
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_C0"></a> C0

```csharp
public Vector4 C0
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_C1"></a> C1

```csharp
public Vector4 C1
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_C2"></a> C2

```csharp
public Vector4 C2
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_C3"></a> C3

```csharp
public Vector4 C3
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_MaxIExclusive"></a> MaxIExclusive

```csharp
public int MaxIExclusive
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_MaxJExclusive"></a> MaxJExclusive

```csharp
public int MaxJExclusive
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_MinI"></a> MinI

```csharp
public int MinI
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_MinJ"></a> MinJ

```csharp
public int MinJ
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_Stride"></a> Stride

```csharp
public const int Stride = 80
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_Contains_System_Int32_System_Int32_"></a> Contains\(int, int\)

```csharp
public bool Contains(int i, int j)
```

#### 引数（Parameters）

`i` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`j` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetGpuCubicPatch_Evaluate_System_Single_System_Single_"></a> Evaluate\(float, float\)

```csharp
public float Evaluate(float x, float y)
```

#### 引数（Parameters）

`x` [float](https://learn.microsoft.com/dotnet/api/system.single)

`y` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
