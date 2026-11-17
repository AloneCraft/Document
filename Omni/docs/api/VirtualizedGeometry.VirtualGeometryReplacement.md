# <a id="VirtualizedGeometry_VirtualGeometryReplacement"></a> Class VirtualGeometryReplacement

Namespace: [VirtualizedGeometry](VirtualizedGeometry.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

静的meshのCPU参照と手続きmeshが共有する誤差/ヒステリシス契約。

```csharp
public static class VirtualGeometryReplacement
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryReplacement](VirtualizedGeometry.VirtualGeometryReplacement.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_VirtualGeometryReplacement_WantsRefinement_System_Single_System_Single_System_Single_System_Boolean_"></a> WantsRefinement\(float, float, float, bool\)

```csharp
public static bool WantsRefinement(float error, float target, float hysteresis, bool wasRefined)
```

#### 引数（Parameters）

`error` [float](https://learn.microsoft.com/dotnet/api/system.single)

`target` [float](https://learn.microsoft.com/dotnet/api/system.single)

`hysteresis` [float](https://learn.microsoft.com/dotnet/api/system.single)

`wasRefined` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
