# <a id="Omni_Sequencer_Path_LogicalTimelineSample"></a> Struct LogicalTimelineSample

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

Timeline のミキサーが受け手へ渡す、ある時刻の有効なクリップ。

```csharp
public readonly struct LogicalTimelineSample
```

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalTimelineSample__ctor_System_String_System_Double_System_Double_System_Double_System_Single_"></a> LogicalTimelineSample\(string, double, double, double, float\)

```csharp
public LogicalTimelineSample(string clipId, double sequenceSeconds, double clipSeconds, double clipDuration, float weight)
```

#### 引数（Parameters）

`clipId` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sequenceSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clipSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`clipDuration` [double](https://learn.microsoft.com/dotnet/api/system.double)

`weight` [float](https://learn.microsoft.com/dotnet/api/system.single)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalTimelineSample_ClipDuration"></a> ClipDuration

```csharp
public readonly double ClipDuration
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineSample_ClipId"></a> ClipId

クリップの識別子(受け手が評価を選ぶ鍵)。

```csharp
public readonly string ClipId
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalTimelineSample_ClipSeconds"></a> ClipSeconds

クリップの先頭からの秒。

```csharp
public readonly double ClipSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineSample_SequenceSeconds"></a> SequenceSeconds

Timeline の先頭からの秒。

```csharp
public readonly double SequenceSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalTimelineSample_Weight"></a> Weight

```csharp
public readonly float Weight
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)
