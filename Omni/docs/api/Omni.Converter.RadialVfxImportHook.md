# <a id="Omni_Converter_RadialVfxImportHook"></a> Class RadialVfxImportHook

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

VFX Graph の取り込みで生成される表示用シェーダーへ、取り込みのたびに Radial のパッチ（<xref href="Omni.Converter.RadialVfxShaderPatcher" data-throw-if-not-resolved="false"></xref>）を当てます。

<p>
VFX Graph 17.6 は、ネイティブの取り込み処理から <code>VisualEffectResource.onCompileResource</code>（グラフを編集中は
<code>onEarlyGetAuthoringCompileData</code>）を呼び、グラフから生成したシェーダーのソースを <code>VisualEffectAssetDesc.shaderSourceDesc</code>
で直接返します。外部化したシェーダーのファイルを読み戻す仕組みは無く、以前の「外部化の設定を有効にして取り込み直す」方式では
パッチ済みのシェーダーが使われていませんでした（2026-10-04 に確認）。そこで、この2つのコールバックを包み、返るソースに
その場でパッチを当てます。生成物のファイルは作りません。
</p>
<p>
コールバックは internal なので、リフレクションと式木で包みます（C# のデリゲートを差し替えるだけで、ネイティブの関数は呼びません）。
見つからない版では <xref href="Omni.Converter.RadialVfxImportHook.Fault" data-throw-if-not-resolved="false"></xref> に理由を残し、<xref href="Omni.Converter.RadialVfxBackend" data-throw-if-not-resolved="false"></xref> が Faulted として報告します（Fail Closed）。
注入シェーダー（<xref href="Omni.Converter.RadialVfxImportHook.InjectDirectory" data-throw-if-not-resolved="false"></xref> の HLSL）と patcher の版から作る custom dependency を全ての VFX の取り込みに登録するので、
どちらかを変えると、全ての VFX が取り込み直されます。
</p>

```csharp
[InitializeOnLoad]
public static class RadialVfxImportHook
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialVfxImportHook](Omni.Converter.RadialVfxImportHook.md)

## フィールド（Fields）

### <a id="Omni_Converter_RadialVfxImportHook_DependencyName"></a> DependencyName

全ての VFX の取り込みが依存する custom dependency の名前。

```csharp
public const string DependencyName = "Omni/RadialVfxPatch"
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

## プロパティ（Properties）

### <a id="Omni_Converter_RadialVfxImportHook_DependencyHash"></a> DependencyHash

直近に登録した依存の hash。

```csharp
public static Hash128 DependencyHash { get; }
```

#### 値（Property Value）

 Hash128

### <a id="Omni_Converter_RadialVfxImportHook_Fault"></a> Fault

包めなかった理由（包めたら null）。

```csharp
public static string Fault { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxImportHook_InjectDirectory"></a> InjectDirectory

VFX の表示用シェーダーが include する注入シェーダーの置き場（この下の HLSL の内容が依存の hash に入ります）。

```csharp
public static string InjectDirectory { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxImportHook_IsAuthoringHookInstalled"></a> IsAuthoringHookInstalled

グラフ編集中の旧authoringコールバックを包めたか。

```csharp
public static bool IsAuthoringHookInstalled { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxImportHook_IsInstalled"></a> IsInstalled

この版のScene描画に必要なimportフックを包めたか。

```csharp
public static bool IsInstalled { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxImportHook_LastAssetPath"></a> LastAssetPath

```csharp
public static string LastAssetPath { get; }
```

#### 値（Property Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Converter_RadialVfxImportHook_PatchCalls"></a> PatchCalls

このドメインで包んだコールバックが呼ばれた回数と、パッチを当てたソースの数（診断用）。

```csharp
public static int PatchCalls { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Converter_RadialVfxImportHook_PatchedSources"></a> PatchedSources

```csharp
public static int PatchedSources { get; }
```

#### 値（Property Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

## メソッド（Methods）

### <a id="Omni_Converter_RadialVfxImportHook_IsUnsupportedVersionFault_System_Exception_"></a> IsUnsupportedVersionFault\(Exception\)

取り込みのフックに使う内部のメンバー（<xref href="System.MissingMemberException" data-throw-if-not-resolved="false"></xref>）や型（<xref href="System.TypeLoadException" data-throw-if-not-resolved="false"></xref>）が
この Unity／VFX Graph の版に無い、という「未対応の版」の失敗か。それ以外の想定外の失敗は false（エラーとして出す）。

```csharp
public static bool IsUnsupportedVersionFault(Exception exception)
```

#### 引数（Parameters）

`exception` [Exception](https://learn.microsoft.com/dotnet/api/system.exception)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Converter_RadialVfxImportHook_RefreshDependency"></a> RefreshDependency\(\)

注入シェーダーと patcher の版から依存の hash を作り直し、変わっていれば登録します（変わると VFX が取り込み直されます）。

```csharp
public static bool RefreshDependency()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
