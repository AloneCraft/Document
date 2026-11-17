# <a id="Omni_Converter_OmniGuidManifest"></a> Class OmniGuidManifest

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

<code>Assets/Radial/</code> 配下の生成物パス→GUID の対応を記録する、
Unity Assetではないプロジェクト設定マニフェストです。正本は
<code>ProjectSettings/Omni/Generated.manifest.json</code>に置きます。

<p>
<code>Assets/Radial/</code> はディスク上のキャッシュとして丸ごと削除・
再生成できますが、削除後に再生成すると <xref href="UnityEditor.AssetDatabase.CreateAsset(UnityEngine.Object%2cSystem.String)" data-throw-if-not-resolved="false"></xref>
は新しい GUID を発行します。シーンファイルは committed であり、生成物への
参照が GUID で焼き込まれているため、削除→再生成のたびにシーン参照が
永久に壊れる事故が起きていました（2026-08-01 のTerminalScene破損の根本原因）。
</p>
<p>
Unity は、アセットをインポートする前に <code>.meta</code> ファイルが既に存在していれば
そこに書かれた GUID を採用します。このマニフェストは「このパスには過去このGUIDを
割り当てた」という記録を git 管理下に置き、次回生成時に同じ GUID の <code>.meta</code> を
先に書き込むことで、フォルダを丸ごと消して作り直しても GUID が再現されるようにします。
</p>

