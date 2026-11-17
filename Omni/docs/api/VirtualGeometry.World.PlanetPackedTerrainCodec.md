# <a id="VirtualGeometry_World_PlanetPackedTerrainCodec"></a> Class PlanetPackedTerrainCodec

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

12 Bの形式を検証するCPU参照。GPU pool/生成への接続は別途行う。

```csharp
public static class PlanetPackedTerrainCodec
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetPackedTerrainCodec](VirtualGeometry.World.PlanetPackedTerrainCodec.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetPackedTerrainCodec_TryPack_UnityEngine_Vector3_UnityEngine_Vector3_VirtualGeometry_World_PlanetPackedTerrainBounds__System_UInt16_VirtualGeometry_World_PlanetPackedTerrainVertex__"></a> TryPack\(Vector3, Vector3, in PlanetPackedTerrainBounds, ushort, out PlanetPackedTerrainVertex\)

```csharp
public static bool TryPack(Vector3 position, Vector3 normal, in PlanetPackedTerrainBounds bounds, ushort flags, out PlanetPackedTerrainVertex vertex)
```

#### 引数（Parameters）

`position` Vector3

`normal` Vector3

`bounds` [PlanetPackedTerrainBounds](VirtualGeometry.World.PlanetPackedTerrainBounds.md)

`flags` [ushort](https://learn.microsoft.com/dotnet/api/system.uint16)

`vertex` [PlanetPackedTerrainVertex](VirtualGeometry.World.PlanetPackedTerrainVertex.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetPackedTerrainCodec_TryUnpack_VirtualGeometry_World_PlanetPackedTerrainVertex__VirtualGeometry_World_PlanetPackedTerrainBounds__UnityEngine_Vector3__UnityEngine_Vector3__"></a> TryUnpack\(in PlanetPackedTerrainVertex, in PlanetPackedTerrainBounds, out Vector3, out Vector3\)

```csharp
public static bool TryUnpack(in PlanetPackedTerrainVertex vertex, in PlanetPackedTerrainBounds bounds, out Vector3 position, out Vector3 normal)
```

#### 引数（Parameters）

`vertex` [PlanetPackedTerrainVertex](VirtualGeometry.World.PlanetPackedTerrainVertex.md)

`bounds` [PlanetPackedTerrainBounds](VirtualGeometry.World.PlanetPackedTerrainBounds.md)

`position` Vector3

`normal` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
