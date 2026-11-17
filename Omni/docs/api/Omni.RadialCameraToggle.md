# <a id="Omni_RadialCameraToggle"></a> Class RadialCameraToggle

Namespace: [Omni](Omni.md)  
Assembly: Omni.RadialCameraToggle.dll  

Play中に <xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> の有効／無効を切り替え、同じ視点で標準描画と対数描画を
見比べるためのコンポーネントです。RadialCameraを持つCameraへ付けて使います。

```csharp
[AddComponentMenu("Omni/Radial Camera Toggle")]
[DisallowMultipleComponent]
public sealed class RadialCameraToggle : MonoBehaviour
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
Component ← 
Behaviour ← 
MonoBehaviour ← 
[RadialCameraToggle](Omni.RadialCameraToggle.md)

## 補足（Remarks）

<p>
対数レンダリングへ切り替え済みのScene（Omni ManagerでRadial MaterialとRadialCameraを適用した
状態）を想定します。OFFではRadial Materialが恒等写像で描かれ、標準描画と同じ見た目になります。
Radial非対応のMaterialはRadialCameraが有効な間は安全側で非表示になるため、標準Materialのままの
Sceneでは先に対数レンダリングへ切り替えてください。
</p>
<p>
画面上のボタン（UI Toolkit）、キー（Input Systemがある場合、既定F8）、公開APIのどれからでも
切り替えられます。描画側は各Cameraの描画ごとに <code>RadialCamera.enabled</code> を読むため、
このコンポーネントはenabledを書き換えるだけです。Edit Modeではボタンを作らず、Sceneへ保存される
値はPlay終了でUnityが元へ戻します。
</p>

## プロパティ（Properties）

### <a id="Omni_RadialCameraToggle_RadialEnabled"></a> RadialEnabled

対象RadialCameraが有効（対数描画）ならtrueです。

```csharp
public bool RadialEnabled { get; }
```

#### 値（Property Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_RadialCameraToggle_Target"></a> Target

切り替え対象のRadialCameraです。見つからなければnullです。

```csharp
public RadialCamera Target { get; }
```

#### 値（Property Value）

 RadialCamera

## メソッド（Methods）

### <a id="Omni_RadialCameraToggle_SetRadialEnabled_System_Boolean_"></a> SetRadialEnabled\(bool\)

対数描画の有効／無効を設定します。

```csharp
public bool SetRadialEnabled(bool enabled)
```

#### 引数（Parameters）

`enabled` [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

trueで対数描画、falseで標準描画。

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

対象RadialCameraがあり、指定状態にできた場合true。

### <a id="Omni_RadialCameraToggle_Toggle"></a> Toggle\(\)

対数描画と標準描画を入れ替えます。

```csharp
public bool Toggle()
```

#### 戻り値（Returns）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

対象RadialCameraがあり、切り替えられた場合true。

### <a id="Omni_RadialCameraToggle_RadialEnabledChanged"></a> RadialEnabledChanged

対数描画の有効／無効が変わったときに、新しい状態で通知します。

```csharp
public event Action<bool> RadialEnabledChanged
```

#### 型（Event Type）

 [Action](https://learn.microsoft.com/dotnet/api/system.action\-1)<[bool](https://learn.microsoft.com/dotnet/api/system.boolean)\>
