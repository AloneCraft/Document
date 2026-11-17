# <a id="Omni_Editor_Build_OmniDotsRadialGuard"></a> Class OmniDotsRadialGuard

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Omni 0.1 はDOTS／Entities Graphicsの描画を対数（Radial）レンダリングの対象にしません。
対数切替とPlayer Buildの前に、DOTSコンテンツを検出したら理由を示して停止します。

```csharp
public static class OmniDotsRadialGuard
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniDotsRadialGuard](Omni.Editor.Build.OmniDotsRadialGuard.md)

## 補足（Remarks）

製品のEditor assemblyはEntitiesへ依存しません。Entitiesパッケージがある環境だけで
コンパイルされる検出器が<xref href="Omni.Editor.Build.OmniDotsRadialGuard.Register(Omni.Editor.Build.OmniDotsRadialGuard.IDetector)" data-throw-if-not-resolved="false"></xref>で登録し、無い環境では常に通過します。
開発環境（配布しない<code>Assets/Omni/Development</code>のEditorコード）は<xref href="Omni.Editor.Build.OmniDotsRadialGuard.RegisterDevelopmentAllowance" data-throw-if-not-resolved="false"></xref>で
許可を登録でき、許可がある間は拒否の代わりに警告を返して切替とPlayer Buildを通します
（Docs/Plans/DotsRadialDevelopmentSwitch.md）。配布パッケージの利用者の環境には許可がありません。

## プロパティ（Properties）

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_DevelopmentAllowed"></a> DevelopmentAllowed

開発環境の許可が登録されているかを返します。

```csharp
public static bool DevelopmentAllowed { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

## メソッド（Methods）

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_DescribeDevelopmentWarnings_System_Boolean_"></a> DescribeDevelopmentWarnings\(bool\)

許可がある開発環境で、読み込み中のDOTSコンテンツについて未対応の点を返します。
DOTSコンテンツが無い、または許可が無い場合は空文字です。OnGUIから呼べるよう2秒だけ結果を使い回します。

```csharp
public static string DescribeDevelopmentWarnings(bool refresh = false)
```

#### 引数（Parameters）

`refresh` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

#### 戻り値（Returns）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_NotifyMaterialsSwitched"></a> NotifyMaterialsSwitched\(\)

切替でMaterialのShaderが変わった後に、所有者へ描画の作り直しを通知します。

```csharp
public static void NotifyMaterialsSwitched()
```

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_Register_Omni_Editor_Build_OmniDotsRadialGuard_IDetector_"></a> Register\(IDetector\)

検出器を登録し、解除用のハンドルを返します。

```csharp
public static IDisposable Register(OmniDotsRadialGuard.IDetector detector)
```

#### 引数（Parameters）

`detector` [OmniDotsRadialGuard](Omni.Editor.Build.OmniDotsRadialGuard.md).[IDetector](Omni.Editor.Build.OmniDotsRadialGuard.IDetector.md)

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_RegisterDevelopmentAllowance"></a> RegisterDevelopmentAllowance\(\)

開発環境でDOTSの切替を許可します。許可がある間は拒否の代わりに警告を返します。
配布しないEditorコードからだけ登録します。

```csharp
public static IDisposable RegisterDevelopmentAllowance()
```

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_RegisterMaterialOwner_Omni_Editor_Build_OmniDotsRadialGuard_IMaterialOwner_"></a> RegisterMaterialOwner\(IMaterialOwner\)

Entityを作る所有者を登録します。許可がある間だけMaterialが切替の対象になります。

```csharp
public static IDisposable RegisterMaterialOwner(OmniDotsRadialGuard.IMaterialOwner owner)
```

#### 引数（Parameters）

`owner` [OmniDotsRadialGuard](Omni.Editor.Build.OmniDotsRadialGuard.md).[IMaterialOwner](Omni.Editor.Build.OmniDotsRadialGuard.IMaterialOwner.md)

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_SuspendDevelopmentAllowanceForTests"></a> SuspendDevelopmentAllowanceForTests\(\)

テストで、開発環境の許可を一時的に無効にします（利用者の環境と同じ拒否の挙動を検証するため）。
解除用のハンドルを返します。

```csharp
public static IDisposable SuspendDevelopmentAllowanceForTests()
```

#### 戻り値（Returns）

 [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_TryValidateBuildScenes_System_Collections_Generic_IReadOnlyList_System_String__System_String__"></a> TryValidateBuildScenes\(IReadOnlyList<string\>, out string\)

Build対象Sceneに、対数レンダリングを使うRadialCameraとSubSceneが同時にあれば拒否します。
実行時にコードで作るEntityは静的に検出できないため、この検査の対象外です。

```csharp
public static bool TryValidateBuildScenes(IReadOnlyList<string> scenePaths, out string reason)
```

#### 引数（Parameters）

`scenePaths` [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist\-1)<[string](https://learn.microsoft.com/dotnet/api/system.string)\>

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Build_OmniDotsRadialGuard_TryValidateLoadedScenesForRadial_System_String__"></a> TryValidateLoadedScenesForRadial\(out string\)

ロード済みSceneを対数へ切り替えてよいかを検証します。SubSceneまたは
Entities Graphicsの描画Entityがあれば、理由を返して拒否します。

```csharp
public static bool TryValidateLoadedScenesForRadial(out string reason)
```

#### 引数（Parameters）

`reason` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
