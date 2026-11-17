# <a id="Omni_VirtualObject_ProceduralMeshStep"></a> Delegate ProceduralMeshStep

Namespace: [Omni.VirtualObject](Omni.VirtualObject.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

メッシュを少しずつ作る関数。呼ばれるたびに <code class="paramref">buffer</code> へ最大 <code class="paramref">triangleBudget</code> 個の三角形を足し、全部できたら true を返す。
どこまで作ったかは buffer（<xref href="Omni.VirtualObject.ProceduralMeshBuffer.TriangleCount" data-throw-if-not-resolved="false"></xref> など）から読んで再開する（関数自体は状態を持たなくてよい）。
予算を超えて足すと失敗として扱う。

```csharp
public delegate bool ProceduralMeshStep(ProceduralMeshBuffer buffer, int triangleBudget)
```

#### 引数（Parameters）

`buffer` [ProceduralMeshBuffer](Omni.VirtualObject.ProceduralMeshBuffer.md)

`triangleBudget` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
