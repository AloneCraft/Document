# <a id="Omni_Editor_RadialCameraEditor"></a> Class RadialCameraEditor

Namespace: [Omni.Editor](Omni.Editor.md)  
Assembly: Omni.Editor.dll  

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> のインスペクタです。

<p>
写像は Smooth Log ひとつだけで（<code>d' = S·log2(1 + d·M/S)</code>、S = <xref href="Omni.RadialSettings.RadialScale" data-throw-if-not-resolved="false"></xref> = 1）、
曲線・S・線形半径の設定はありません。編集できるのは論理 Near／Far だけで、View Scale M は
<code>Camera の Near ÷ 論理 Near</code> で決まります。式の根拠は <code>Assets/Omni/Core/Runtime/Sharders/RadialWarp.hlsl</code> と
<xref href="Omni.RadialSettings" data-throw-if-not-resolved="false"></xref> の距離写像APIです。写像を変更したら HelpBox の文言も合わせて直してください。
</p>

```csharp
[CustomEditor(typeof(RadialCamera))]
[CanEditMultipleObjects]
public sealed class RadialCameraEditor : Editor
```

#### 継承（Inheritance）

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
Object ← 
ScriptableObject ← 
Editor ← 
[RadialCameraEditor](Omni.Editor.RadialCameraEditor.md)

## メソッド（Methods）

### <a id="Omni_Editor_RadialCameraEditor_OnInspectorGUI"></a> OnInspectorGUI\(\)

<p>Implement this function to make a custom inspector.</p>

```csharp
public override void OnInspectorGUI()
```
