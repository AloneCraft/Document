# <a id="Omni_RadialPhysicalBounds"></a> Class RadialPhysicalBounds

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Rendererの物理（Radialで圧縮する前）のworld Boundsを返します。
Radial有効中の <xref href="UnityEngine.Renderer.bounds" data-throw-if-not-resolved="false"></xref> は、描画するCameraごとに <xref href="Omni.RadialRendererBoundsRegistry" data-throw-if-not-resolved="false"></xref> が
カリング用の保守Boundsへ書き換えるため、物理の位置関係（交差、包含、可視判定、画面上の大きさ）には使えません。
直前に描いたCamera次第で物理から離れた値になります。

```csharp
public static class RadialPhysicalBounds
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialPhysicalBounds](Omni.RadialPhysicalBounds.md)

## メソッド（Methods）

### <a id="Omni_RadialPhysicalBounds_Transform_UnityEngine_Matrix4x4_UnityEngine_Bounds_"></a> Transform\(Matrix4x4, Bounds\)

元Meshのboundsを、Transformのlocal-to-worldで変換した物理のBoundsです。

```csharp
public static Bounds Transform(Matrix4x4 localToWorld, Bounds local)
```

#### 引数（Parameters）

`localToWorld` Matrix4x4

`local` Bounds

#### 戻り値（Returns）

 Bounds

### <a id="Omni_RadialPhysicalBounds_TryGet_UnityEngine_Renderer_UnityEngine_Bounds__"></a> TryGet\(Renderer, out Bounds\)

MeshFilterまたはSkinnedMeshRendererを持つRendererは、元Meshのboundsから物理のBoundsを作ります。
それ以外（Particleなど）は元のMeshが無いので、<xref href="UnityEngine.Renderer.bounds" data-throw-if-not-resolved="false"></xref> をそのまま返し、false を返します
（この値は物理とは限りません）。

```csharp
public static bool TryGet(Renderer renderer, out Bounds bounds)
```

#### 引数（Parameters）

`renderer` Renderer

`bounds` Bounds

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
