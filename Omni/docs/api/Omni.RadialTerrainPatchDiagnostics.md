# <a id="Omni_RadialTerrainPatchDiagnostics"></a> Struct RadialTerrainPatchDiagnostics

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

<xref href="Omni.RadialTerrainPatchRegistry" data-throw-if-not-resolved="false"></xref> の読み取り専用診断値です。
Omni Manager/ValidatorがTerrainDataを変更せずにbackendの状態を表示するために使います。

```csharp
public readonly struct RadialTerrainPatchDiagnostics
```

## フィールド（Fields）

### <a id="Omni_RadialTerrainPatchDiagnostics_CurrentLodLevel"></a> CurrentLodLevel

v1固定LODです。quadtree LOD導入まで常に0です。

```csharp
public readonly int CurrentLodLevel
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialTerrainPatchDiagnostics_DirtyPatchCount"></a> DirtyPatchCount

Heightmapまたは穴の変更を受けて再構築待ちになっているpatch数です。

```csharp
public readonly int DirtyPatchCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialTerrainPatchDiagnostics_FaultReason"></a> FaultReason

Faulted時の理由です。正常時はnullです。

```csharp
public readonly string FaultReason
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_RadialTerrainPatchDiagnostics_NativeHeightmapSuppressed"></a> NativeHeightmapSuppressed

Native Terrain surface（drawHeightmap）をbackendが停止している場合はtrueです。

```csharp
public readonly bool NativeHeightmapSuppressed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialTerrainPatchDiagnostics_PatchCount"></a> PatchCount

生成済みの33×33相当patch数です。

```csharp
public readonly int PatchCount
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_RadialTerrainPatchDiagnostics_State"></a> State

現在のbackend状態です。

```csharp
public readonly RadialTerrainBackendState State
```

#### 値（Field Value）

 [RadialTerrainBackendState](Omni.RadialTerrainBackendState.md)

### <a id="Omni_RadialTerrainPatchDiagnostics_TreesAndDetailsUntouched"></a> TreesAndDetailsUntouched

Tree/Detail設定へ触れていないことを示します。

```csharp
public readonly bool TreesAndDetailsUntouched
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
