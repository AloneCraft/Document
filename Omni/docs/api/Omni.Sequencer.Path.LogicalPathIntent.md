# <a id="Omni_Sequencer_Path_LogicalPathIntent"></a> Struct LogicalPathIntent

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

経路のある時刻の「意図」。地面の高さや錨の現在姿勢を含まない(後から届いて変わる値は解決器が当てはめる)。
時刻だけで決まり、経路の開始後に変わらない。

```csharp
public readonly struct LogicalPathIntent : IEquatable<LogicalPathIntent>
```

#### 実装するインターフェース（Implements）

[IEquatable<LogicalPathIntent\>](https://learn.microsoft.com/dotnet/api/system.iequatable\-1)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Altitude"></a> Altitude

```csharp
public readonly Scalar Altitude
```

#### 値（Field Value）

 Scalar

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Anchor"></a> Anchor

アプリが決める錨の番号(例: 天体)。Absolute では使わない。

```csharp
public readonly int Anchor
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_AnchorKind"></a> AnchorKind

```csharp
public readonly LogicalPathAnchorKind AnchorKind
```

#### 値（Field Value）

 [LogicalPathAnchorKind](Omni.Sequencer.Path.LogicalPathAnchorKind.md)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Direction"></a> Direction

```csharp
public readonly Vector3 Direction
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Sequencer_Path_LogicalPathIntent_FieldOfView"></a> FieldOfView

縦の画角(度)。0 は変えない。

```csharp
public readonly float FieldOfView
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Offset"></a> Offset

```csharp
public readonly Vector3 Offset
```

#### 値（Field Value）

 Vector3

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Placement"></a> Placement

```csharp
public readonly LogicalPathPlacement Placement
```

#### 値（Field Value）

 [LogicalPathPlacement](Omni.Sequencer.Path.LogicalPathPlacement.md)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Rotation"></a> Rotation

錨の座標系での向き。

```csharp
public readonly Quaternion Rotation
```

#### 値（Field Value）

 Quaternion

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalPathIntent_AtOffset_Omni_Sequencer_Path_LogicalPathAnchorKind_System_Int32_Omni_Logical_Vector3__Omni_Logical_Quaternion__System_Single_"></a> AtOffset\(LogicalPathAnchorKind, int, in Vector3, in Quaternion, float\)

```csharp
public static LogicalPathIntent AtOffset(LogicalPathAnchorKind kind, int anchor, in Vector3 offset, in Quaternion rotation, float fieldOfView = 0)
```

#### 引数（Parameters）

`kind` [LogicalPathAnchorKind](Omni.Sequencer.Path.LogicalPathAnchorKind.md)

`anchor` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`offset` Vector3

`rotation` Quaternion

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_AtSurface_Omni_Sequencer_Path_LogicalPathAnchorKind_System_Int32_Omni_Logical_Vector3__Omni_Logical_Scalar__Omni_Logical_Quaternion__System_Single_"></a> AtSurface\(LogicalPathAnchorKind, int, in Vector3, in Scalar, in Quaternion, float\)

```csharp
public static LogicalPathIntent AtSurface(LogicalPathAnchorKind kind, int anchor, in Vector3 direction, in Scalar altitude, in Quaternion rotation, float fieldOfView = 0)
```

#### 引数（Parameters）

`kind` [LogicalPathAnchorKind](Omni.Sequencer.Path.LogicalPathAnchorKind.md)

`anchor` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`direction` Vector3

`altitude` Scalar

`rotation` Quaternion

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Equals_Omni_Sequencer_Path_LogicalPathIntent_"></a> Equals\(LogicalPathIntent\)

```csharp
public bool Equals(LogicalPathIntent other)
```

#### 引数（Parameters）

`other` [LogicalPathIntent](Omni.Sequencer.Path.LogicalPathIntent.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_Equals_System_Object_"></a> Equals\(object\)

```csharp
public override bool Equals(object obj)
```

#### 引数（Parameters）

`obj` [object](https://learn.microsoft.com/dotnet/api/system.object)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Sequencer_Path_LogicalPathIntent_GetHashCode"></a> GetHashCode\(\)

```csharp
public override int GetHashCode()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
