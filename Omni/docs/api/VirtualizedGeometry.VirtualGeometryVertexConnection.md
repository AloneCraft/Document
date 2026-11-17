# <a id="VirtualizedGeometry_VirtualGeometryVertexConnection"></a> Struct VirtualGeometryVertexConnection

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

局所meshの頂点を、共有Logical正本へ結ぶ供給側の明示参照。追加の接続頂点も同じ契約を使う。

```csharp
public readonly struct VirtualGeometryVertexConnection
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryVertexConnection__ctor_System_Int32_VirtualizedGeometry_VirtualGeometrySharedVertex__UnityEngine_Vector3_UnityEngine_Vector2_"></a> VirtualGeometryVertexConnection\(int, in VirtualGeometrySharedVertex, Vector3, Vector2\)

```csharp
public VirtualGeometryVertexConnection(int localIndex, in VirtualGeometrySharedVertex vertex, Vector3 normal, Vector2 uv)
```

#### 引数（Parameters）

`localIndex` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`vertex` [VirtualGeometrySharedVertex](VirtualizedGeometry.VirtualGeometrySharedVertex.md)

`normal` Vector3

`uv` Vector2

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryVertexConnection_LocalIndex"></a> LocalIndex

```csharp
public readonly int LocalIndex
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryVertexConnection_Normal"></a> Normal

```csharp
public readonly Vector3 Normal
```

#### 値（Field Value）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryVertexConnection_Uv"></a> Uv

```csharp
public readonly Vector2 Uv
```

#### 値（Field Value）

 Vector2

### <a id="VirtualizedGeometry_VirtualGeometryVertexConnection_Vertex"></a> Vertex

```csharp
public readonly VirtualGeometrySharedVertex Vertex
```

#### 値（Field Value）

 [VirtualGeometrySharedVertex](VirtualizedGeometry.VirtualGeometrySharedVertex.md)
