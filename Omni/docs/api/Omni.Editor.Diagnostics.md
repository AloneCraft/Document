# <a id="Omni_Editor_Diagnostics"></a> Namespace Omni.Editor.Diagnostics

### クラス（Classes）

 [GalaxyAcceptanceEditorSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceEditorSnapshot.md)

受入前に記録するEditor状態のシリアライズ可能なスナップショットです。
Scene/Selection/SceneView以外の設定も同じ復元単位へ含め、失敗時にGalaxyを
強制的に開き直すことを禁止します。

 [GalaxyAcceptanceSceneSetupSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceSceneSetupSnapshot.md)

Acceptance 前の加算 Scene setup と dirty 境界です。

 [GalaxyAcceptanceSceneViewSnapshot](Omni.Editor.Diagnostics.GalaxyAcceptanceSceneViewSnapshot.md)

一つの Scene View に属する復元可能な表示・Logical 状態です。

 [GalaxyAcceptanceStateContract](Omni.Editor.Diagnostics.GalaxyAcceptanceStateContract.md)

受入ランナーとEditorコマンドが共有する純粋な契約判定です。

 [InteractionStageBoundaryLayers](Omni.Editor.Diagnostics.InteractionStageBoundaryLayers.md)

S03の合成対象を一つずつ分離描画するためのEditor専用Layer契約です。
Scene Builderと実GPU検証が同じ番号を正本として共有します。

 [OmniInputDeliveryReadResult](Omni.Editor.Diagnostics.OmniInputDeliveryReadResult.md)

<code>pointer-log-read</code> の応答本文（2 行目以降）の JSON です。

 [OmniInputDeliveryRecorder](Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.md)

実入力が Unity に届いたかを、読み取り専用で記録します。開いている EditorWindow のパネルの visualTree に
TrickleDown で、Scene View には <xref href="UnityEditor.SceneView.beforeSceneGui" data-throw-if-not-resolved="false"></xref> で登録します。イベントを消費も変更もせず
（Use、StopPropagation、PreventDefault、フォーカスや hotControl の変更をしません）、購読は
<xref href="Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.Start(System.String)" data-throw-if-not-resolved="false"></xref> から <xref href="Omni.Editor.Diagnostics.OmniInputDeliveryRecorder.Stop(System.String%2cSystem.String%40)" data-throw-if-not-resolved="false"></xref> までだけです。非アクティブな間にコストはありません。

 [OmniInputDeliveryStartResult](Omni.Editor.Diagnostics.OmniInputDeliveryStartResult.md)

<code>pointer-log-start</code> の応答本文（2 行目以降）の JSON です。

 [OmniObservationEnvironmentReader](Omni.Editor.Diagnostics.OmniObservationEnvironmentReader.md)

実 Editor から <xref href="Omni.Editor.Diagnostics.OmniObservationEnvironment" data-throw-if-not-resolved="false"></xref> を読む薄いアダプターです。
呼ばれた時点の値を読むだけで、購読・毎フレーム処理・Repaint の要求はしません。

 [OmniObservationPreconditions](Omni.Editor.Diagnostics.OmniObservationPreconditions.md)

観測の前提を判定する純粋関数です。入力は値だけで、静的な状態や Editor の API を読みません。
前提が 1 つでも崩れた観測は、計測が合格でも不合格でも <xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Unavailable" data-throw-if-not-resolved="false"></xref> です。

 [OmniObservationReport](Omni.Editor.Diagnostics.OmniObservationReport.md)

JsonUtility で保存できる観測の報告です。enum は読みやすさのため名前の文字列で持ちます。

 [OmniOverlayBrgRegression](Omni.Editor.Diagnostics.OmniOverlayBrgRegression.md)

LogicalOriginalTransformの実Scene ViewでBRGの標準描画と座標保持を検証します。
実オーバーレイイベントとGPU描画を通し、終了時には元の視点・表示状態へ戻します。

 [OmniSceneNoiseProbe](Omni.Editor.Diagnostics.OmniSceneNoiseProbe.md)

現在の比較Sceneを保存せず、指定した列だけのGPU出力を取得します。

 [OmniSceneViewCapture](Omni.Editor.Diagnostics.OmniSceneViewCapture.md)

