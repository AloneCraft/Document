# <a id="Omni_Editor_Manager_RadialRenderingSwitch_State"></a> Struct RadialRenderingSwitch.State

Namespace: [Omni.Editor.Manager](Omni.Editor.Manager.md)  
Assembly: Omni.Manager.dll  

ラジオボタンの表示状態です。

```csharp
public struct RadialRenderingSwitch.State
```

## フィールド（Fields）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_CamerasTotal"></a> CamerasTotal

```csharp
public int CamerasTotal
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_CamerasWithRadialDisabled"></a> CamerasWithRadialDisabled

```csharp
public int CamerasWithRadialDisabled
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_CamerasWithRadialEnabled"></a> CamerasWithRadialEnabled

```csharp
public int CamerasWithRadialEnabled
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_CamerasWithoutRadial"></a> CamerasWithoutRadial

```csharp
public int CamerasWithoutRadial
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_Materials"></a> Materials

```csharp
public RadialSceneState Materials
```

#### 値（Field Value）

 RadialSceneState

## プロパティ（Properties）

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_HasNoSwitchTargets"></a> HasNoSwitchTargets

切替対象が 1 つも無い（信用できる走査で、Camera も Material も VFX も数えられない）。標準へ戻す処理の
事後検証では「戻すものが無い＝すでに標準」として完了とみなします（Camera の無い Scene、または
変換の対象外の Material だけの Scene で、何も変えていないのに失敗しないため）。
ラジオの選択（<xref href="Omni.Editor.Manager.RadialRenderingSwitch.State.IsFullyUnity" data-throw-if-not-resolved="false"></xref>）は、空の Scene でどちらも選ばない仕様を保つため変えません。

```csharp
public bool HasNoSwitchTargets { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_IsFullyRadial"></a> IsFullyRadial

全カメラが有効な RadialCamera を持ち、マテリアルも完全に適用済み。走査結果が
信用できない（Playモード中のランタイムクローン差し替え等で、描画中のランタイム
インスタンスを検出した）ときは、判定を確定させません（下記 IsFullyUnity 参照）。

```csharp
public bool IsFullyRadial { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Manager_RadialRenderingSwitch_State_IsFullyUnity"></a> IsFullyUnity

マテリアルが1枚もRadial版を参照していない。カメラへの RadialCamera 付与・有効化の
有無は問わない。変換済みマテリアルが無ければ、RadialCamera が付いていてもワープする
シェーダー自体が使われないため描画結果には何も影響せず、実効的には Unity レンダリング
のままだからです。以前はカメラ条件も必須にしていたため、初めて開いたシーンで
「カメラには RadialCamera が付いているがマテリアルは1枚も変換していない」場合に
Unity/Radial のどちらも選択状態にならない詰みになっていました。

<p>
<code>Materials.Unreliable</code> が立っているときは false を返します。Playモード中は
<xref href="Omni.RadialGlobalRenderSystem" data-throw-if-not-resolved="false"></xref> がRadial変換済みマテリアルを
元Materialごとに共有するランタイムクローン（アセットではない）へ差し替えるため、
<xref href="Omni.Converter.RadialSceneMaterialState.Scan" data-throw-if-not-resolved="false"></xref> がそれらを「Unresolved」として数え、
<code>AppliedSlots</code> が実態に反して0まで落ちます。ここでガードしないと、
Radial変換済みのシーンでPlayを実行しただけで「Unityレンダリング」が誤って
選択状態になります（実際に発生した回帰）。
</p>

```csharp
public bool IsFullyUnity { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)
