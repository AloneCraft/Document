# <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifyResult"></a> Struct MeshOptimizerSimplifyResult

Namespace: [VirtualizedGeometry.Editor](VirtualizedGeometry.Editor.md)  
Assembly: Omni.VirtualGeometry.Editor.dll  

```csharp
public readonly struct MeshOptimizerSimplifyResult
```

## コンストラクター（Constructors）

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifyResult__ctor_System_UInt32___System_Single_System_Int32_"></a> MeshOptimizerSimplifyResult\(uint\[\], float, int\)

```csharp
public MeshOptimizerSimplifyResult(uint[] indices, float error, int scratchVertexCount)
```

#### 引数（Parameters）

`indices` [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

`error` [float](https://learn.microsoft.com/dotnet/api/system.single)

`scratchVertexCount` [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifyResult_Error"></a> Error

```csharp
public float Error { get; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifyResult_Indices"></a> Indices

```csharp
public uint[] Indices { get; }
```

#### 値（Property Value）

 [uint](https://learn.microsoft.com/dotnet/api/system.uint32)\[\]

### <a id="VirtualizedGeometry_Editor_MeshOptimizerSimplifyResult_ScratchVertexCount"></a> ScratchVertexCount

```csharp
public int ScratchVertexCount { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
