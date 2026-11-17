# <a id="Omni_NativeDraw_Generation_GrassIndirectPlan"></a> Class GrassIndirectPlan

Namespace: [Omni.NativeDraw.Generation](Omni.NativeDraw.Generation.md)  
Assembly: Omni.Manager.dll  

```csharp
public sealed class GrassIndirectPlan
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md)

## フィールド（Fields）

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_BridgeType"></a> BridgeType

```csharp
public const string BridgeType = "global::Omni.Generated.GrassIndirect.DrawResources"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_CompilationField"></a> CompilationField

```csharp
public const string CompilationField = "OmniGrassGeneratedFingerprint"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Schema"></a> Schema

```csharp
public const string Schema = "grass-indirect-explicit-resources-v1"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Data"></a> Data

```csharp
public GrassIndirectPlan.Manifest Data { get; }
```

#### 値（Property Value）

 [GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md).[Manifest](Omni.NativeDraw.Generation.GrassIndirectPlan.Manifest.md)

## メソッド（Methods）

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Apply_System_String_System_Action_System_Int32__System_Action_Omni_NativeDraw_Generation_GrassIndirectPlan_Manifest__"></a> Apply\(string, Action<int\>, Action<Manifest\>\)

```csharp
public void Apply(string projectRoot, Action<int> afterWrite = null, Action<GrassIndirectPlan.Manifest> beforeWrite = null)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`afterWrite` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

`beforeWrite` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md).[Manifest](Omni.NativeDraw.Generation.GrassIndirectPlan.Manifest.md)\>

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_BeginSerializedAssetChange_System_String_System_String_System_String_"></a> BeginSerializedAssetChange\(string, string, string\)

```csharp
public string BeginSerializedAssetChange(string projectRoot, string assetPath, string journalPath)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`journalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Build_System_String_System_String_System_String_System_Collections_Generic_IReadOnlyDictionary_System_String_System_String__System_Collections_Generic_IReadOnlyDictionary_System_String_System_Byte____System_Collections_Generic_IReadOnlyDictionary_System_String_System_String__"></a> Build\(string, string, string, IReadOnlyDictionary<string, string\>, IReadOnlyDictionary<string, byte\[\]\>, IReadOnlyDictionary<string, string\>\)

```csharp
public static GrassIndirectPlan Build(string sourceRoot, string outputRoot, string sourceProfile, IReadOnlyDictionary<string, string> fingerprints, IReadOnlyDictionary<string, byte[]> inputs, IReadOnlyDictionary<string, string> templates)
```

#### 引数（Parameters）

`sourceRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`outputRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceProfile` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fingerprints` [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

`inputs` [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]\>

`templates` [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_CaptureCreatedMetadata_System_String_"></a> CaptureCreatedMetadata\(string\)

```csharp
public void CaptureCreatedMetadata(string projectRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_CompleteSerializedAssetChange_System_String_System_String_System_String_System_String_System_Action_Omni_NativeDraw_Generation_GrassIndirectPlan_Manifest__"></a> CompleteSerializedAssetChange\(string, string, string, string, Action<Manifest\>\)

```csharp
public void CompleteSerializedAssetChange(string projectRoot, string assetPath, string journalPath, string transaction, Action<GrassIndirectPlan.Manifest> persistManifest)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`journalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`transaction` [string](https://learn.microsoft.com/dotnet/api/system.string)

`persistManifest` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md).[Manifest](Omni.NativeDraw.Generation.GrassIndirectPlan.Manifest.md)\>

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_FromManifest_Omni_NativeDraw_Generation_GrassIndirectPlan_Manifest_"></a> FromManifest\(Manifest\)

```csharp
public static GrassIndirectPlan FromManifest(GrassIndirectPlan.Manifest manifest)
```

#### 引数（Parameters）

`manifest` [GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md).[Manifest](Omni.NativeDraw.Generation.GrassIndirectPlan.Manifest.md)

#### 戻り値（Returns）

 [GrassIndirectPlan](Omni.NativeDraw.Generation.GrassIndirectPlan.md)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Hash_System_Byte___"></a> Hash\(byte\[\]\)

```csharp
public static string Hash(byte[] bytes)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_ReadSourceInventory_System_String_System_String_"></a> ReadSourceInventory\(string, string\)

Grass の source 全体を列挙し、未知のコードを計画前の照合に含める。

```csharp
public static Dictionary<string, byte[]> ReadSourceInventory(string projectRoot, string sourceRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]\>

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_RecordSerializedAssetChange_System_String_System_String_System_Byte___"></a> RecordSerializedAssetChange\(string, string, byte\[\]\)

```csharp
public void RecordSerializedAssetChange(string projectRoot, string assetPath, byte[] original)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`original` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_RecoverSerializedAssetJournal_System_String_System_String_System_String_System_Action_"></a> RecoverSerializedAssetJournal\(string, string, string, Action\)

排他を保持した呼出し側が、中断 journal の安全な完了状態だけを解消する。

```csharp
public void RecoverSerializedAssetJournal(string projectRoot, string assetPath, string journalPath, Action verifyManifest)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`journalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`verifyManifest` [Action](https://learn.microsoft.com/dotnet/api/system.action)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_Restore_System_String_System_Action_System_Int32__"></a> Restore\(string, Action<int\>\)

```csharp
public void Restore(string projectRoot, Action<int> afterRestore = null)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`afterRestore` [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[int](https://learn.microsoft.com/dotnet/api/system.int32)\>

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_ValidateApplicableState_System_String_"></a> ValidateApplicableState\(string\)

資産を変更せず、Apply と同じ入力・出力衝突を確認する。

```csharp
public void ValidateApplicableState(string projectRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_ValidateInstalledState_System_String_"></a> ValidateInstalledState\(string\)

記録済みの導入資産を変更せず、生成後の内容と一致するか確認する。

```csharp
public void ValidateInstalledState(string projectRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_ValidateRestoredState_System_String_"></a> ValidateRestoredState\(string\)

元資産と削除対象が復元済みであることを、実ファイルから確認する。

```csharp
public void ValidateRestoredState(string projectRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassIndirectPlan_ValidateSerializedAssetJournal_System_String_System_String_System_String_System_Action_"></a> ValidateSerializedAssetJournal\(string, string, string, Action\)

中断 journal を変更せず、解消可能な状態だけを検証する。

```csharp
public void ValidateSerializedAssetJournal(string projectRoot, string assetPath, string journalPath, Action verifyManifest)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

`assetPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`journalPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`verifyManifest` [Action](https://learn.microsoft.com/dotnet/api/system.action)
