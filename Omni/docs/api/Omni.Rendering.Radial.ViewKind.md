# <a id="Omni_Rendering_Radial_ViewKind"></a> Enum ViewKind

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

Radial描画のビュー種別です。SaturnのBRG v1は<xref href="Omni.Rendering.Radial.ViewKind.Camera" data-throw-if-not-resolved="false"></xref>だけを描画対象にし、
それ以外はカリングを省略するfail-open経路へ渡します。

```csharp
public enum ViewKind
```

## フィールド（Fields）

`Camera = 0` 

Game Viewなど、プレイヤー向けの通常カメラです。



`Other = 4` 

上記へ分類できないカメラです。



`Preview = 2` 

Inspector等のPreviewカメラです。



`Reflection = 3` 

反射プローブなどのReflectionカメラです。



`SceneView = 1` 

Unity EditorのScene Viewです。
