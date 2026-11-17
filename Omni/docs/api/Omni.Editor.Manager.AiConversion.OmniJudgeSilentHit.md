# <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit"></a> Class OmniJudgeSilentHit

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

生成に成功しても黙ってワープされない書き方の検出結果です（J3）。

```csharp
[Serializable]
public sealed class OmniJudgeSilentHit
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniJudgeSilentHit](Omni.Editor.Manager.AiConversion.OmniJudgeSilentHit.md)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_approved"></a> approved

利用者が「この検出は誤り」と承認済みか。

```csharp
public bool approved
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_file"></a> file

```csharp
public string file
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_fingerprint"></a> fingerprint

この検出箇所の指紋（承認の記録に使う）。

```csharp
public string fingerprint
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_line"></a> line

```csharp
public int line
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_pass"></a> pass

```csharp
public string pass
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniJudgeSilentHit_pattern"></a> pattern

```csharp
public string pattern
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
