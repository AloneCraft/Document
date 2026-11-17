# <a id="VirtualizedGeometry_VirtualGeometryNormalMapping"></a> Class VirtualGeometryNormalMapping

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

格納tangentがないv3向け、三角形の位置差とUV差からtangent/bitangentを作るCPU参照(VirtualGeometryVertexInput.hlslのVGFaceTangentと同じ式)。UV縮退時はfalse。

```csharp
public static class VirtualGeometryNormalMapping
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryNormalMapping](VirtualizedGeometry.VirtualGeometryNormalMapping.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryNormalMapping_TryBuildFrame_UnityEngine_Vector3_UnityEngine_Vector3_UnityEngine_Vector3_UnityEngine_Vector2_UnityEngine_Vector2_UnityEngine_Vector3__UnityEngine_Vector3__"></a> TryBuildFrame\(Vector3, Vector3, Vector3, Vector2, Vector2, out Vector3, out Vector3\)

```csharp
public static bool TryBuildFrame(Vector3 normal, Vector3 dx, Vector3 dy, Vector2 uvx, Vector2 uvy, out Vector3 tangent, out Vector3 bitangent)
```

#### 引数（Parameters）

`normal` Vector3

`dx` Vector3

`dy` Vector3

`uvx` Vector2

`uvy` Vector2

`tangent` Vector3

`bitangent` Vector3

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
