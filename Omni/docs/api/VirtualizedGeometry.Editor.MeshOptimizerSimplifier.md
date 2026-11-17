# <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifier"></a> Class MeshOptimizerSimplifier

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

meshoptimizer v1.1を決定的なEditor変換だけに使用する薄い境界。

```csharp
public static class MeshOptimizerSimplifier
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[MeshOptimizerSimplifier](VirtualizedGeometry.Editor.MeshOptimizerSimplifier.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifier_ExpectedVersion"></a> ExpectedVersion

```csharp
public const int ExpectedVersion = 1010
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifier_VertexLock"></a> VertexLock

```csharp
public const byte VertexLock = 1
```

#### 値（Field Value）

 [byte](https://learn.microsoft.com/dotnet/api/system.byte)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifier_Version"></a> Version

```csharp
public static int Version { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifier_Simplify_VirtualizedGeometry_VirtualGeometryPackedVertex___System_UInt32___System_Byte___System_Int32_"></a> Simplify\(VirtualGeometryPackedVertex\[\], uint\[\], byte\[\], int\)

```csharp
public static MeshOptimizerSimplifyResult Simplify(VirtualGeometryPackedVertex[] vertices, uint[] indices, byte[] vertexLocks, int targetIndexCount)
```

#### 引数（Parameters）

`vertices` VirtualGeometryPackedVertex\[\]

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`vertexLocks` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

`targetIndexCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [MeshOptimizerSimplifyResult](VirtualizedGeometry.Editor.MeshOptimizerSimplifyResult.md)
