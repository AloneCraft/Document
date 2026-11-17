# <a id="VirtualGeometry_World_PlanetCellHeightStatus"></a> Enum PlanetCellHeightStatus

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

```csharp
public enum PlanetCellHeightStatus
```

## フィールド（Fields）

`NotProvided = 0` 

この Cell の高さは持たない(階層が細かすぎる、焼いていない、など)。呼び手は、高さの供給元(<xref href="VirtualGeometry.World.IPlanetHeightProvider" data-throw-if-not-resolved="false"></xref>)で作る。



`Pending = 1` 

まだ届いていない(取得を要求済み)。呼び手はその Cell を作らず、次の frame にもう一度問い合わせる(選択は親を描き続ける)。



`Ready = 2` 

格子の高さを書いた。



`Unavailable = 3` 

届かない(取得に失敗した、取得手段が無い)。偽の高さで作らず、その Cell は作らない(選択は親を描き続ける)。
