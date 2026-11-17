# <a id="Omni_Editor_Manager_ShaderStatus"></a> Enum ShaderStatus

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

```csharp
public enum ShaderStatus
```

## フィールド（Fields）

`Generated = 1` 

`InvalidReference = 4` 

`NativeRadial = 5` 

Shader自身が最初からRadial変換を実装している（例: <code>StencilOnly.shader</code>）。
切替は対数化済みとして扱い、生成も変更もしないため、生成先の有無を問いません。
判定は切替処理と同じ <xref href="Omni.RadialMaterialContract.DeclaresRadialTransform(UnityEngine.Shader)" data-throw-if-not-resolved="false"></xref> です。



`NotGenerated = 0` 

`Skipped = 2` 

`Stale = 3` 

生成物はあるが、現在のパッチャの出力と食い違っている（作り直しが必要）。

<p>
判定は <xref href="Omni.Editor.Manager.OmniShaderGenerator.IsGeneratedShaderStale(System.String%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> が行います。
この状態を持たなかったために、パッチャを改良しても古い生成物が使われ続けている
ことを UI から知る術がありませんでした（2026-08 の対数表示オブジェクトが
クリック選択できない不具合）。
</p>
