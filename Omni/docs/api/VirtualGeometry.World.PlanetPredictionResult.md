# <a id="VirtualGeometry_World_PlanetPredictionResult"></a> Struct PlanetPredictionResult

Namespace: [VirtualGeometry.World](VirtualGeometry.World.md)  
Assembly: Omni.VirtualGeometry.Runtime.dll  

描画を変更しない先読み結果。必須経路では選択上限と予約容量不足を区別する。

```csharp
public readonly struct PlanetPredictionResult
```

## コンストラクター（Constructors）

### <a id="VirtualGeometry_World_PlanetPredictionResult__ctor_System_Int32_System_Int32_System_Boolean_"></a> PlanetPredictionResult\(int, int, bool\)

```csharp
public PlanetPredictionResult(int required, int missing, bool budget)
```

#### 引数（Parameters）

`required` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`missing` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`budget` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetPredictionResult__ctor_System_Int32_System_Int32_System_Boolean_System_Boolean_System_Boolean_System_Int32_System_Int32_System_Boolean_"></a> PlanetPredictionResult\(int, int, bool, bool, bool, int, int, bool\)

```csharp
public PlanetPredictionResult(int required, int missing, bool budget, bool selectionLimited, bool admissionLimited, int closureRequired, int newSlots, bool temporarilyBlocked = false)
```

#### 引数（Parameters）

`required` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`missing` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`budget` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`selectionLimited` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`admissionLimited` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

`closureRequired` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`newSlots` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`temporarilyBlocked` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## フィールド（Fields）

### <a id="VirtualGeometry_World_PlanetPredictionResult_AdmissionLimited"></a> AdmissionLimited

```csharp
public readonly bool AdmissionLimited
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetPredictionResult_BudgetLimited"></a> BudgetLimited

```csharp
public readonly bool BudgetLimited
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetPredictionResult_ClosureRequired"></a> ClosureRequired

```csharp
public readonly int ClosureRequired
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetPredictionResult_Missing"></a> Missing

```csharp
public readonly int Missing
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetPredictionResult_NewSlots"></a> NewSlots

```csharp
public readonly int NewSlots
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetPredictionResult_Required"></a> Required

```csharp
public readonly int Required
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="VirtualGeometry_World_PlanetPredictionResult_SelectionLimited"></a> SelectionLimited

```csharp
public readonly bool SelectionLimited
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="VirtualGeometry_World_PlanetPredictionResult_TemporarilyBlocked"></a> TemporarilyBlocked

```csharp
public readonly bool TemporarilyBlocked
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## プロパティ（Properties）

### <a id="VirtualGeometry_World_PlanetPredictionResult_Ready"></a> Ready

```csharp
public bool Ready { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
