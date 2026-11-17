# <a id="Omni_Editor"></a> Namespace Omni.Editor

### 名前空間（Namespaces）

 [Omni.Editor.BatchRendering](Omni.Editor.BatchRendering.md)

 [Omni.Editor.Build](Omni.Editor.Build.md)

 [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)

 [Omni.Editor.Manager](Omni.Editor.Manager.md)

 [Omni.Editor.Overlay](Omni.Editor.Overlay.md)

 [Omni.Editor.Performance](Omni.Editor.Performance.md)

 [Omni.Editor.SceneViewNavigation](Omni.Editor.SceneViewNavigation.md)

 [Omni.Editor.State](Omni.Editor.State.md)

### クラス（Classes）

 [RadialCameraEditor](Omni.Editor.RadialCameraEditor.md)

<xref href="Omni.RadialCamera" data-throw-if-not-resolved="false"></xref> のインスペクタです。

<p>
写像は Smooth Log ひとつだけで（<code>d' = S·log2(1 + d·M/S)</code>、S = <xref href="Omni.RadialSettings.RadialScale" data-throw-if-not-resolved="false"></xref> = 1）、
曲線・S・線形半径の設定はありません。編集できるのは論理 Near／Far だけで、View Scale M は
<code>Camera の Near ÷ 論理 Near</code> で決まります。式の根拠は <code>Assets/Omni/Core/Runtime/Sharders/RadialWarp.hlsl</code> と
<xref href="Omni.RadialSettings" data-throw-if-not-resolved="false"></xref> の距離写像APIです。写像を変更したら HelpBox の文言も合わせて直してください。
</p>

 [ReferencedSubAssetCleaner](Omni.Editor.ReferencedSubAssetCleaner.md)

生成済みmain assetから到達できない、同一ファイル内の古いサブアセットを除去します。
