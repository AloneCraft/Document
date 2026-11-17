# <a id="VirtualGeometry_World_PlanetTerrainStorageRecord"></a> Struct PlanetTerrainStorageRecord

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

logical slotから12 B/元の32 Bの物理word領域へ写す。範囲はCell局所、UVは格子から復元する。

```csharp
public struct PlanetTerrainStorageRecord
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetTerrainStorageRecord_Control"></a> Control

```csharp
public uint4 Control
```

#### 値（Field Value）

 uint4

### <a id="VirtualGeometry_World_PlanetTerrainStorageRecord_Extent"></a> Extent

```csharp
public Vector4 Extent
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetTerrainStorageRecord_FaceRange"></a> FaceRange

```csharp
public Vector4 FaceRange
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetTerrainStorageRecord_Minimum"></a> Minimum

```csharp
public Vector4 Minimum
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetTerrainStorageRecord_Stride"></a> Stride

```csharp
public const int Stride = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
