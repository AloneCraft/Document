# <a id="Omni_Sequencer_Path_ILogicalPathGate"></a> Interface ILogicalPathGate

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

移動の許可。要求した秒数のうち、今回進めてよい秒数を返す。

```csharp
public interface ILogicalPathGate
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalPathGate_Request_Omni_Sequencer_Path_ILogicalPath_System_Double_System_Double_"></a> Request\(ILogicalPath, double, double\)

```csharp
LogicalPathPermit Request(ILogicalPath path, double pathSeconds, double requestedSeconds)
```

#### 引数（Parameters）

`path` [ILogicalPath](Omni.Sequencer.Path.ILogicalPath.md)

`pathSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

`requestedSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

#### 戻り値（Returns）

 [LogicalPathPermit](Omni.Sequencer.Path.LogicalPathPermit.md)
