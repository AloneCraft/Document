# <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore"></a> Class OmniAiConversionStore

Namespace: [Omni.Editor.Manager.AiConversion](Omni.Editor.Manager.AiConversion.md)  
Assembly: Omni.Manager.dll  

個人の作業記録（Git の外）の読み書きです。置き場は <code>&lt;プロジェクト&gt;/UserSettings/Omni/AiConversion/&lt;sourceGuid&gt;/</code>。
読み込みは、ファイルが無い・壊れている・形式が違うときに null を返し、例外を投げません。書き込みは一時ファイルへ書いてから置き換えます。
プロジェクトの場所はコンストラクタで差し替えられます（テスト用）。

```csharp
public sealed class OmniAiConversionStore
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniAiConversionStore](Omni.Editor.Manager.AiConversion.OmniAiConversionStore.md)

## コンストラクター（Constructors）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore__ctor_System_String_"></a> OmniAiConversionStore\(string\)

```csharp
public OmniAiConversionStore(string projectRoot)
```

#### 引数（Parameters）

`projectRoot` [string](https://learn.microsoft.com/dotnet/api/system.string)

## フィールド（Fields）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_JudgeFileName"></a> JudgeFileName

```csharp
public const string JudgeFileName = "judge.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_RelativeBaseDirectory"></a> RelativeBaseDirectory

```csharp
public const string RelativeBaseDirectory = "UserSettings/Omni/AiConversion"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_RequestFileName"></a> RequestFileName

```csharp
public const string RequestFileName = "request.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ResultFileName"></a> ResultFileName

