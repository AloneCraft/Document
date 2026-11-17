# <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings"></a> Class VirtualGeometryBuildSettings

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

クラスタ化、共通位置量子化、境界保持階層を制御する変換設定。

```csharp
[Serializable]
public sealed class VirtualGeometryBuildSettings
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_GenerateStreamingPages"></a> GenerateStreamingPages

```csharp
public bool GenerateStreamingPages
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_Connection"></a> Connection

任意指定。共通local格子と全生成LODで維持する外部archive接続鎖。

```csharp
public VirtualGeometryConnection Connection { get; set; }
```

#### 値（Property Value）

 VirtualGeometryConnection

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_GenerateHierarchy"></a> GenerateHierarchy

```csharp
public bool GenerateHierarchy { get; set; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_HierarchyFanout"></a> HierarchyFanout

```csharp
public int HierarchyFanout { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_MaxTrianglesPerCluster"></a> MaxTrianglesPerCluster

```csharp
public int MaxTrianglesPerCluster { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_PositionQuantizationBits"></a> PositionQuantizationBits

```csharp
public int PositionQuantizationBits { get; set; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_SimplificationRatio"></a> SimplificationRatio

```csharp
public float SimplificationRatio { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_Clone"></a> Clone\(\)

```csharp
public VirtualGeometryBuildSettings Clone()
```

#### 戻り値（Returns）

 [VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)
