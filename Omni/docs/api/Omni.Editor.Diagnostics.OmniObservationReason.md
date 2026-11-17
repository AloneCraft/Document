# <a id="Omni_Editor_Diagnostics_OmniObservationReason"></a> Enum OmniObservationReason

Namespace: [Omni.Editor.Diagnostics](Omni.Editor.Diagnostics.md)  
Assembly: Omni.Editor.dll  

観測を無効（<xref href="Omni.Editor.Diagnostics.OmniObservationOutcome.Unavailable" data-throw-if-not-resolved="false"></xref>）にした理由です。
JSON と応答のマーカー行には名前で書くため、既存の名前は変えずに末尾へ追加だけします。

```csharp
public enum OmniObservationReason
```

## フィールド（Fields）

`AssemblyReloadInterrupted = 26` 

観測の途中で assembly の再読み込み（Domain Reload）が始まり、観測を打ち切りました。



`AssetDatabaseUpdating = 5` 

AssetDatabase の更新中でした。



`BackendMismatch = 25` 

Scene の描画 backend が観測の要求と違いました。



`BackgroundOnly = 21` 

画像に背景以外の画素がありませんでした。



`BrgSequenceDidNotAdvance = 14` 

観測窓の間に、BRG の culling 世代と順番が進みませんでした。



`Compiling = 4` 

スクリプトのコンパイル中でした。



`ConcurrentAutomationRequest = 28` 

観測の間に、別の自動化の要求が受理されました。その要求が送る合成イベントを、届いた入力と区別できません。



`ControlMismatch = 22` 

既知の正解を持つ対照が期待どおりではありませんでした。



`DirtySceneLoaded = 2` 

未保存の変更を持つ Scene が読み込まれていました。



`EditorNotForeground = 10` 

Editor が前面にありませんでした。



`ExpectedSceneMissing = 1` 

期待した Scene が読み込まれていませんでした。



`ExtraSceneLoaded = 0` 

期待した集合の外の Scene が読み込まれていました。



`ForegroundLostDuringObservation = 11` 

観測の途中で Editor が前面を失いました。



`ForegroundPixelsZero = 20` 

比較の対象の画素が 0（または下限未満）でした。



`ForegroundUnknown = 12` 

Editor が前面にあるかを判定できませんでした。



`FramesDidNotAdvance = 13` 

観測窓の間に、対象の描画回数が要求した数だけ進みませんでした。



`InputNotDelivered = 27` 

入力を送った前後で、Unity が受けた入力イベントが 0 件（または期待した操作のイベントが 0 件）でした。入力が Unity に届いていません。



`NoTestExecuted = 18` 

テストは選ばれましたが、合格・不合格のどちらにもなったものがありませんでした。



`ObservationAlreadyRunning = 9` 

同じ観測が既に実行中でした。



`OccludedByFloatingWindow = 16` 

測定に使った画素の領域に、浮いた EditorWindow が重なっていました。



`OccludedByOverlay = 15` 

Omni Overlay が展開されたままで、画面の撮影に写り得ました。



`PlayModeActive = 3` 

Play Mode 中、または Play Mode へ切り替わる途中でした。



`RefreshPending = 8` 

外部要求の refresh が完了していませんでした。



`SceneViewUnavailable = 23` 

観測に使う Scene View を得られませんでした。



`ScriptCompilationFailed = 6` 

直近のスクリプトのコンパイルが失敗しており、古い assembly が動いていました。



`TestFilterStateUnknown = 29` 

要求したテスト名を読めませんでした。要求の記録が無く、全件か名前付きかを区別できません。



`TestRunActive = 7` 

別のテスト実行が進行中でした。



`UnmatchedTestFilter = 19` 

要求したテスト名に一致し、実行されたテストがありませんでした。



`UnsupportedScene = 24` 

観測が対象としない Scene でした。



`ZeroTests = 17` 

実行されたテストの総数が 0 でした。
