# <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput"></a> Class VirtualGeometryBuildOutput

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

```csharp
public sealed class VirtualGeometryBuildOutput
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput__ctor_VirtualizedGeometry_VirtualGeometryPage_VirtualizedGeometry_Editor_VirtualGeometryBuildDiagnostic___System_Int32_System_Int32_"></a> VirtualGeometryBuildOutput\(VirtualGeometryPage, VirtualGeometryBuildDiagnostic\[\], int, int\)

```csharp
public VirtualGeometryBuildOutput(VirtualGeometryPage page, VirtualGeometryBuildDiagnostic[] diagnostics, int inputTriangleCount, int leafTriangleCount)
```

#### 引数（Parameters）

`page` VirtualGeometryPage

`diagnostics` [VirtualGeometryBuildDiagnostic](VirtualizedGeometry.Editor.VirtualGeometryBuildDiagnostic.md)\[\]

`inputTriangleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`leafTriangleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Bounds"></a> Bounds

```csharp
public Bounds Bounds { get; }
```

#### 値（Property Value）

 Bounds

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Clusters"></a> Clusters

```csharp
public VirtualGeometryCluster[] Clusters { get; }
```

#### 値（Property Value）

 VirtualGeometryCluster\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_ContentHash"></a> ContentHash

```csharp
public string ContentHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Diagnostics"></a> Diagnostics

```csharp
public VirtualGeometryBuildDiagnostic[] Diagnostics { get; }
```

#### 値（Property Value）

 [VirtualGeometryBuildDiagnostic](VirtualizedGeometry.Editor.VirtualGeometryBuildDiagnostic.md)\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Indices"></a> Indices

```csharp
public uint[] Indices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_InputTriangleCount"></a> InputTriangleCount

```csharp
public int InputTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_LeafTriangleCount"></a> LeafTriangleCount

```csharp
public int LeafTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Nodes"></a> Nodes

```csharp
public VirtualGeometryHierarchyNode[] Nodes { get; }
```

#### 値（Property Value）

 VirtualGeometryHierarchyNode\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Page"></a> Page

変換結果のgeometryと階層。streaming archiveはここから直接書き出す。

```csharp
public VirtualGeometryPage Page { get; }
```

#### 値（Property Value）

 VirtualGeometryPage

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_PageBytes"></a> PageBytes

単一page形式のbyte列。大きなmeshでは書き出しが重いため、参照されたときに初めて作る。

```csharp
public byte[] PageBytes { get; }
```

#### 値（Property Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_RootNodeIndices"></a> RootNodeIndices

```csharp
public uint[] RootNodeIndices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_Vertices"></a> Vertices

```csharp
public VirtualGeometryPackedVertex[] Vertices { get; }
```

#### 値（Property Value）

 VirtualGeometryPackedVertex\[\]
