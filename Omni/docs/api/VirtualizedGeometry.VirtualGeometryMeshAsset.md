# <a id="VirtualizedGeometry_VirtualGeometryMeshAsset"></a> Class VirtualGeometryMeshAsset

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

変換済みpageの小さな索引。モデルのInspectorで「Virtual Geometry」を有効にすると、インポート時にモデルのサブアセットとして作られる。
高密度の頂点配列はpage archive(VirtualGeometryPagePaths)に置く。

```csharp
public sealed class VirtualGeometryMeshAsset : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[VirtualGeometryMeshAsset](VirtualizedGeometry.VirtualGeometryMeshAsset.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_IndependentCutBuilderVersion"></a> IndependentCutBuilderVersion

group ごとの独立な細分化の判定が整合する変換器の版(親の group の誤差を子の 1.25 倍以上にする変換)。

```csharp
public const int IndependentCutBuilderVersion = 12
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_Bounds"></a> Bounds

```csharp
public Bounds Bounds { get; }
```

#### 値（Property Value）

 Bounds

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_BuilderVersion"></a> BuilderVersion

```csharp
public int BuilderVersion { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ClusterCount"></a> ClusterCount

```csharp
public int ClusterCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ContentHash"></a> ContentHash

```csharp
public string ContentHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_FormatVersion"></a> FormatVersion

```csharp
public int FormatVersion { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_GeometryBytes"></a> GeometryBytes

```csharp
public long GeometryBytes { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_InputTriangleCount"></a> InputTriangleCount

```csharp
public int InputTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_LeafTriangleCount"></a> LeafTriangleCount

```csharp
public int LeafTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_LevelCount"></a> LevelCount

LODの段数。1段目が最も細かい元の形状。

```csharp
public int LevelCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_MaterialCount"></a> MaterialCount

```csharp
public int MaterialCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_MetadataBytes"></a> MetadataBytes

```csharp
public int MetadataBytes { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_NodeCount"></a> NodeCount

```csharp
public int NodeCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_PageRelativePath"></a> PageRelativePath

```csharp
public string PageRelativePath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ProxyGeometricError"></a> ProxyGeometricError

```csharp
public float ProxyGeometricError { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ProxyLitMaterial"></a> ProxyLitMaterial

```csharp
public Material ProxyLitMaterial { get; }
```

#### 値（Property Value）

 Material

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ProxyMesh"></a> ProxyMesh

```csharp
public Mesh ProxyMesh { get; }
```

#### 値（Property Value）

 Mesh

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ProxyTriangleCount"></a> ProxyTriangleCount

```csharp
public int ProxyTriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_ProxyUnlitMaterial"></a> ProxyUnlitMaterial

```csharp
public Material ProxyUnlitMaterial { get; }
```

#### 値（Property Value）

 Material

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_SettingsHash"></a> SettingsHash

```csharp
public string SettingsHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_SlotGeometryBytes"></a> SlotGeometryBytes

```csharp
public int SlotGeometryBytes { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_SourceGuid"></a> SourceGuid

```csharp
public string SourceGuid { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_SourceHash"></a> SourceHash

```csharp
public string SourceHash { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_SourceLocalId"></a> SourceLocalId

```csharp
public long SourceLocalId { get; }
```

#### 値（Property Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_StreamingPageCount"></a> StreamingPageCount

```csharp
public int StreamingPageCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_VirtualGeometryMeshAsset_TriangleCount"></a> TriangleCount

```csharp
public int TriangleCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
