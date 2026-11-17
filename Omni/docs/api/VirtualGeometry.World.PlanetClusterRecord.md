# <a id="VirtualGeometry_World_PlanetClusterRecord"></a> Struct PlanetClusterRecord

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

CameraごとのCell配置。64 byte。C#とHLSLは4つのfloat4で配置を共有する。

```csharp
public struct PlanetClusterRecord
```

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetClusterRecord_Morph"></a> Morph

四隅のmorph割合。

```csharp
public Vector4 Morph
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetClusterRecord_MorphInfo"></a> MorphInfo

親slot、N、slot頂点数、quadrant+1（0ならmorph無効）。既存PlanetMorphの符号化。

```csharp
public Vector4 MorphInfo
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetClusterRecord_MorphOffsetFace"></a> MorphOffsetFace

xyz: 親原点−Cell原点、w: cube face（接線の基底を選ぶ）。

```csharp
public Vector4 MorphOffsetFace
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetClusterRecord_OriginPadding"></a> OriginPadding

xyz: Cell原点−アンカー原点（Logicalで差を求めてからfloat化）、w: morphのカリングpadding。

```csharp
public Vector4 OriginPadding
```

#### 値（Field Value）

 Vector4

### <a id="VirtualGeometry_World_PlanetClusterRecord_Stride"></a> Stride

```csharp
public const int Stride = 64
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
