# <a id="VirtualGeometry_World_PlanetLodBudgetController"></a> Class PlanetLodBudgetController

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

Layer全体の閾値倍率だけを調整する。選択cutや接地、pool容量を直接変更しない。

```csharp
public sealed class PlanetLodBudgetController
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[PlanetLodBudgetController](VirtualGeometry.World.PlanetLodBudgetController.md)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetLodBudgetController_AttackSeconds"></a> AttackSeconds

```csharp
public const double AttackSeconds = 0.25
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLodBudgetController_MaximumMultiplier"></a> MaximumMultiplier

```csharp
public const double MaximumMultiplier = 2
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLodBudgetController_RecoveryDelaySeconds"></a> RecoveryDelaySeconds

```csharp
public const double RecoveryDelaySeconds = 1
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLodBudgetController_RecoveryPerSecond"></a> RecoveryPerSecond

```csharp
public const double RecoveryPerSecond = 0.95
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="VirtualGeometry_World_PlanetLodBudgetController_RecoveryThreshold"></a> RecoveryThreshold

```csharp
public const double RecoveryThreshold = 0.8
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetLodBudgetController_Multiplier"></a> Multiplier

```csharp
public double Multiplier { get; }
```

#### 値（Property Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

## メソッド（Methods）

### <a id="VirtualGeometry_World_PlanetLodBudgetController_FromSerialized_VirtualGeometry_World_PlanetLodBudgetSignals_"></a> FromSerialized\(PlanetLodBudgetSignals\)

保存された信号の指定を、<xref href="VirtualGeometry.World.PlanetLodBudgetController.Step(System.Int64%2cVirtualGeometry.World.PlanetLodBudgetMode%2cSystem.Double%2cVirtualGeometry.World.PlanetLodBudgetSample%40%2cVirtualGeometry.World.PlanetLodBudgetSignals)" data-throw-if-not-resolved="false"></xref> へ渡せる形にする。Inspector の Flags の欄で「Everything」を選ぶと、Unity は定義した信号の外のビットも
立てた値(-1)を書くので、定義の外のビットを落として全ての信号(<xref href="VirtualGeometry.World.PlanetLodBudgetSignals.All" data-throw-if-not-resolved="false"></xref>)にする。
「Nothing」(0)は 0 のまま返す(見る信号が無い指定で、<xref href="VirtualGeometry.World.PlanetLodBudgetController.Step(System.Int64%2cVirtualGeometry.World.PlanetLodBudgetMode%2cSystem.Double%2cVirtualGeometry.World.PlanetLodBudgetSample%40%2cVirtualGeometry.World.PlanetLodBudgetSignals)" data-throw-if-not-resolved="false"></xref> は受け付けない。呼ぶ側が扱いを決める)。

```csharp
public static PlanetLodBudgetSignals FromSerialized(PlanetLodBudgetSignals value)
```

#### 引数（Parameters）

`value` [PlanetLodBudgetSignals](VirtualGeometry.World.PlanetLodBudgetSignals.md)

#### 戻り値（Returns）

 [PlanetLodBudgetSignals](VirtualGeometry.World.PlanetLodBudgetSignals.md)

### <a id="VirtualGeometry_World_PlanetLodBudgetController_Reset"></a> Reset\(\)

```csharp
public void Reset()
```

### <a id="VirtualGeometry_World_PlanetLodBudgetController_Step_System_Int64_VirtualGeometry_World_PlanetLodBudgetMode_System_Double_VirtualGeometry_World_PlanetLodBudgetSample__VirtualGeometry_World_PlanetLodBudgetSignals_"></a> Step\(long, PlanetLodBudgetMode, double, in PlanetLodBudgetSample, PlanetLodBudgetSignals\)

1 frameの全Cameraに同じ倍率を返す。欠測があれば回復せず、有効な超過信号には反応する。

```csharp
public double Step(long frame, PlanetLodBudgetMode mode, double deltaSeconds, in PlanetLodBudgetSample sample, PlanetLodBudgetSignals monitored = PlanetLodBudgetSignals.All)
```

#### 引数（Parameters）

`frame` [long](https://learn.microsoft.com/dotnet/api/system.int64)

`mode` [PlanetLodBudgetMode](VirtualGeometry.World.PlanetLodBudgetMode.md)

`deltaSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`sample` [PlanetLodBudgetSample](VirtualGeometry.World.PlanetLodBudgetSample.md)

`monitored` [PlanetLodBudgetSignals](VirtualGeometry.World.PlanetLodBudgetSignals.md)

#### 戻り値（Returns）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
