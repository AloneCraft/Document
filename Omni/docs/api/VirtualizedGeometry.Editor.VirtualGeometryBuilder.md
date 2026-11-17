# <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder"></a> Class VirtualGeometryBuilder

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

入力を検査し、共有頂点を維持したクラスタと原子的な境界保持LOD階層へ変換する。

```csharp
public static class VirtualGeometryBuilder
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[VirtualGeometryBuilder](VirtualizedGeometry.Editor.VirtualGeometryBuilder.md)

## フィールド（Fields）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_LevelStatsSink"></a> LevelStatsSink

計測用。設定すると、段ごとの統計(group の数、入出力の三角形数、固定した頂点の割合)を 1 行ずつ渡す(変換は複数 thread なので、呼び出しは 1 段に 1 回、変換の thread から)。

```csharp
public static Action<string> LevelStatsSink
```

#### 値（Field Value）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_MinimumErrorGrowth"></a> MinimumErrorGrowth

```csharp
public const float MinimumErrorGrowth = 1.25
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_MinimumLevelReductionPercent"></a> MinimumLevelReductionPercent

```csharp
public static int MinimumLevelReductionPercent
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_Build_UnityEngine_Mesh_VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_"></a> Build\(Mesh, VirtualGeometryBuildSettings\)

```csharp
public static VirtualGeometryBuildOutput Build(Mesh mesh, VirtualGeometryBuildSettings settings)
```

#### 引数（Parameters）

`mesh` Mesh

`settings` [VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)

#### 戻り値（Returns）

 [VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_Build_VirtualizedGeometry_Editor_VirtualGeometryMeshInput_VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_"></a> Build\(VirtualGeometryMeshInput, VirtualGeometryBuildSettings\)

```csharp
public static VirtualGeometryBuildOutput Build(VirtualGeometryMeshInput input, VirtualGeometryBuildSettings settings)
```

#### 引数（Parameters）

`input` [VirtualGeometryMeshInput](VirtualizedGeometry.Editor.VirtualGeometryMeshInput.md)

`settings` [VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)

#### 戻り値（Returns）

 [VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)

### <a id="VirtualizedGeometry_Editor_VirtualGeometryBuilder_Build_VirtualizedGeometry_Editor_VirtualGeometryMeshInput_VirtualizedGeometry_Editor_VirtualGeometryBuildSettings_System_Threading_CancellationToken_System_Action_System_Single__"></a> Build\(VirtualGeometryMeshInput, VirtualGeometryBuildSettings, CancellationToken, Action<float\>\)

```csharp
public static VirtualGeometryBuildOutput Build(VirtualGeometryMeshInput input, VirtualGeometryBuildSettings settings, CancellationToken cancellation, Action<float> progress = null)
```

#### 引数（Parameters）

`input` [VirtualGeometryMeshInput](VirtualizedGeometry.Editor.VirtualGeometryMeshInput.md)

`settings` [VirtualGeometryBuildSettings](VirtualizedGeometry.Editor.VirtualGeometryBuildSettings.md)

`cancellation` [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)

`progress` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[float](https://learn.microsoft.com/dotnet/api/system.single)\>

#### 戻り値（Returns）

 [VirtualGeometryBuildOutput](VirtualizedGeometry.Editor.VirtualGeometryBuildOutput.md)
