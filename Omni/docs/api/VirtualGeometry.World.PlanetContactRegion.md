# <a id="VirtualGeometry_World_PlanetContactRegion"></a> Struct PlanetContactRegion

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

接地の領域。惑星のローカル座標の点 <xref href="VirtualGeometry.World.PlanetContactRegion.Point" data-throw-if-not-resolved="false"></xref>(Logical)のまわり半径 <xref href="VirtualGeometry.World.PlanetContactRegion.Radius" data-throw-if-not-resolved="false"></xref>(m)に掛かる Cell を、
描くときにちょうど階層 <xref href="VirtualGeometry.World.PlanetContactRegion.Level" data-throw-if-not-resolved="false"></xref> にする(<xref href="VirtualGeometry.World.PlanetLayerSource.SetContactRegions(System.Collections.Generic.IReadOnlyList%7bVirtualGeometry.World.PlanetContactRegion%7d%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref>)。

```csharp
public readonly struct PlanetContactRegion
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetContactRegion__ctor_Omni_Logical_Vector3__System_Single_System_Int32_"></a> PlanetContactRegion\(in Vector3, float, int\)

```csharp
public PlanetContactRegion(in Vector3 point, float radius, int level)
```

#### 引数（Parameters）

`point` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetContactRegion_Level"></a> Level

```csharp
public readonly int Level
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetContactRegion_Point"></a> Point

```csharp
public readonly Vector3 Point
```

#### 値（Field Value）

 Vector3

### <a id="VirtualGeometry_World_PlanetContactRegion_Radius"></a> Radius

```csharp
public readonly float Radius
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