```csharp
public static class OmniGuidManifest
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniGuidManifest](Omni.Converter.OmniGuidManifest.md)

## プロパティ（Properties）

### <a id="Omni_Converter_OmniGuidManifest_HasPendingChanges"></a> HasPendingChanges

```csharp
public static bool HasPendingChanges { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_LastSaveResult"></a> LastSaveResult

```csharp
public static OmniGuidManifest.SaveResult LastSaveResult { get; }
```

#### 値（Property Value）

 [OmniGuidManifest](Omni.Converter.OmniGuidManifest.md).[SaveResult](Omni.Converter.OmniGuidManifest.SaveResult.md)

## メソッド（Methods）

### <a id="Omni_Converter_OmniGuidManifest_EnumeratePaths"></a> EnumeratePaths\(\)

記録済みの生成物パスを列挙します（バックフィル・検証用）。

```csharp
public static IEnumerable<string> EnumeratePaths()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniGuidManifest_HasEntry_System_String_"></a> HasEntry\(string\)

この生成物パスのエントリが<b>存在するか</b>どうか。

<p>
<xref href="Omni.Converter.OmniGuidManifest.HasSourceInfo(System.String)" data-throw-if-not-resolved="false"></xref> とは別物です。エントリ自体が無い「孤児」の生成物は
<xref href="Omni.Converter.OmniGuidManifest.EnumeratePaths" data-throw-if-not-resolved="false"></xref> に現れないため、バックフィルの走査から漏れます。
「バックフィルを実行してください」と案内してよいのはエントリがある場合だけなので、
報告の出し分けにこちらを使ってください。
</p>

```csharp
public static bool HasEntry(string generatedPath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_HasSourceInfo_System_String_"></a> HasSourceInfo\(string\)

逆引き情報が入っているかどうか。バックフィルの対象判定に使います。

```csharp
public static bool HasSourceInfo(string generatedPath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_IsRecordedGuid_System_String_"></a> IsRecordedGuid\(string\)

この GUID が、記録済みの生成物の GUID かどうか。追跡される .mat / .unity が生成物を GUID で参照してよいのは、
その GUID が（追跡された）台帳に載っていて、別の clone の再生成でも同じ GUID が与えられる場合だけです。

```csharp
public static bool IsRecordedGuid(string guid)
```

#### 引数（Parameters）

`guid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_PinGuidIfKnown_System_String_"></a> PinGuidIfKnown\(string\)

出力先パスに記録済みの GUID があれば、生成前に <code>.meta</code> を書き込んで固定します。
既に <code>.meta</code> が存在する場合（既存アセットの上書き更新時）は何もしません。
生成本体（.mat / .shader ファイル自体）を書き込む<b>前</b>に呼ぶこと。

```csharp
public static void PinGuidIfKnown(string dstPath)
```

#### 引数（Parameters）

`dstPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_OmniGuidManifest_RecordGuid_System_String_UnityEngine_Object_"></a> RecordGuid\(string, Object\)

生成完了後、実際に割り当てられた GUID を記録します（新規・既存どちらでも呼んでよい。
既存アセットの上書き更新時に呼べば、まだマニフェストに無い過去の生成物を
自然に取り込んでいけます）。<xref href="Omni.Converter.OmniGuidManifest.SaveIfDirty(Omni.Converter.OmniGuidManifest.SaveIntent)" data-throw-if-not-resolved="false"></xref> を呼ぶまでは
メモリ上に保持されるだけです。

```csharp
public static void RecordGuid(string dstPath, Object asset)
```

#### 引数（Parameters）

`dstPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`asset` Object

### <a id="Omni_Converter_OmniGuidManifest_RecordGuid_System_String_UnityEngine_Object_UnityEngine_Object_"></a> RecordGuid\(string, Object, Object\)

生成物の GUID に加えて、<b>元アセットへの逆引き</b>も記録します。

<p>
<code class="paramref">source</code> を渡せる呼び出し（マテリアル変換など）は必ずこちらを使ってください。
これが入っていないと Revert が生成物パスからの推測に頼ることになり、
<code>Assets/Radial/User/</code> 配下や埋め込みマテリアルを戻せません。
</p>

```csharp
public static void RecordGuid(string dstPath, Object asset, Object source)
```

#### 引数（Parameters）

`dstPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`asset` Object

`source` Object

### <a id="Omni_Converter_OmniGuidManifest_RemoveEntriesForSourcePathPrefix_System_String_"></a> RemoveEntriesForSourcePathPrefix\(string\)

別の生成系が所有する元asset prefixに対応した製品manifest entryを除去します。
返した生成物pathの削除可否は、所有者側が参照を確認して判断します。

```csharp
public static IReadOnlyList<string> RemoveEntriesForSourcePathPrefix(string sourcePathPrefix)
```

#### 引数（Parameters）

`sourcePathPrefix` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

### <a id="Omni_Converter_OmniGuidManifest_RemoveEntry_System_String_"></a> RemoveEntry\(string\)

生成物のエントリを取り除きます。元が消えた生成物を削除した後だけに使います
（元が残っている生成物のエントリを消すと、再生成でGUIDが変わりScene参照が壊れます）。

```csharp
public static bool RemoveEntry(string generatedPath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_RenameEntry_System_String_System_String_"></a> RenameEntry\(string, string\)

生成物が別のパスへ移ったとき、記録（GUID と元アセットへの逆引き）を新しいパスへ付け替えます。
新しいパスに別の記録が既にあるときは、何もせず false を返します（GUID を取り違えないため）。

```csharp
public static bool RenameEntry(string oldPath, string newPath)
```

#### 引数（Parameters）

`oldPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`newPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_ResolveSource_System_String_"></a> ResolveSource\(string\)

生成物パスから元アセットを解決します。<b>Revert の正規経路</b>です。

<p>
解決順は「GUID + localId」→「GUID + 名前」の 2 段で、フォールスルーしません。
どちらも駄目なら null を返します（呼び出し側が理由を報告できるように、
黙って別のものを返すことはしません）。
</p>

```csharp
public static Object ResolveSource(string generatedPath)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 Object

### <a id="Omni_Converter_OmniGuidManifest_SaveIfDirty_Omni_Converter_OmniGuidManifest_SaveIntent_"></a> SaveIfDirty\(SaveIntent\)

変更があれば正規manifestへ保存します。BestEffortの失敗はdirtyを保持して
Deferredを返し、Requiredの失敗は呼出し元がトランザクションを失敗させるため
Failedを返します。例外はこの境界から外へ送出しません。

```csharp
public static OmniGuidManifest.SaveResult SaveIfDirty(OmniGuidManifest.SaveIntent intent)
```

#### 引数（Parameters）

`intent` [OmniGuidManifest](Omni.Converter.OmniGuidManifest.md).[SaveIntent](Omni.Converter.OmniGuidManifest.SaveIntent.md)

#### 戻り値（Returns）

 [OmniGuidManifest](Omni.Converter.OmniGuidManifest.md).[SaveResult](Omni.Converter.OmniGuidManifest.SaveResult.md)

### <a id="Omni_Converter_OmniGuidManifest_SetSourceInfo_System_String_UnityEngine_Object_"></a> SetSourceInfo\(string, Object\)

逆引き情報だけを後から書き込みます（バックフィル用）。

```csharp
public static bool SetSourceInfo(string generatedPath, Object source)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`source` Object

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_TryGetGeneratedPathForSource_UnityEngine_Object_System_String__"></a> TryGetGeneratedPathForSource\(Object, out string\)

元Assetのidentityに対応する記録済み生成pathを返します。

```csharp
public static bool TryGetGeneratedPathForSource(Object source, out string generatedPath)
```

#### 引数（Parameters）

`source` Object

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_TryGetSourceGuid_System_String_System_String__"></a> TryGetSourceGuid\(string, out string\)

記録済みの元アセットGUIDを返します。<xref href="Omni.Converter.OmniGuidManifest.ResolveSource(System.String)" data-throw-if-not-resolved="false"></xref> と違い、元が消えていても
GUIDを返すので、「元が消えた」と「逆引きが未記録」を区別できます。

```csharp
public static bool TryGetSourceGuid(string generatedPath, out string sourceGuid)
```

#### 引数（Parameters）

`generatedPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

`sourceGuid` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_OmniGuidManifest_TryPrepareGeneratedPathForSource_System_String_UnityEngine_Object_System_Boolean__System_String__"></a> TryPrepareGeneratedPathForSource\(string, Object, out bool, out string\)

元AssetのGUIDとlocal idから既存生成物を検索し、現在の正規出力先へ移行します。
元Assetの移動・rename後も生成物GUIDを維持するため、生成ファイルを書き込む前に呼びます。

```csharp
public static bool TryPrepareGeneratedPathForSource(string destinationPath, Object source, out bool migrated, out string error)
```

#### 引数（Parameters）

`destinationPath` [string](https://learn.microsoft.com/dotnet/api/system.string)

現在の出力規則で求めた生成先pathです。

`source` Object

移動に追従する元Assetです。

`migrated` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Assetまたはmanifestのpathを変更した場合はtrueです。

`error` [string](https://learn.microsoft.com/dotnet/api/system.string)

GUID衝突などで安全に移行できない場合の理由です。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

生成処理を続行してよい場合はtrueです。
