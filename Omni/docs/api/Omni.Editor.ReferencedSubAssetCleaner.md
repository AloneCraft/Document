# <a id="Omni_Editor_ReferencedSubAssetCleaner"></a> Class ReferencedSubAssetCleaner

Namespace: [Omni.Editor](Omni.Editor.md)  
Assembly: Omni.Editor.dll  

生成済みmain assetから到達できない、同一ファイル内の古いサブアセットを除去します。

```csharp
public static class ReferencedSubAssetCleaner
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ReferencedSubAssetCleaner](Omni.Editor.ReferencedSubAssetCleaner.md)

## メソッド（Methods）

### <a id="Omni_Editor_ReferencedSubAssetCleaner_RemoveUnreferencedSubAssets_UnityEngine_Object_"></a> RemoveUnreferencedSubAssets\(Object\)

main assetのSerializedObject参照を辿り、参照されていないサブアセットを除去します。

```csharp
public static int RemoveUnreferencedSubAssets(Object mainAsset)
```

#### 引数（Parameters）

`mainAsset` Object

整理するassetファイルのmain assetです。nullは許可しません。

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

除去したサブアセット数です。保存は呼び出し側が行います。
