# <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildInclusion"></a> Class VirtualGeometryBuildInclusion

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

Playerへ収録するarchive集合とEditor専用native依存の禁止境界。

```csharp
public static class VirtualGeometryBuildInclusion
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryBuildInclusion](VirtualizedGeometry.Editor.VirtualGeometryBuildInclusion.md)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildInclusion_DistinctArchives_System_Collections_Generic_IEnumerable_System_String__"></a> DistinctArchives\(IEnumerable<string\>\)

```csharp
public static string[] DistinctArchives(IEnumerable<string> paths)
```

#### 引数（Parameters）

`paths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuildInclusion_IsForbiddenPlayerPath_System_String_"></a> IsForbiddenPlayerPath\(string\)

```csharp
public static bool IsForbiddenPlayerPath(string path)
```

#### 引数（Parameters）

`path` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
