# <a id="Omni_Sequencer_Path_LogicalPathPermit"></a> Struct LogicalPathPermit

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
public readonly struct LogicalPathPermit
```

## コンストラクター（Constructors）

### <a id="Omni_Sequencer_Path_LogicalPathPermit__ctor_System_Double_System_String_"></a> LogicalPathPermit\(double, string\)

```csharp
public LogicalPathPermit(double allowedSeconds, string failure = null)
```

#### 引数（Parameters）

`allowedSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`failure` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalPathPermit_AllowedSeconds"></a> AllowedSeconds

```csharp
public readonly double AllowedSeconds
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_LogicalPathPermit_Failure"></a> Failure

null なら成功。値があれば経路を有限に終える理由。

```csharp
public readonly string Failure
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalPathPermit_Allow_System_Double_"></a> Allow\(double\)

```csharp
public static LogicalPathPermit Allow(double seconds)
```

#### 引数（Parameters）

`seconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [LogicalPathPermit](Omni.Sequencer.Path.LogicalPathPermit.md)

### <a id="Omni_Sequencer_Path_LogicalPathPermit_Fail_System_String_"></a> Fail\(string\)

```csharp
public static LogicalPathPermit Fail(string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [LogicalPathPermit](Omni.Sequencer.Path.LogicalPathPermit.md)
