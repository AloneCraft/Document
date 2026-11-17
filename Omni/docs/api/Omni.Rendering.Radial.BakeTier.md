# <a id="Omni_Rendering_Radial_BakeTier"></a> Enum BakeTier

Namespace: [Omni.Rendering.Radial](Omni.Rendering.Radial.md)  
Assembly: Radial.Runtime.dll  

距離帯の分類です。

```csharp
public enum BakeTier : byte
```

## フィールド（Fields）

`FarField = 2` 

遠景キャッシュ（RadialFarFieldCache）の対象になりうる帯。



`MidField = 1` 

NearFieldとFarFieldの中間帯。



`NearField = 0` 

常にlinearRadius内（ThresholdLinearLogでは恒等写像）。
