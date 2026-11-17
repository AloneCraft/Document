# <a id="Omni_Converter_OmniSceneRadialUsage"></a> Enum OmniSceneRadialUsage

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

Scene 1つが対数（Radial）レンダリングを使うかの判定です。

```csharp
public enum OmniSceneRadialUsage
```

## フィールド（Fields）

`Radial = 1` 

対数を使う。



`Standard = 0` 

有効な RadialCamera も、対数用に生成した資産の参照も無い。



`Undetermined = 2` 

判定できない（Scene が読めない等）。Fail Closed で対数を使うものとして扱う。
