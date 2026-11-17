# <a id="Omni_Converter_OmniMaterialShaderMappingStore"></a> Class OmniMaterialShaderMappingStore

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

既存Materialを直接Omni Shaderへ切り替えた履歴を永続化します。
Libraryやstatic状態に依存せず、Editor再起動後も同じMaterialを復元できます。

```csharp
public sealed class OmniMaterialShaderMappingStore : ScriptableObject
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_BuiltInReplacements"></a> BuiltInReplacements

```csharp
public IReadOnlyList<OmniMaterialShaderMappingStore.BuiltInReplacement> BuiltInReplacements { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)\>

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_DiagnosticReplacements"></a> DiagnosticReplacements

```csharp
public IReadOnlyList<OmniMaterialShaderMappingStore.DiagnosticReplacement> DiagnosticReplacements { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)\>

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Entries"></a> Entries

```csharp
public IReadOnlyList<OmniMaterialShaderMappingStore.Entry> Entries { get; }
```

#### 値（Property Value）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)\>

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_TransactionId"></a> TransactionId

```csharp
public string TransactionId { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_TransactionInProgress"></a> TransactionInProgress

```csharp
public bool TransactionInProgress { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Add_Omni_Converter_OmniMaterialShaderMappingStore_Entry_"></a> Add\(Entry\)

```csharp
public void Add(OmniMaterialShaderMappingStore.Entry entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Add_Omni_Converter_OmniMaterialShaderMappingStore_BuiltInReplacement_"></a> Add\(BuiltInReplacement\)

```csharp
public void Add(OmniMaterialShaderMappingStore.BuiltInReplacement entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Add_Omni_Converter_OmniMaterialShaderMappingStore_DiagnosticReplacement_"></a> Add\(DiagnosticReplacement\)

```csharp
public void Add(OmniMaterialShaderMappingStore.DiagnosticReplacement entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_BeginTransaction_System_String_"></a> BeginTransaction\(string\)

```csharp
public void BeginTransaction(string id)
```

#### 引数（Parameters）

`id` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_CompleteTransaction"></a> CompleteTransaction\(\)

```csharp
public void CompleteTransaction()
```

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Find_UnityEngine_Material_"></a> Find\(Material\)

```csharp
public OmniMaterialShaderMappingStore.Entry Find(Material material)
```

#### 引数（Parameters）

`material` Material

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_FindBuiltIn_UnityEngine_Material_UnityEngine_Shader_"></a> FindBuiltIn\(Material, Shader\)

```csharp
public OmniMaterialShaderMappingStore.BuiltInReplacement FindBuiltIn(Material original, Shader omniShader)
```

#### 引数（Parameters）

`original` Material

`omniShader` Shader

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_FindDiagnostic_UnityEngine_Material_"></a> FindDiagnostic\(Material\)

```csharp
public OmniMaterialShaderMappingStore.DiagnosticReplacement FindDiagnostic(Material original)
```

#### 引数（Parameters）

`original` Material

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_FindManagedBuiltIn_UnityEngine_Material_"></a> FindManagedBuiltIn\(Material\)

```csharp
public OmniMaterialShaderMappingStore.BuiltInReplacement FindManagedBuiltIn(Material managed)
```

#### 引数（Parameters）

`managed` Material

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_FindManagedDiagnostic_UnityEngine_Material_"></a> FindManagedDiagnostic\(Material\)

```csharp
public OmniMaterialShaderMappingStore.DiagnosticReplacement FindManagedDiagnostic(Material managed)
```

#### 引数（Parameters）

`managed` Material

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_LoadOrCreate"></a> LoadOrCreate\(\)

固定パスから台帳を読み、必要なら利用者データ領域へ作成します。

```csharp
public static OmniMaterialShaderMappingStore LoadOrCreate()
```

#### 戻り値（Returns）

 [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Remove_Omni_Converter_OmniMaterialShaderMappingStore_Entry_"></a> Remove\(Entry\)

```csharp
public void Remove(OmniMaterialShaderMappingStore.Entry entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[Entry](Omni.Converter.OmniMaterialShaderMappingStore.Entry.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Remove_Omni_Converter_OmniMaterialShaderMappingStore_BuiltInReplacement_"></a> Remove\(BuiltInReplacement\)

```csharp
public void Remove(OmniMaterialShaderMappingStore.BuiltInReplacement entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[BuiltInReplacement](Omni.Converter.OmniMaterialShaderMappingStore.BuiltInReplacement.md)

### <a id="Omni_Converter_OmniMaterialShaderMappingStore_Remove_Omni_Converter_OmniMaterialShaderMappingStore_DiagnosticReplacement_"></a> Remove\(DiagnosticReplacement\)

```csharp
public void Remove(OmniMaterialShaderMappingStore.DiagnosticReplacement entry)
```

#### 引数（Parameters）

`entry` [OmniMaterialShaderMappingStore](Omni.Converter.OmniMaterialShaderMappingStore.md).[DiagnosticReplacement](Omni.Converter.OmniMaterialShaderMappingStore.DiagnosticReplacement.md)
