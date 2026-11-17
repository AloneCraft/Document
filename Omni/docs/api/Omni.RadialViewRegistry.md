# <a id="Omni_RadialViewRegistry"></a> Class RadialViewRegistry

Namespace: [Omni](Omni.md)  
Assembly: Radial.Runtime.dll  

カメラ描画ごとの不変<xref href="Omni.Rendering.Radial.ViewSnapshot" data-throw-if-not-resolved="false"></xref>を、Unity 6000の
<xref href="UnityEngine.EntityId" data-throw-if-not-resolved="false"></xref> viewIDで管理するレジストリです。BRGのculling callbackは
<code>context.viewID.GetEntityId()</code>で得た値から本レジストリを読むため、
Shader.SetGlobal*をカメラ状態の正本にしません。SaturnシーンのMesoリングBRG描画で使用します。

```csharp
public static class RadialViewRegistry
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[RadialViewRegistry](Omni.RadialViewRegistry.md)

## メソッド（Methods）

### <a id="Omni_RadialViewRegistry_ClearAll"></a> ClearAll\(\)

全Snapshotを破棄します。Scene unload、domain reload、テスト後始末で使います。
revisionは単調性を保つためリセットしません。

```csharp
public static void ClearAll()
```

### <a id="Omni_RadialViewRegistry_PruneDestroyedCameras"></a> PruneDestroyedCameras\(\)

破棄済みカメラを弱参照から検出して除去します。メインスレッドのカメラ準備または
テストの後始末で呼びます。BRG worker callbackからは呼びません。

```csharp
public static int PruneDestroyedCameras()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

削除したSnapshot数です。

### <a id="Omni_RadialViewRegistry_Publish_UnityEngine_Camera_UnityEngine_EntityId_Omni_Rendering_Radial_ViewSnapshot__Omni_Rendering_Radial_ViewSnapshot__"></a> Publish\(Camera, EntityId, in ViewSnapshot, out ViewSnapshot\)

描画直前に生成したRadialビュー状態を公開します。

```csharp
public static bool Publish(Camera camera, EntityId viewId, in ViewSnapshot draft, out ViewSnapshot published)
```

#### 引数（Parameters）

`camera` Camera

状態を所有するカメラ。nullは受け付けません。

`viewId` EntityId

Camera componentのEntityId。BRG callbackのviewIDと同じ値を渡します。

`draft` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

revision未採番の不変Snapshot草案です。

`published` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

採番済みのSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

Camera ID、EntityId、草案の対応が一致して公開できた場合はtrueです。

### <a id="Omni_RadialViewRegistry_Remove_UnityEngine_EntityId_"></a> Remove\(EntityId\)

指定viewIDのSnapshotを破棄します。カメラ破棄通知を持つ所有者が使う補助入口です。

```csharp
public static void Remove(EntityId viewId)
```

#### 引数（Parameters）

`viewId` EntityId

破棄対象のEntityId。Noneなら何もしません。

### <a id="Omni_RadialViewRegistry_TryGet_UnityEngine_EntityId_System_UInt64_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGet\(EntityId, ulong, out ViewSnapshot\)

Unity 6000のviewIDと明示的なrevisionに一致するSnapshotを取得します。

```csharp
public static bool TryGet(EntityId viewId, ulong frameRevision, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`viewId` EntityId

BRG callbackの<xref href="UnityEngine.EntityId" data-throw-if-not-resolved="false"></xref>です。Noneは無効です。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

公開時に返されたrevisionです。0は無効です。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

一致時のSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

viewIDとrevisionが完全一致した場合はtrueです。

### <a id="Omni_RadialViewRegistry_TryGet_System_UInt64_System_UInt64_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGet\(ulong, ulong, out ViewSnapshot\)

正規化済みview keyと明示的なrevisionに一致するSnapshotを取得します。
Jobの事前入力検証で使用します。

```csharp
public static bool TryGet(ulong viewKey, ulong frameRevision, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`viewKey` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

EntityId.ToULongで正規化したview keyです。0は無効です。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

公開時に返されたrevisionです。0は無効です。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

一致時のSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

view keyとrevisionが完全一致した場合はtrueです。

### <a id="Omni_RadialViewRegistry_TryGetCamera_UnityEngine_EntityId_System_UInt64_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGetCamera\(EntityId, ulong, out ViewSnapshot\)

CameraのEntityIdと明示的なrevisionに一致するSnapshotを取得します。

```csharp
public static bool TryGetCamera(EntityId cameraInstanceId, ulong frameRevision, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`cameraInstanceId` EntityId

Camera.GetEntityId()の値です。Noneは無効です。

`frameRevision` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

公開時に返されたrevisionです。0は無効です。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

一致時のSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

カメラとrevisionが完全一致した場合はtrueです。

### <a id="Omni_RadialViewRegistry_TryGetCurrent_UnityEngine_EntityId_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGetCurrent\(EntityId, out ViewSnapshot\)

現在のUnityフレームに公開されたviewID用Snapshotを取得します。
BRG callbackの<code>context.viewID.GetEntityId()</code>から呼び、前フレームの
staleな状態ならfalseを返して描画側をfail-openにします。

```csharp
public static bool TryGetCurrent(EntityId viewId, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`viewId` EntityId

BRG callbackが渡すEntityId。Noneは無効です。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

現フレームのSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

現フレームのCamera Snapshotを安全に取得できた場合はtrueです。

### <a id="Omni_RadialViewRegistry_TryGetCurrent_System_UInt64_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGetCurrent\(ulong, out ViewSnapshot\)

現在のUnityフレームに公開された正規化view key用Snapshotを取得します。

```csharp
public static bool TryGetCurrent(ulong viewKey, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`viewKey` [ulong](https://learn.microsoft.com/dotnet/api/system.uint64)

EntityId.ToULongで正規化したview keyです。0は無効です。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

現フレームのSnapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

現フレームのSnapshotを安全に取得できた場合はtrueです。

### <a id="Omni_RadialViewRegistry_TryGetLatest_UnityEngine_EntityId_Omni_Rendering_Radial_ViewSnapshot__"></a> TryGetLatest\(EntityId, out ViewSnapshot\)

指定viewIDの最新Snapshotを取得します。診断用途専用であり、BRG callbackは
stale防止のため<xref href="Omni.RadialViewRegistry.TryGetCurrent(UnityEngine.EntityId%2cOmni.Rendering.Radial.ViewSnapshot%40)" data-throw-if-not-resolved="false"></xref>を使います。

```csharp
public static bool TryGetLatest(EntityId viewId, out ViewSnapshot snapshot)
```

#### 引数（Parameters）

`viewId` EntityId

参照したいCameraのEntityIdです。

`snapshot` [ViewSnapshot](Omni.Rendering.Radial.ViewSnapshot.md)

登録済みの最新Snapshot。失敗時はdefaultです。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

登録済みのSnapshotがある場合はtrueです。
