# <a id="VirtualizedGeometry_Editor_VirtualGeometryRendererSetup"></a> Class VirtualGeometryRendererSetup

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

URP の Renderer に、Virtual Geometry の専用描画(<xref href="VirtualizedGeometry.VirtualGeometryRenderFeature" data-throw-if-not-resolved="false"></xref>)を追加する。

```csharp
public static class VirtualGeometryRendererSetup
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryRendererSetup](VirtualizedGeometry.Editor.VirtualGeometryRendererSetup.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryRendererSetup_EnsureFeature_UnityEngine_Rendering_Universal_UniversalRendererData_"></a> EnsureFeature\(UniversalRendererData\)

Renderer に feature が無ければ追加し、depth copy の shader を設定する。

```csharp
public static VirtualGeometryRenderFeature EnsureFeature(UniversalRendererData data)
```

#### 引数（Parameters）

`data` UniversalRendererData

#### 戻り値（Returns）

 VirtualGeometryRenderFeature
