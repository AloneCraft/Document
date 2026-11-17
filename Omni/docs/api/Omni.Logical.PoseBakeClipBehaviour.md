# <a id="Omni_Logical_PoseBakeClipBehaviour"></a> Class PoseBakeClipBehaviour

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

```csharp
[MovedFrom(true, "Omni.Sequencer.Timeline", null, "LogicalPoseBakeClipBehaviour")]
public class PoseBakeClipBehaviour : PlayableBehaviour, IPlayableBehaviour, ICloneable
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
PlayableBehaviour ← 
[PoseBakeClipBehaviour](Omni.Logical.PoseBakeClipBehaviour.md)

#### 実装するインターフェース（Implements）

IPlayableBehaviour, 
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable)

## フィールド（Fields）

### <a id="Omni_Logical_PoseBakeClipBehaviour_Bake"></a> Bake

参照するベイクアセット。

```csharp
public PoseBake Bake
```

#### 値（Field Value）

 [PoseBake](Omni.Logical.PoseBake.md)

### <a id="Omni_Logical_PoseBakeClipBehaviour_ChannelTargetPath"></a> ChannelTargetPath

駆動対象のチャンネル識別子。

```csharp
public string ChannelTargetPath
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Logical_PoseBakeClipBehaviour_ClipStart"></a> ClipStart

このクリップがシーケンス上で始まる時刻（秒）。

```csharp
public double ClipStart
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)
