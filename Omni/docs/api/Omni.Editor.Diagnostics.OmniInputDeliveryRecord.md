# <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord"></a> Struct OmniInputDeliveryRecord

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

入力到達ログの 1 件です。JsonUtility で書けるよう、種類は名前の文字列で持ちます。

```csharp
[Serializable]
public struct OmniInputDeliveryRecord
```

## フィールド（Fields）

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_alreadyUsed"></a> alreadyUsed

IMGUI で type が Used で、rawType は元の種類のままでした。Unity 6000.6.4f1 の Event.Use() は rawType も
Used に変え、その場合は記録しないので、通常は false です。

```csharp
public bool alreadyUsed
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_button"></a> button

マウスのボタンです（キーでは -1、ホイールでは -1）。

```csharp
public int button
```

#### 値（Field Value）

 [int](https://learn.microsoft.com/dotnet/api/system.int32)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_editorTime"></a> editorTime

EditorApplication.timeSinceStartup です。

```csharp
public double editorTime
```

#### 値（Field Value）

 [double](https://learn.microsoft.com/dotnet/api/system.double)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_element"></a> element

UI Toolkit では "型名#name"、IMGUI では "SceneView(IMGUI)" です。

```csharp
public string element
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_keyCode"></a> keyCode

KeyCode の名前です（マウスでは "None"）。

```csharp
public string keyCode
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_kind"></a> kind

"Down"、"Up"、"Drag"、"Click"、"Wheel"、"KeyDown"、"KeyUp" のどれかです。

```csharp
public string kind
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_localX"></a> localX

UI Toolkit ではパネル座標、IMGUI では GUI 座標です（point）。

```csharp
public float localX
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_localY"></a> localY

UI Toolkit ではパネル座標、IMGUI では GUI 座標です（point）。

```csharp
public float localY
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_matchedFilter"></a> matchedFilter

記録した時点の filter に、帰属したウィンドウが一致しました（filter 省略時は常に true）。

```csharp
public bool matchedFilter
```

#### 値（Field Value）

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_modifiers"></a> modifiers

修飾キーの名前です。

```csharp
public string modifiers
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_pixelsPerPoint"></a> pixelsPerPoint

```csharp
public float pixelsPerPoint
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_screenX"></a> screenX

画面座標の近似です（point）。診断用で、判定には使いません。

```csharp
public float screenX
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_screenY"></a> screenY

画面座標の近似です（point）。診断用で、判定には使いません。

```csharp
public float screenY
```

#### 値（Field Value）

 [float](https://learn.microsoft.com/dotnet/api/system.single)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_sequence"></a> sequence

セッション内の通し番号です（1 から）。

```csharp
public long sequence
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_source"></a> source

"UIToolkit" か "SceneViewImgui" です。

```csharp
public string source
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_utcTicks"></a> utcTicks

<xref href="System.DateTime.UtcNow" data-throw-if-not-resolved="false"></xref> の Ticks です。外部ランナーが入力の直前に取った時刻と比べます。

```csharp
public long utcTicks
```

#### 値（Field Value）

 [long](https://learn.microsoft.com/dotnet/api/system.int64)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_windowTitle"></a> windowTitle

入力を受けた EditorWindow の題です。

```csharp
public string windowTitle
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Omni_Editor_Diagnostics_OmniInputDeliveryRecord_windowType"></a> windowType

入力を受けた EditorWindow の型名です。帰属できなければ "&lt;unknown&gt;" です。

```csharp
public string windowType
```

#### 値（Field Value）

 [string](https://learn.microsoft.com/dotnet/api/system.string)
