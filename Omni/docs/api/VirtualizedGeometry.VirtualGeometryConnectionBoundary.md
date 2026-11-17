# <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary"></a> Class VirtualGeometryConnectionBoundary

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

独立archiveが共有する有向の開いた接続鎖。頂点番号はbuild入力、位置は共通local frameの正本。

```csharp
public sealed class VirtualGeometryConnectionBoundary
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryConnectionBoundary](VirtualizedGeometry.VirtualGeometryConnectionBoundary.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary__ctor_System_String_System_Int32___UnityEngine_Vector3___"></a> VirtualGeometryConnectionBoundary\(string, int\[\], Vector3\[\]\)

```csharp
public VirtualGeometryConnectionBoundary(string id, int[] vertices, Vector3[] positions)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

`vertices` [int](https://learn.microsoft.com/dotnet/api/system.int32)\[\]

`positions` Vector3\[\]

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary_Count"></a> Count

```csharp
public int Count { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary_Id"></a> Id

```csharp
public string Id { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary_Position_System_Int32_"></a> Position\(int\)

```csharp
public Vector3 Position(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 Vector3

### <a id="VirtualizedGeometry_VirtualGeometryConnectionBoundary_Vertex_System_Int32_"></a> Vertex\(int\)

```csharp
public int Vertex(int index)
```

#### 引数（Parameters）

`index` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