```csharp
public const string ResultFileName = "result.json"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_Default"></a> Default

このプロジェクトの記録。最初の参照は main thread で行う（Application.dataPath を使うため）。

```csharp
public static OmniAiConversionStore Default { get; }
```

#### 値（Property Value）

 [OmniAiConversionStore](Omni.Editor.Manager.AiConversion.OmniAiConversionStore.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ProjectRoot"></a> ProjectRoot

```csharp
public string ProjectRoot { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ArchiveResult_System_String_System_Int32_"></a> ArchiveResult\(string, int\)

現在の結果 JSON を <code>result.&lt;attempt&gt;.json</code> へ移し、新しい依頼の結果を検出できるようにします。
結果が無ければ何もしない。移せたら true。

```csharp
public bool ArchiveResult(string guid, int attempt)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_CreateSnapshot_System_String_System_Int32_System_Collections_Generic_IEnumerable_System_String__"></a> CreateSnapshot\(string, int, IEnumerable<string\>\)

退避を作る。失敗は null（<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionStore.TryCreateSnapshot(System.String%2cSystem.Int32%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d%2cOmni.Editor.Manager.AiConversion.OmniAiSnapshotManifest%40%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> で理由が分かる）。

```csharp
public OmniAiSnapshotManifest CreateSnapshot(string guid, int attempt, IEnumerable<string> projectRelativePaths)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`projectRelativePaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [OmniAiSnapshotManifest](Omni.Editor.Manager.AiConversion.OmniAiSnapshotManifest.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_DescribeRestore_System_String_System_Int32_System_Collections_Generic_IEnumerable_System_String__"></a> DescribeRestore\(string, int, IEnumerable<string\>\)

退避と今のファイルを比べ、ファイルごとの戻し方を説明します。退避が無ければ null。
<code class="paramref">extraPaths</code> は退避に無いが AI が作った可能性のあるファイル（結果 JSON の modifiedFiles）。

```csharp
public IReadOnlyList<OmniAiRestoreItem> DescribeRestore(string guid, int attempt, IEnumerable<string> extraPaths = null)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`extraPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[OmniAiRestoreItem](Omni.Editor.Manager.AiConversion.OmniAiRestoreItem.md)\>

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_DetectProjectRoot"></a> DetectProjectRoot\(\)

```csharp
public static string DetectProjectRoot()
```

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_DirectoryFor_System_String_"></a> DirectoryFor\(string\)

```csharp
public string DirectoryFor(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_IsValidGuid_System_String_"></a> IsValidGuid\(string\)

sourceGuid として使える文字列か（32 桁の 16 進）。パスの組み立てに使うので、それ以外は拒否する。

```csharp
public static bool IsValidGuid(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_JudgePath_System_String_"></a> JudgePath\(string\)

```csharp
public string JudgePath(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_LoadJudge_System_String_"></a> LoadJudge\(string\)

```csharp
public OmniJudgeReport LoadJudge(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniJudgeReport](Omni.Editor.Manager.AiConversion.OmniJudgeReport.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_LoadManifest_System_String_System_Int32_"></a> LoadManifest\(string, int\)

退避の一覧を読む。無い・壊れているときは null。

```csharp
public OmniAiSnapshotManifest LoadManifest(string guid, int attempt)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [OmniAiSnapshotManifest](Omni.Editor.Manager.AiConversion.OmniAiSnapshotManifest.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_LoadRequest_System_String_"></a> LoadRequest\(string\)

```csharp
public OmniAiRequest LoadRequest(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniAiRequest](Omni.Editor.Manager.AiConversion.OmniAiRequest.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_LoadResult_System_String_"></a> LoadResult\(string\)

```csharp
public OmniAiConversionResult LoadResult(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_RecordAiOutput_System_String_System_Int32_System_Collections_Generic_IEnumerable_System_String__System_Boolean_"></a> RecordAiOutput\(string, int, IEnumerable<string\>, bool\)

AI が作業を終えた時点の各ファイルのハッシュを記録します（退避した各ファイルと <code class="paramref">extraPaths</code>）。
以後、<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionStore.DescribeRestore(System.String%2cSystem.Int32%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d)" data-throw-if-not-resolved="false"></xref> が「AI の後に人が直した」ファイルを検出できます。結果の取り込み時と、最初の再判定で呼びます。
既に記録済みなら上書きしません（<code class="paramref">overwrite</code> が true のときを除く）。

```csharp
public bool RecordAiOutput(string guid, int attempt, IEnumerable<string> extraPaths = null, bool overwrite = false)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`extraPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`overwrite` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_RequestPath_System_String_"></a> RequestPath\(string\)

```csharp
public string RequestPath(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_Restore_System_String_System_Int32_System_Collections_Generic_IEnumerable_System_String__System_Collections_Generic_IEnumerable_System_String__System_Func_System_String_System_Boolean__"></a> Restore\(string, int, IEnumerable<string\>, IEnumerable<string\>, Func<string, bool\>\)

退避から戻します。変更・削除されたファイルは元の内容を書き戻し、AI が作ったファイルは
<code class="paramref">moveToTrash</code>（既定は <xref href="UnityEditor.AssetDatabase.MoveAssetToTrash(System.String)" data-throw-if-not-resolved="false"></xref>）で Unity のごみ箱へ移します。
<code class="paramref">onlyPaths</code> が null なら変更のあるファイルすべて。書き戻した後は、呼び出し側で <code>AssetDatabase.Refresh</code> または各 <code>ImportAsset</code> が要ります。

```csharp
public OmniAiRestoreReport Restore(string guid, int attempt, IEnumerable<string> onlyPaths = null, IEnumerable<string> extraPaths = null, Func<string, bool> moveToTrash = null)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`onlyPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`extraPaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`moveToTrash` [Func](https://learn.microsoft.com/dotnet/api/system.func\-2)<[string](https://learn.microsoft.com/dotnet/api/system.string), [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

#### 戻り値（Returns）

 [OmniAiRestoreReport](Omni.Editor.Manager.AiConversion.OmniAiRestoreReport.md)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ResultLastWriteUtc_System_String_"></a> ResultLastWriteUtc\(string\)

結果 JSON の最終更新時刻（UTC）。ファイルが無ければ null。

```csharp
public DateTime? ResultLastWriteUtc(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)?

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ResultPath_System_String_"></a> ResultPath\(string\)

```csharp
public string ResultPath(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ResultRelativePath_System_String_"></a> ResultRelativePath\(string\)

エージェントへ渡す結果 JSON の書き先（プロジェクト相対、/ 区切り）。

```csharp
public static string ResultRelativePath(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_SaveJudge_System_String_Omni_Editor_Manager_AiConversion_OmniJudgeReport_"></a> SaveJudge\(string, OmniJudgeReport\)

```csharp
public bool SaveJudge(string guid, OmniJudgeReport report)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`report` [OmniJudgeReport](Omni.Editor.Manager.AiConversion.OmniJudgeReport.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_SaveRequest_System_String_Omni_Editor_Manager_AiConversion_OmniAiRequest_"></a> SaveRequest\(string, OmniAiRequest\)

```csharp
public bool SaveRequest(string guid, OmniAiRequest request)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`request` [OmniAiRequest](Omni.Editor.Manager.AiConversion.OmniAiRequest.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_SaveResult_System_String_Omni_Editor_Manager_AiConversion_OmniAiConversionResult_"></a> SaveResult\(string, OmniAiConversionResult\)

結果 JSON を保存します（チャットの貼り付けを取り込むとき）。

```csharp
public bool SaveResult(string guid, OmniAiConversionResult result)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`result` [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_Sha256Hex_System_Byte___"></a> Sha256Hex\(byte\[\]\)

内容の SHA-256（小文字の 16 進）。

```csharp
public static string Sha256Hex(byte[] bytes)
```

#### 引数（Parameters）

`bytes` [byte](https://learn.microsoft.com/dotnet/api/system.byte)\[\]

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_SnapshotDirectory_System_String_System_Int32_"></a> SnapshotDirectory\(string, int\)

```csharp
public string SnapshotDirectory(string guid, int attempt)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_ToAbsolute_System_String_"></a> ToAbsolute\(string\)

プロジェクト相対パスの絶対パス。安全でないパス（絶対、<code>..</code> を含む）は null。

```csharp
public string ToAbsolute(string projectRelativePath)
```

#### 引数（Parameters）

`projectRelativePath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Manager_AiConversion_OmniAiConversionStore_TryCreateSnapshot_System_String_System_Int32_System_Collections_Generic_IEnumerable_System_String__Omni_Editor_Manager_AiConversion_OmniAiSnapshotManifest__System_String__"></a> TryCreateSnapshot\(string, int, IEnumerable<string\>, out OmniAiSnapshotManifest, out string\)

依頼時のファイルを <code>snapshots/&lt;attempt&gt;/files/&lt;相対パス&gt;</code> へ写し、manifest（パスとハッシュ。無いファイルは "absent"）を書く。
同じ attempt の退避があれば作り直す。安全でないパスが 1 つでもあれば何も作らない。

```csharp
public bool TryCreateSnapshot(string guid, int attempt, IEnumerable<string> projectRelativePaths, out OmniAiSnapshotManifest manifest, out string error)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

`attempt` [int](https://learn.microsoft.com/dotnet/api/system.int32)

`projectRelativePaths` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`manifest` [OmniAiSnapshotManifest](Omni.Editor.Manager.AiConversion.OmniAiSnapshotManifest.md)

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
