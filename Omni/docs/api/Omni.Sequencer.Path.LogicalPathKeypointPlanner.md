# <a id="Omni_Sequencer_Path_LogicalPathKeypointPlanner"></a> Class LogicalPathKeypointPlanner

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

経路を解析して先読みの要点を作る。区切りは時間の等分ではなく、高度が半分(または倍)になるごと、
視線が画角の1/4回るごと、錨が変わるごと。解析だけに double を使い、要点の意図は経路の値をそのまま持つ。

```csharp
public static class LogicalPathKeypointPlanner
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LogicalPathKeypointPlanner](Omni.Sequencer.Path.LogicalPathKeypointPlanner.md)

## フィールド（Fields）

### <a id="Omni_Sequencer_Path_LogicalPathKeypointPlanner_DefaultFieldOfView"></a> DefaultFieldOfView

```csharp
public const float DefaultFieldOfView = 60
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Sequencer_Path_LogicalPathKeypointPlanner_DefaultMaximumKeypoints"></a> DefaultMaximumKeypoints

```csharp
public const int DefaultMaximumKeypoints = 256
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Sequencer_Path_LogicalPathKeypointPlanner_DefaultSamples"></a> DefaultSamples

```csharp
public const int DefaultSamples = 512
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_LogicalPathKeypointPlanner_Plan_Omni_Sequencer_Path_ILogicalPath_System_Int32_System_Int32_System_Single_"></a> Plan\(ILogicalPath, int, int, float\)

```csharp
public static List<LogicalPathKeypoint> Plan(ILogicalPath path, int samples = 512, int maximumKeypoints = 256, float defaultFieldOfView = 60)
```

#### 引数（Parameters）

`path` [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

`samples` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`maximumKeypoints` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`defaultFieldOfView` [float](https://learn.microsoft.com/dotnet/api/system.single)

#### 戻り値（Returns）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[LogicalPathKeypoint](Omni.Sequencer.Path.LogicalPathKeypoint.md)\>
