# <a id="Omni_Observer_RadialObserverFraming"></a> Class RadialObserverFraming

Namespace: [Omni.Observer](Omni.Observer.md)  
Assembly: Omni.RadialObserver.dll  

変形後の世界を俯瞰するカメラの枠取り数学です。Unity型へ依存する副作用を持ちません。

<p>
変形後の世界は有限です（<code>F(M*d)</code>は距離の対数に比例）。巨大・遠距離の対象も、
Logical差分を<xref href="Omni.RadialSettings.TryMap(Omni.Logical.Vector3%40%2cUnity.Mathematics.float3%40)" data-throw-if-not-resolved="false"></xref>で有限の描画座標へ落としてから扱うため、
絶対座標をfloatへ狭小化しません。
</p>

```csharp
public static class RadialObserverFraming
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialObserverFraming](Omni.Observer.RadialObserverFraming.md)

## メソッド（Methods）

### <a id="Omni_Observer_RadialObserverFraming_CreateFixedDistanceFrame_System_Single_System_Single_"></a> CreateFixedDistanceFrame\(float, float\)

注視点をC（原点）に置き、カメラ距離を <code>distanceInScale × S</code> に固定する枠を返します。
変形後の世界の広がりは <code>S × log2(…)</code> の桁（Sは1オクターブあたりの描画単位）なので、
距離をSに比例させれば、Sが0.01でも10でも同じ見え方になります。
境界球の半径は近遠クリップ用で、距離の0.4倍です。

```csharp
public static ObserverFrame CreateFixedDistanceFrame(float radialScale, float distanceInScale)
```

#### 引数（Parameters）

`radialScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

`distanceInScale` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [ObserverFrame](Omni.Observer.ObserverFrame.md)
