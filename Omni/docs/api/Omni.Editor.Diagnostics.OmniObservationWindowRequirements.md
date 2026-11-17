# <a id="Omni_Editor_Diagnostics_OmniObservationWindowRequirements"></a> Struct OmniObservationWindowRequirements

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

観測窓の間に満たすべき前提です。

```csharp
[Serializable]
public struct OmniObservationWindowRequirements
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniObservationWindowRequirements_minimumObservedFrames"></a> minimumObservedFrames

窓の間に進むべき描画回数の下限です。0 なら照合しません。

```csharp
public long minimumObservedFrames
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniObservationWindowRequirements_requireBrgAdvance"></a> requireBrgAdvance

```csharp
public bool requireBrgAdvance
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniObservationWindowRequirements_requireForegroundThroughout"></a> requireForegroundThroughout

```csharp
public bool requireForegroundThroughout
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
