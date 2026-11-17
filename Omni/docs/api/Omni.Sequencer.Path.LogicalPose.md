# <a id="Omni_Sequencer_Path_LogicalPose"></a> Struct LogicalPose

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

解決済みの姿勢。位置・回転は Logical の raw を正本にする。

```csharp
public readonly struct LogicalPose
```

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalPose__ctor_Omni_Logical_Position3__Omni_Logical_Quaternion__System_Single_"></a> LogicalPose\(in Position3, in Quaternion, float\)

```csharp
public LogicalPose(in Position3 position, in Quaternion rotation, float fieldOfView = 0)
```

#### 引数（Parameters）

`position` Position3

`rotation` Quaternion

`fieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalPose_FieldOfView"></a> FieldOfView

縦の画角(度)。0 は変えない。

```csharp
public readonly float FieldOfView
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Sequencer_Path_LogicalPose_Position"></a> Position

```csharp
public readonly Position3 Position
```

#### 値（Field Value）

 Position3

### <a id="Omni_Sequencer_Path_LogicalPose_Rotation"></a> Rotation

```csharp
public readonly Quaternion Rotation
```

#### 値（Field Value）

 Quaternion
