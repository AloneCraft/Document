# <a id="VirtualizedGeometry_Editor_VirtualGeometryProxyBuilder"></a> Class VirtualGeometryProxyBuilder

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

fallback/影/物理/選択用の低密度Meshを階層から生成し、元Mesh参照を残さない。
rootから単一子の段を降りた、group束ねで1 nodeへまとまった段を使う。最粗root(1 cluster以下)では影やcolliderが粗すぎるため。

```csharp
public static class VirtualGeometryProxyBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryProxyBuilder](VirtualizedGeometry.Editor.VirtualGeometryProxyBuilder.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryProxyBuilder_Create_VirtualizedGeometry_Editor_VirtualGeometryBuildOutput_System_Int32__System_Single__"></a> Create\(VirtualGeometryBuildOutput, out int, out float\)

```csharp
public static Mesh Create(VirtualGeometryBuildOutput source, out int triangleCount, out float error)
```

#### 引数（Parameters）

`source` [VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)

`triangleCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`error` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 Mesh
