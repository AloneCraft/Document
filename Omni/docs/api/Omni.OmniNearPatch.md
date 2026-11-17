# <a id="Omni_OmniNearPatch"></a> Class OmniNearPatch

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

とても長い三角形(世界の辺が <xref href="Omni.OmniNearPatch.LongEdge" data-throw-if-not-resolved="false"></xref> を超える)を持つ物に付けます。描くたびに、視点を中心とした箱
(一辺 2 × <xref href="Omni.OmniNearPatch.Reach" data-throw-if-not-resolved="false"></xref>)に入る部分を CPU が double で切り出し、視点を原点にした小さな Mesh として描きます。
float の頂点ではラスタの被覆が本当の三角形から外れ、視点の近くで欠ける(D06 の段 3)のを補います。
元の物はそのまま描きます(同じ面なので重なっても同じ見え方)。
設計: Docs/refactoring-designs/20261114-0400-cpu-near-patch-long-triangles.md

<p>
三角形は Editor で写して保存します(<xref href="Omni.OmniNearPatch.Bake" data-throw-if-not-resolved="false"></xref>)。Player で Mesh の Read/Write が無くても動きます。
LogicalTransform の Inspector で大きな倍率を入れると、自動で付きます。
</p>

```csharp
[DisallowMultipleComponent]
[ExecuteAlways]
[AddComponentMenu("Omni/Near Patch (Long Triangles)")]
public sealed class OmniNearPatch : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[OmniNearPatch](Omni.OmniNearPatch.md)

## フィールド（Fields）

### <a id="Omni_OmniNearPatch_MaxTriangles"></a> MaxTriangles

保存できる三角形の数の上限(多すぎる Mesh は対象にしない)。

```csharp
public const int MaxTriangles = 65536
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## プロパティ（Properties）

### <a id="Omni_OmniNearPatch_IsBaked"></a> IsBaked

保存した三角形が、今の MeshFilter の Mesh のものか。

```csharp
public bool IsBaked { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniNearPatch_LongEdge"></a> LongEdge

```csharp
public float LongEdge { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_OmniNearPatch_PatchRenderers"></a> PatchRenderers

今ある Patch の Renderer(隠れた物なので、選択の候補を集める時に足す)。

```csharp
public static IReadOnlyList<Renderer> PatchRenderers { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<Renderer\>

### <a id="Omni_OmniNearPatch_Reach"></a> Reach

```csharp
public float Reach { get; set; }
```

#### 値（Property Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

## メソッド（Methods）

### <a id="Omni_OmniNearPatch_Bake"></a> Bake\(\)

MeshFilter の Mesh の三角形を写して保存します。Editor では Read/Write の無い Mesh も読めます。
Player で読めない Mesh、三角形が多すぎる Mesh は写さず false を返します。

```csharp
public bool Bake()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniNearPatch_IsPatchRenderer_UnityEngine_Renderer_"></a> IsPatchRenderer\(Renderer\)

この Renderer が、視点の近くを作り直した Patch(Omni が作る隠れた物)か。

```csharp
public static bool IsPatchRenderer(Renderer renderer)
```

#### 引数（Parameters）

`renderer` Renderer

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_OmniNearPatch_TryGetPatchOwner_UnityEngine_Renderer_UnityEngine_GameObject__"></a> TryGetPatchOwner\(Renderer, out GameObject\)

Patch の Renderer なら、元の物を返します(選択で Patch ではなく元の物を選ぶため)。

```csharp
public static bool TryGetPatchOwner(Renderer renderer, out GameObject owner)
```

#### 引数（Parameters）

`renderer` Renderer

`owner` GameObject

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
