# <a id="Omni_NativeDraw_Generation_GrassEnvironmentSelection"></a> Class GrassEnvironmentSelection

Namespace: [Omni.NativeDraw.Generation](Omni.NativeDraw.Generation.md)  
Assembly: Omni.Manager.dll  

```csharp
public static class GrassEnvironmentSelection
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md)

## メソッド（Methods）

### <a id="Omni_NativeDraw_Generation_GrassEnvironmentSelection_RequireFullEditorVersion_Omni_NativeDraw_Generation_GrassEnvironmentSelection_Profile_System_String_"></a> RequireFullEditorVersion\(Profile, string\)

Editor 実体の完全版が、検証済みプロファイルの revision と一致することを確認する。

```csharp
public static void RequireFullEditorVersion(GrassEnvironmentSelection.Profile profile, string fullEditorVersion)
```

#### 引数（Parameters）

`profile` [GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md).[Profile](Omni.NativeDraw.Generation.GrassEnvironmentSelection.Profile.md)

`fullEditorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_NativeDraw_Generation_GrassEnvironmentSelection_Select_System_Collections_Generic_IEnumerable_Omni_NativeDraw_Generation_GrassEnvironmentSelection_Profile__System_String_System_String_System_String_"></a> Select\(IEnumerable<Profile\>, string, string, string\)

```csharp
public static GrassEnvironmentSelection.Profile Select(IEnumerable<GrassEnvironmentSelection.Profile> profiles, string editorVersion, string urpVersion, string urpContentSha256)
```

#### 引数（Parameters）

`profiles` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md).[Profile](Omni.NativeDraw.Generation.GrassEnvironmentSelection.Profile.md)\>

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`urpVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`urpContentSha256` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md).[Profile](Omni.NativeDraw.Generation.GrassEnvironmentSelection.Profile.md)

### <a id="Omni_NativeDraw_Generation_GrassEnvironmentSelection_SelectForEditor_System_Collections_Generic_IEnumerable_Omni_NativeDraw_Generation_GrassEnvironmentSelection_Profile__System_String_System_String_System_String_System_String_"></a> SelectForEditor\(IEnumerable<Profile\>, string, string, string, string\)

完全版を含む実 Editor 環境から、該当する認証済みプロファイルを一意に選択する。

```csharp
public static GrassEnvironmentSelection.Profile SelectForEditor(IEnumerable<GrassEnvironmentSelection.Profile> profiles, string editorVersion, string fullEditorVersion, string urpVersion, string urpContentSha256)
```

#### 引数（Parameters）

`profiles` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<[GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md).[Profile](Omni.NativeDraw.Generation.GrassEnvironmentSelection.Profile.md)\>

`editorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`fullEditorVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`urpVersion` [string](https://learn.microsoft.com/dotnet/api/system.string)

`urpContentSha256` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### 戻り値（Returns）

 [GrassEnvironmentSelection](Omni.NativeDraw.Generation.GrassEnvironmentSelection.md).[Profile](Omni.NativeDraw.Generation.GrassEnvironmentSelection.Profile.md)
