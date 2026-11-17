# <a id="VirtualGeometry_World_IPlanetHeightOverride"></a> Interface IPlanetHeightOverride

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

天体の一部だけ高さを書き換える層(局所の実測、施設の地ならし、島など)。内容を変えたら <xref href="VirtualGeometry.World.IPlanetHeightOverride.CacheIdentity" data-throw-if-not-resolved="false"></xref> も変えること。
方向は天体のローカル座標の単位ベクトル。複数のスレッドから同時に呼ばれるので、状態を変えないこと。

```csharp
public interface IPlanetHeightOverride
```

## プロパティ（Properties）

### <a id="VirtualGeometry_World_IPlanetHeightOverride_CacheIdentity"></a> CacheIdentity

```csharp
string CacheIdentity { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="VirtualGeometry_World_IPlanetHeightOverride_MaximumAbsoluteHeightMeters"></a> MaximumAbsoluteHeightMeters

```csharp
double MaximumAbsoluteHeightMeters { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_IPlanetHeightOverride_Sample_System_Double_System_Double_System_Double_"></a> Sample\(double, double, double\)

```csharp
PlanetHeightBlend Sample(double unitX, double unitY, double unitZ)
```

#### 引数（Parameters）

`unitX` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitY` [double](https://learn.microsoft.com/dotnet/api/system.double)

`unitZ` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [PlanetHeightBlend](VirtualGeometry.World.PlanetHeightBlend.md)
