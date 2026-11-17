# <a id="Omni_Sequencer_Path_ILogicalKeyframeSink"></a> Interface ILogicalKeyframeSink

Namespace: [Omni.Sequencer.Path](Omni.Sequencer.Path.md)  
Assembly: Omni.Sequencer.Runtime.dll  

キーフレームのトラックの評価の受け手。書くのは受け手。

```csharp
public interface ILogicalKeyframeSink
```

## メソッド（Methods）

### <a id="Omni_Sequencer_Path_ILogicalKeyframeSink_PresentKeyframes_System_Double_"></a> PresentKeyframes\(double\)

有効なクリップがある時刻(Timeline の先頭からの秒)。

```csharp
void PresentKeyframes(double sequenceSeconds)
```

#### 引数（Parameters）

`sequenceSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Sequencer_Path_ILogicalKeyframeSink_PresentNoKeyframes_System_Double_"></a> PresentNoKeyframes\(double\)

有効なクリップが無い時刻。

```csharp
void PresentNoKeyframes(double sequenceSeconds)
```

#### 引数（Parameters）

`sequenceSeconds` [double](https://learn.microsoft.com/dotnet/api/system.double)
