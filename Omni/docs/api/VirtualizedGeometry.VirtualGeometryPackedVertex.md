# <a id="VirtualizedGeometry_VirtualGeometryPackedVertex"></a> Struct VirtualGeometryPackedVertex

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

C#とHLSLで共有する頂点(32 byte)。実行時生成clusterの頂点buffer(<xref href="VirtualizedGeometry.VirtualGeometryClusterSource" data-throw-if-not-resolved="false"></xref>)がこの形で持つ。

```csharp
[Serializable]
public struct VirtualGeometryPackedVertex
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryPackedVertex__ctor_UnityEngine_Vector3_UnityEngine_Vector3_UnityEngine_Vector2_"></a> VirtualGeometryPackedVertex\(Vector3, Vector3, Vector2\)

```csharp
public VirtualGeometryPackedVertex(Vector3 position, Vector3 normal, Vector2 uv)
```

#### 引数（Parameters）

`position` Vector3

`normal` Vector3

`uv` Vector2

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryPackedVertex_Normal"></a> Normal

```csharp
public Vector3 Normal
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryPackedVertex_Position"></a> Position

```csharp
public Vector3 Position
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryPackedVertex_Stride"></a> Stride

```csharp
public const int Stride = 32
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryPackedVertex_UV"></a> UV

```csharp
public Vector2 UV
```

#### 値（Field Value）

 Vector2
