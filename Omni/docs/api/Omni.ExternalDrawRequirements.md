# <a id="Omni_ExternalDrawRequirements"></a> Enum ExternalDrawRequirements

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

Renderer収集外の外部描画経路が、Omniのcamera準備へ参加するときに宣言する要件です。

```csharp
[Flags]
public enum ExternalDrawRequirements : byte
```

## フィールド（Fields）

`CameraPacket = 1` 

Camera別packet（<code>_OmniRadialCamera_*</code>）を有効にする。



`None = 0` 

このCamera境界では何も描かない。



`SceneViewContent = 2` 

Scene Viewへ実ジオメトリを提出する。Camera別packetも有効にする。
