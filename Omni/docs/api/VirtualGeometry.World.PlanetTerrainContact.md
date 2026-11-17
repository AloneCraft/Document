# <a id="VirtualGeometry_World_PlanetTerrainContact"></a> Class PlanetTerrainContact

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

物体の三角形メッシュを方向 d へまっすぐ動かしたとき、地形の三角形メッシュに初めて触れる距離を厳密に求める(どちらも描く三角形そのもの)。
区分的に平らな面どうしの最初の接触は、(1) 物体の頂点と地形の面、(2) 地形の頂点と物体の面、(3) 物体の辺と地形の辺 のどれかで起きるので、
それぞれの距離の最小値が答えになる(凹んだ形、斜面、細かい起伏でも成り立つ。球を真上から置くときの斜面の食い込み r(√(1+s²)−1) も無い)。
速くするため、d に垂直な面へ写した 2 次元の格子で候補を絞る。また、物体の最も低い点から、地形の高さの幅より上にある部分は触れようがないので除く。
入力は倍精度で、呼び出し側が同じ基準点からの相対位置にそろえる(地形の頂点は Cell の原点との Logical の差 + 描く float の頂点)。

```csharp
public static class PlanetTerrainContact
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetTerrainContact](VirtualGeometry.World.PlanetTerrainContact.md)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetTerrainContact_LastTimings"></a> LastTimings

直近の <xref href="VirtualGeometry.World.PlanetTerrainContact.TrySolve(VirtualGeometry.World.PlanetTriangleSoup%2cVirtualGeometry.World.PlanetTriangleSoup%2cVirtualGeometry.World.PlanetDouble3%2cVirtualGeometry.World.PlanetContactResult%40)" data-throw-if-not-resolved="false"></xref> の段階ごとの時間（ミリ秒、診断用）: 格子・種・頂点・地形の頂点・辺。

```csharp
public static string LastTimings { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetTerrainContact_TrySolve_VirtualGeometry_World_PlanetTriangleSoup_VirtualGeometry_World_PlanetTriangleSoup_VirtualGeometry_World_PlanetDouble3_VirtualGeometry_World_PlanetContactResult__"></a> TrySolve\(PlanetTriangleSoup, PlanetTriangleSoup, PlanetDouble3, out PlanetContactResult\)

```csharp
public static bool TrySolve(PlanetTriangleSoup body, PlanetTriangleSoup terrain, PlanetDouble3 direction, out PlanetContactResult result)
```

#### 引数（Parameters）

`body` [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

`terrain` [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

`direction` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`result` [PlanetContactResult](VirtualGeometry.World.PlanetContactResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetTerrainContact_VertexGap_VirtualGeometry_World_PlanetTriangleSoup_VirtualGeometry_World_PlanetTriangleSoup_VirtualGeometry_World_PlanetDouble3_System_Double_"></a> VertexGap\(PlanetTriangleSoup, PlanetTriangleSoup, PlanetDouble3, double\)

物体を travel だけ動かした後の、物体と地形の d 方向の最小の隙間(正なら離れている、負ならめり込み)。<xref href="VirtualGeometry.World.PlanetTerrainContact.TrySolve(VirtualGeometry.World.PlanetTriangleSoup%2cVirtualGeometry.World.PlanetTriangleSoup%2cVirtualGeometry.World.PlanetDouble3%2cVirtualGeometry.World.PlanetContactResult%40)" data-throw-if-not-resolved="false"></xref> と独立に、
物体の頂点と地形の頂点の半直線だけで測る(検証用。辺と辺の接触は数えないので、TrySolve の答えでは 0 以上になる)。

```csharp
public static double VertexGap(PlanetTriangleSoup body, PlanetTriangleSoup terrain, PlanetDouble3 direction, double travel)
```

#### 引数（Parameters）

`body` [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

`terrain` [PlanetTriangleSoup](VirtualGeometry.World.PlanetTriangleSoup.md)

`direction` [PlanetDouble3](VirtualGeometry.World.PlanetDouble3.md)

`travel` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
