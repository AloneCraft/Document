# <a id="Omni_Editor_Manager_OmniCameraScanner"></a> Class OmniCameraScanner

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

シーン内カメラのスキャンと診断を行うクラスです。

```csharp
public static class OmniCameraScanner
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[OmniCameraScanner](Omni.Editor.Manager.OmniCameraScanner.md)

## メソッド（Methods）

### <a id="Omni_Editor_Manager_OmniCameraScanner_AddRadialCameraComponents_System_Collections_Generic_IEnumerable_UnityEngine_Camera__"></a> AddRadialCameraComponents\(IEnumerable<Camera\>\)

指定カメラへ <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を追加します（Undo 対応）。
既に付いている場合は何もしません。

<p>
付けたComponentは <xref href="UnityEngine.HideFlags.DontSaveInEditor" data-throw-if-not-resolved="false"></xref> にします。切替が足した分をSceneファイルへ書かず、
標準へ戻す／対数モードの記録が標準になったときに <code>OmniRenderingModeAutoApply</code> が外すためです
（自動付与と同じ扱い）。保存すると、標準へ戻した後も無効なRadialCameraがgitの差分として残ります。
</p>

```csharp
public static void AddRadialCameraComponents(IEnumerable<Camera> cameras)
```

#### 引数（Parameters）

`cameras` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Camera\>

### <a id="Omni_Editor_Manager_OmniCameraScanner_CountAllCameras"></a> CountAllCameras\(\)

シーン内の Camera コンポーネントの総数を返します。

```csharp
public static int CountAllCameras()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_OmniCameraScanner_CountOmniCameras"></a> CountOmniCameras\(\)

シーン内の RadiaCamera コンポーネントの総数を返します。

```csharp
public static int CountOmniCameras()
```

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_OmniCameraScanner_DisableRadialCameraComponents_System_Collections_Generic_IEnumerable_Omni_RadialCamera__"></a> DisableRadialCameraComponents\(IEnumerable<RadialCamera\>\)

指定 <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 群を無効化します（Undo 対応）。

<p>
無効化と同時に、そのカメラの <xref href="UnityEngine.Camera.cullingMatrix" data-throw-if-not-resolved="false"></xref> /
<xref href="UnityEngine.Camera.projectionMatrix" data-throw-if-not-resolved="false"></xref> の上書き（非シリアライズのネイティブ実行時
プロパティ）も同期的に復元します。これらは Radial 描画中に上書きされたカメラが
再描画されて初めて元に戻る仕組みのため、無効化した後そのカメラが一度も描画されずに
終わると上書きが永久に残り、以後そのカメラが何も描画しなくなる不具合があったためです。
</p>

```csharp
public static void DisableRadialCameraComponents(IEnumerable<RadialCamera> components)
```

#### 引数（Parameters）

`components` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<RadialCamera\>

### <a id="Omni_Editor_Manager_OmniCameraScanner_EnableRadialCameraComponents_System_Collections_Generic_IEnumerable_Omni_RadialCamera__"></a> EnableRadialCameraComponents\(IEnumerable<RadialCamera\>\)

指定 <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> 群を有効化します（Undo 対応）。

```csharp
public static void EnableRadialCameraComponents(IEnumerable<RadialCamera> components)
```

#### 引数（Parameters）

`components` [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<RadialCamera\>

### <a id="Omni_Editor_Manager_OmniCameraScanner_EnsureRadialCameras_UnityEngine_SceneManagement_Scene_System_Action_Omni_RadialCamera_System_Boolean__"></a> EnsureRadialCameras\(Scene, Action<RadialCamera, bool\>\)

1つのSceneの切替対象カメラへ <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を付けて有効にします
（<xref href="Omni.Editor.Manager.OmniRenderingModeSettings" data-throw-if-not-resolved="false"></xref> の対数モード用）。Undoへ記録せず、Sceneを
未保存（dirty）にもしません。PlayとBuildの処理中に呼ばれるためと、開くたびに保存を
求めないためです。

```csharp
public static int EnsureRadialCameras(Scene scene, Action<RadialCamera, bool> onChanged = null)
```

#### 引数（Parameters）

`scene` Scene

`onChanged` [Action](https://learn.microsoft.com/dotnet/api/system.action\-2)<RadialCamera, [bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>

付けた・有効にしたRadialCameraごとに呼びます（第2引数は新規に付けたか）。

#### 戻り値（Returns）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

追加または有効化したカメラの数です。

### <a id="Omni_Editor_Manager_OmniCameraScanner_EnumerateCameras"></a> EnumerateCameras\(\)

ロード済み全シーンのカメラを列挙します。非アクティブな GameObject も含み、
Prefab Stage を開いている間はそのシーンを除外します。

```csharp
public static IEnumerable<Camera> EnumerateCameras()
```

#### 戻り値（Returns）

 [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable\-1)<Camera\>

### <a id="Omni_Editor_Manager_OmniCameraScanner_IsRadialSwitchTarget_UnityEngine_Camera_"></a> IsRadialSwitchTarget\(Camera\)

統合スイッチが <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を追加・有効化・無効化してよいカメラかを返します。

<p>
保存されない隠しカメラ（Scene View の隠しアンカー等。<code>WarpCameraSelection</code> と同じ規則）と、
観察Rigの枠カメラは対象外です。観察カメラに <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> を付けると、描画カメラ自身が
ワープ中心（Owner）になり、メインカメラの変形後の世界を観察できなくなります。
</p>

```csharp
public static bool IsRadialSwitchTarget(Camera camera)
```

#### 引数（Parameters）

`camera` Camera

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_OmniCameraScanner_IsSceneMaterialsRadial_UnityEngine_SceneManagement_Scene_"></a> IsSceneMaterialsRadial\(Scene\)

このSceneのMaterialが対数（Radial）になっているかを返します。対数レンダリングの記録がある間の
RadialCameraの自動付与は、この判定がtrueのSceneだけに行います。標準のMaterialのSceneへ
RadialCameraを付けると、LogicalTransform配下の標準Materialが安全側で非表示になり、
Sceneを標準では見られなくなるためです。

<p>
対数のMaterial（適用済み・対数契約を直接実装・変換エラーの診断表示）が1つ以上あり、
対数へ変換できるのに標準のままのMaterialが無いときだけtrueです。
</p>

```csharp
public static bool IsSceneMaterialsRadial(Scene scene)
```

#### 引数（Parameters）

`scene` Scene

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