対象Scene Viewカメラの実GPUカラー出力をPNGへ保存する診断用キャプチャです。
OS画面座標は使用しないため、別ウィンドウが前面でも誤った画像を成功扱いしません。

 [OmniSceneViewVerification](Omni.Editor.Diagnostics.OmniSceneViewVerification.md)

<b>実際のScene Viewを駆動して</b>ナビゲーションの不変条件を検証します。

 [OmniSmallScaleLiveProbe](Omni.Editor.Diagnostics.OmniSmallScaleLiveProbe.md)

専用の追加SceneとViewで、実OS入力後の表示・視点を記録する調査用入口です。

### 構造体（Structs）

 [OmniImageEvidence](Omni.Editor.Diagnostics.OmniImageEvidence.md)

画像から数えた、比較の対象と背景の画素数です。

 [OmniInputDeliveryEvidence](Omni.Editor.Diagnostics.OmniInputDeliveryEvidence.md)

入力到達ログを、入力の前後で読んだ値です。

 [OmniInputDeliveryRecord](Omni.Editor.Diagnostics.OmniInputDeliveryRecord.md)

入力到達ログの 1 件です。JsonUtility で書けるよう、種類は名前の文字列で持ちます。

 [OmniInputDeliveryRect](Omni.Editor.Diagnostics.OmniInputDeliveryRect.md)

画面上の矩形です（物理ピクセル）。

 [OmniInputDeliveryWindowRect](Omni.Editor.Diagnostics.OmniInputDeliveryWindowRect.md)

購読したウィンドウと、その画面上の矩形です（物理ピクセル）。

 [OmniObservationEnvironment](Omni.Editor.Diagnostics.OmniObservationEnvironment.md)

前提の判定に使う Editor 環境の値です。実 Editor からは
<xref href="Omni.Editor.Diagnostics.OmniObservationEnvironmentReader" data-throw-if-not-resolved="false"></xref> が読み、テストは偽の値を直接作ります。

 [OmniObservationRequirements](Omni.Editor.Diagnostics.OmniObservationRequirements.md)

観測を始める前に満たすべき前提です。

 [OmniObservationWindowRequirements](Omni.Editor.Diagnostics.OmniObservationWindowRequirements.md)

観測窓の間に満たすべき前提です。

 [OmniObservationWindowSample](Omni.Editor.Diagnostics.OmniObservationWindowSample.md)

観測窓の開始と終了で読む値です。

 [OmniScreenOccluder](Omni.Editor.Diagnostics.OmniScreenOccluder.md)

画面や画像の上で観測を遮り得るもの（浮いたウィンドウなど）の名前と矩形です。

 [OmniTestNode](Omni.Editor.Diagnostics.OmniTestNode.md)

テスト結果の木の 1 節点です（名前空間・fixture・パラメーター化メソッド・test case のどれでも）。

 [OmniTestRunCounts](Omni.Editor.Diagnostics.OmniTestRunCounts.md)

テスト実行の集計値です。

### 列挙型（Enums）

 [GalaxyAcceptanceFailureClass](Omni.Editor.Diagnostics.GalaxyAcceptanceFailureClass.md)

Galaxy受入の開始・復元境界で扱う失敗分類です。
文字列はPowerShellランナーとの交換契約として小文字へ正規化します。

 [OmniForegroundState](Omni.Editor.Diagnostics.OmniForegroundState.md)

Editor が OS の前面にあるかどうかです。

 [OmniInputDeliverySessionState](Omni.Editor.Diagnostics.OmniInputDeliverySessionState.md)

入力到達ログのセッションの状態です。

 [OmniObservationOutcome](Omni.Editor.Diagnostics.OmniObservationOutcome.md)

撮影・テスト・計測などの観測の結果です。値は外部ランナーの終了コードと一致します。

 [OmniObservationReason](Omni.Editor.Diagnostics.OmniObservationReason.md)

観測を無効（<xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Unavailable" data-throw-if-not-resolved="false"></xref>）にした理由です。
JSON と応答のマーカー行には名前で書くため、既存の名前は変えずに末尾へ追加だけします。
