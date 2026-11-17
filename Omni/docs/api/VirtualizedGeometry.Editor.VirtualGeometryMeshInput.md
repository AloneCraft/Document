# <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput"></a> Class VirtualGeometryMeshInput

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

Meshから抽出した、Unityオブジェクト寿命に依存しない変換入力。

```csharp
public sealed class VirtualGeometryMeshInput
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryMeshInput](VirtualizedGeometry.Editor.VirtualGeometryMeshInput.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput__ctor_UnityEngine_Vector3___UnityEngine_Vector3___UnityEngine_Vector2___System_Int32_____"></a> VirtualGeometryMeshInput\(Vector3\[\], Vector3\[\], Vector2\[\], int\[\]\[\]\)

```csharp
public VirtualGeometryMeshInput(Vector3[] positions, Vector3[] normals, Vector2[] uv, int[][] submeshIndices)
```

#### 引数（Parameters）

`positions` Vector3\[\]

`normals` Vector3\[\]

`uv` Vector2\[\]

`submeshIndices` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]\[\]

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput_Normals"></a> Normals

```csharp
public Vector3[] Normals { get; }
```

#### 値（Property Value）

 Vector3\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput_Positions"></a> Positions

```csharp
public Vector3[] Positions { get; }
```

#### 値（Property Value）

 Vector3\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput_SubmeshIndices"></a> SubmeshIndices

```csharp
public int[][] SubmeshIndices { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput_UV"></a> UV

```csharp
public Vector2[] UV { get; }
```

#### 値（Property Value）

 Vector2\[\]

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryMeshInput_FromMesh_UnityEngine_Mesh_"></a> FromMesh\(Mesh\)

```csharp
public static VirtualGeometryMeshInput FromMesh(Mesh mesh)
```

#### 引数（Parameters）

`mesh` Mesh

#### 戻り値（Returns）

 [VirtualGeometryMeshInput](VirtualizedGeometry.Editor.VirtualGeometryMeshInput.md)
