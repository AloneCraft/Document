# <a id="Omni_Diagnostics_OmniBenchmarkKind"></a> Enum OmniBenchmarkKind

Namespace: [Omni.Diagnostics](Omni.Diagnostics.md)  
Assembly: Radial.Runtime.dll  

性能計測が対象とするコンテンツ種別を表します。

```csharp
public enum OmniBenchmarkKind
```

## フィールド（Fields）

`GalaxyRegression = 1` 

Galaxyの画像・性能回帰計測です。



`SaturnLargeResident = 5` 

Saturn LargeのResident 100万粒子計測です。



`SaturnStandard = 4` 

Saturn Standard 180秒ショーの計測です。



`SaturnStreaming = 6` 

Saturnの固定時刻列Streaming計測です。



`Scale = 2` 

Scaleシーンの性能計測です。



`Terminal = 3` 

TerminalSceneの性能計測です。



`Unspecified = 0` 

シーン固有の計測種別が未指定です。
