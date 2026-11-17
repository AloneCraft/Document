# <a id="Omni_Logical_OmniHideLayer"></a> Enum OmniHideLayer

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

Rendererを非表示にした層の種別です。

```csharp
public enum OmniHideLayer
```

## フィールド（Fields）

`EditorBoundary = 1` 

Unity標準編集空間の安全域を越えたEditor側の非表示です。



`FiniteProxy = 3` 

有限描画プロキシへ置き換えたことによる元Rendererの抑制です。



`MaterialCompatibility = 2` 

RadialTransform未対応マテリアルのカメラ単位非表示です。



`ShellCulling = 0` 

ベイク済み外接球によるnear/farシェルカリングです。



`Unsupported = 4` 

有限描画プロキシ未対応として隔離した非表示です。
