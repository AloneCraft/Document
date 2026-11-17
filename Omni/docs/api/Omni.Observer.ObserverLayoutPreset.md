# <a id="Omni_Observer_ObserverLayoutPreset"></a> Enum ObserverLayoutPreset

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

観察枠の並べ方です。

```csharp
public enum ObserverLayoutPreset
```

## フィールド（Fields）

`Combined = 2` 

周回枠を大きく、固定4枠をその横に小さく縦に並べます。



`FixedGrid = 1` 

固定角度の4枠（Front／Right／Top／Iso）を2x2で大きく置きます。角度ごとの静止確認と画像回帰の用途です。



`OrbitWipe = 0` 

周回枠1つを画面の隅に小さく置きます。時間変化する異常を探す用途です。
