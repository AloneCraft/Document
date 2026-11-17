# <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry"></a> Class OmniMaterialShaderMappingStore.Entry

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

```csharp
[Serializable]
public sealed class OmniMaterialShaderMappingStore.Entry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniMaterialShaderMappingStore.Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)

## フィールド（Fields）

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedDoubleSidedGi"></a> AppliedDoubleSidedGi

```csharp
public bool AppliedDoubleSidedGi
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedGiFlags"></a> AppliedGiFlags

```csharp
public MaterialGlobalIlluminationFlags AppliedGiFlags
```

#### 値（Field Value）

 MaterialGlobalIlluminationFlags

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedInstancing"></a> AppliedInstancing

```csharp
public bool AppliedInstancing
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedKeywords"></a> AppliedKeywords

```csharp
public string[] AppliedKeywords
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedPasses"></a> AppliedPasses

```csharp
public List<OmniMaterialShaderMappingStore.PassState> AppliedPasses
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[PassState](Omni.Converter.OmniMaterialShaderMappingStore.PassState.md)\>

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedRawRenderQueue"></a> AppliedRawRenderQueue

```csharp
public int AppliedRawRenderQueue
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_AppliedStateHash"></a> AppliedStateHash

適用直後（最初の保存でURPが検証し直した後）のMaterialの保存内容を、利用者の編集かを見る形にした
hashです（Unityが描画時に書き足す既定値のPropertyと、URPが決めるPassの状態は含めません）。
標準へ戻す時点のhashと一致すれば、適用中に利用者の編集も外からの書換えも無かったとみなします。
空なら一致しないものとして扱います。

```csharp
public string AppliedStateHash
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_Material"></a> Material

```csharp
public Material Material
```

#### 値（Field Value）

 Material

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_MaterialGuid"></a> MaterialGuid

```csharp
public string MaterialGuid
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_MaterialLocalId"></a> MaterialLocalId

```csharp
public long MaterialLocalId
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OmniShader"></a> OmniShader

```csharp
public Shader OmniShader
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalDoubleSidedGi"></a> OriginalDoubleSidedGi

```csharp
public bool OriginalDoubleSidedGi
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalGiFlags"></a> OriginalGiFlags

```csharp
public MaterialGlobalIlluminationFlags OriginalGiFlags
```

#### 値（Field Value）

 MaterialGlobalIlluminationFlags

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalInstancing"></a> OriginalInstancing

```csharp
public bool OriginalInstancing
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalKeywords"></a> OriginalKeywords

```csharp
public string[] OriginalKeywords
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalMaterialFile"></a> OriginalMaterialFile

適用前のMaterialの保存内容（<code>EditorJsonUtility.ToJson</code>）です。標準へ戻すとき、適用中に
Materialが変わっていなければ（<xref href="Omni.Converter.OmniMaterialShaderMappingStore.Entry.AppliedStateHash" data-throw-if-not-resolved="false"></xref>が一致すれば）、APIで戻した後に
<code>EditorJsonUtility.FromJsonOverwrite</code>で上書きし、同じMaterialオブジェクトのまま保存内容を
適用前へ戻します。Shaderの代入やkeywordの設定でUnityが既定値のPropertyを補い、Shaderが宣言しない
keyword（<code>m_InvalidKeywords</code>）を落とすため、APIだけでは <code>.mat</code> が元と一致しません。
空の場合（この記録が無い旧Entry）はAPIで戻すだけです。

```csharp
public string OriginalMaterialFile
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalPasses"></a> OriginalPasses

```csharp
public List<OmniMaterialShaderMappingStore.PassState> OriginalPasses
```

#### 値（Field Value）

 [List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list\-1)<[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[PassState](Omni.Converter.OmniMaterialShaderMappingStore.PassState.md)\>

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalPersistedNamesKnown"></a> OriginalPersistedNamesKnown

```csharp
public bool OriginalPersistedNamesKnown
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalPersistedPropertyNames"></a> OriginalPersistedPropertyNames

```csharp
public string[] OriginalPersistedPropertyNames
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalRawRenderQueue"></a> OriginalRawRenderQueue

```csharp
public int OriginalRawRenderQueue
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalSavedPropertyNames"></a> OriginalSavedPropertyNames

適用前のMaterialが保存していたProperty名です。復元時に、適用中だけ増えたProperty
（Radial Shaderの <code>_RadialGlobal_*</code> 等）を元のMaterialへ持ち込まないために使います。
空の場合（この記録が無い旧Entry）は取り除きません。

```csharp
public string[] OriginalSavedPropertyNames
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)\[\]

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalShader"></a> OriginalShader

```csharp
public Shader OriginalShader
```

#### 値（Field Value）

 Shader

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalStateJson"></a> OriginalStateJson

```csharp
public string OriginalStateJson
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_OriginalStateSession"></a> OriginalStateSession

<xref href="Omni.Converter.OmniMaterialShaderMappingStore.Entry.OriginalStateJson" data-throw-if-not-resolved="false"></xref>を書いたEditorの起動の識別子です。<code>EditorJsonUtility.ToJson</code>はShaderとTextureの参照を
その起動の中でだけ有効なinstance IDで書くので、Editorを開き直した後の上書きは参照を壊します（Shaderがnullのピンクになる）。
今の起動の識別子と違えば、上書きはせずAPIで戻します。

```csharp
public string OriginalStateSession
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_RestorePending"></a> RestorePending

```csharp
public bool RestorePending
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entry_TransactionId"></a> TransactionId

```csharp
public string TransactionId
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
