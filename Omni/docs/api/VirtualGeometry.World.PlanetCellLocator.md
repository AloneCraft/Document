# <a id="VirtualGeometry_World_PlanetCellLocator"></a> Class PlanetCellLocator

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

方向から Cell を探す(double の精度。階層 50 程度まで区別できる)。

```csharp
public static class PlanetCellLocator
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetCellLocator](VirtualGeometry.World.PlanetCellLocator.md)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetCellLocator_AddDescentPath_VirtualGeometry_World_PlanetCellKey__System_Collections_Generic_HashSet_VirtualGeometry_World_PlanetCellKey__"></a> AddDescentPath\(in PlanetCellKey, HashSet<PlanetCellKey\>\)

key まで細分化して降りる道（root から key の親まで）の Cell と、その各 Cell の子 4 つ。選択は子 4 つが揃ってから細分化するので、
これらが揃っていれば、画面に入った時点で key の階層まで 1 frame で降りられる。key 自身は含む（親の子として）。

```csharp
public static void AddDescentPath(in PlanetCellKey key, HashSet<PlanetCellKey> keys)
```

#### 引数（Parameters）

`key` [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

`keys` [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>

### <a id="VirtualGeometry_World_PlanetCellLocator_KeyAt_System_Double_System_Double_System_Double_System_Int32_"></a> KeyAt\(double, double, double, int\)

単位方向(惑星のローカル座標)を含む、階層 level の Cell。面の境界ではどちらか一方。

```csharp
public static PlanetCellKey KeyAt(double x, double y, double z, int level)
```

#### 引数（Parameters）

`x` [double](https://learn.microsoft.com/dotnet/api/system.double)

`y` [double](https://learn.microsoft.com/dotnet/api/system.double)

`z` [double](https://learn.microsoft.com/dotnet/api/system.double)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)

### <a id="VirtualGeometry_World_PlanetCellLocator_KeysAround_Omni_Logical_Vector3__System_Single_System_Int32_System_Single_"></a> KeysAround\(in Vector3, float, int, float\)

点 point(惑星のローカル座標、Logical)のまわり半径 radius の円板(点の方向の接平面)に掛かる、階層 level の Cell の集まり(と、その外側 1 周)。
円板を Cell の大きさの半分の間隔で標本して Cell を集めるので、取りこぼさない。sphereRadius は惑星の半径(Cell の大きさの見積もり)。

```csharp
public static HashSet<PlanetCellKey> KeysAround(in Vector3 point, float radius, int level, float sphereRadius)
```

#### 引数（Parameters）

`point` Vector3

`radius` [float](https://learn.microsoft.com/dotnet/api/system.single)

`level` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`sphereRadius` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [HashSet](https://learn.microsoft.com/dotnet/api/system.collections.generic.hashset\-1)<[PlanetCellKey](VirtualGeometry.World.PlanetCellKey.md)\>
