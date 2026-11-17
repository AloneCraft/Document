# <a id="Omni_Editor_Diagnostics_OmniImageEvidence"></a> Struct OmniImageEvidence

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

画像から数えた、比較の対象と背景の画素数です。

```csharp
[Serializable]
public struct OmniImageEvidence
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniImageEvidence_hasTargetMask"></a> hasTargetMask

```csharp
public bool hasTargetMask
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniImageEvidence_nonBackgroundPixels"></a> nonBackgroundPixels

背景色と閾値以上に違う画素数です（mask があれば mask 内だけを数えます）。

```csharp
public int nonBackgroundPixels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniImageEvidence_targetPixels"></a> targetPixels

mask 内の画素数です。mask が無い場合は全画素数です。

```csharp
public int targetPixels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniImageEvidence_totalPixels"></a> totalPixels

```csharp
public int totalPixels
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)
