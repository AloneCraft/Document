# <a id="Omni_Sequencer_Path_LogicalKeyframe"></a> Struct LogicalKeyframe

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

キー 1 つ。時刻はクリップの中の秒(標準の Animation クリップのキーと同じ)。値はチャンネルごとの double。

```csharp
[Serializable]
public struct LogicalKeyframe
```

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalKeyframe__ctor_System_Double_System_String_System_Double___"></a> LogicalKeyframe\(double, string, params double\[\]\)

```csharp
public LogicalKeyframe(double time, string label, params double[] values)
```

#### 引数（Parameters）

`time` [double](https://learn.microsoft.com/dotnet/api/system.double)

`label` [string](https://learn.microsoft.com/dotnet/api/system.string)

`values` [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalKeyframe_label"></a> label

```csharp
[Tooltip("キーの名前(区間の名前など)。")]
public string label
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Sequencer_Path_LogicalKeyframe_time"></a> time

```csharp
[Tooltip("クリップの中の秒。")]
public double time
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalKeyframe_values"></a> values

```csharp
[Tooltip("チャンネルごとの値。数はクリップのチャンネルの数と同じ。")]
public double[] values
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)\[\]
