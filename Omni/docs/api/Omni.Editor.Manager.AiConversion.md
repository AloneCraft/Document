# <a id="Omni_Editor_Manager_AiConversion"></a> Namespace Omni.Editor.Manager.AiConversion

### クラス（Classes）

 [OmniAiConversionResult](Omni.Editor.Manager.AiConversion.OmniAiConversionResult.md)

AI が返す結果 JSON（<code>omni.ai-conversion-result/1</code>）です。エージェントは決まったパスへ書き、チャットは Manager の貼り付け欄に貼ります。
取り込み前に <xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionResult.TryValidate(Omni.Editor.Manager.AiConversion.OmniAiConversionResult%2cSystem.String%2cSystem.Collections.Generic.IEnumerable%7bSystem.String%7d%2cSystem.String%40%2cSystem.Int32%2cSystem.Boolean)" data-throw-if-not-resolved="false"></xref> で検査します（source 不一致、危険なパス、許可範囲外のファイル、規則欠けは拒否）。

 [OmniAiConversionState](Omni.Editor.Manager.AiConversion.OmniAiConversionState.md)

状態を決める純粋関数です（UnityEngine を使わない）。順序:
今の元に対する機械判定が成功なら、依頼・AI の結果に関係なく「変換済み」系（機械判定が最終）。
失敗なら、依頼が無ければ「変換不能」、依頼の後に元が変わっていれば「AI 修正後も変換不能」、変わっていなければ
「対応不可」（AI が none と答えた）か「AI 依頼中」。今の元に対する判定が無いときは、依頼が有れば「AI 依頼中」（再判定待ち）。

 [OmniAiConversionStatusText](Omni.Editor.Manager.AiConversion.OmniAiConversionStatusText.md)

状態の表示（見出し・アイコン名・ツールチップ）です。アイコンは Unity 組込み（<code>EditorGUIUtility.IconContent</code> の名前）で、
色は呼び出し側が <xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionIconColor" data-throw-if-not-resolved="false"></xref> から決めます。

 [OmniAiConversionStore](Omni.Editor.Manager.AiConversion.OmniAiConversionStore.md)

個人の作業記録（Git の外）の読み書きです。置き場は <code>&lt;プロジェクト&gt;/UserSettings/Omni/AiConversion/&lt;sourceGuid&gt;/</code>。
読み込みは、ファイルが無い・壊れている・形式が違うときに null を返し、例外を投げません。書き込みは一時ファイルへ書いてから置き換えます。
プロジェクトの場所はコンストラクタで差し替えられます（テスト用）。

 [OmniAiGraphInfo](Omni.Editor.Manager.AiConversion.OmniAiGraphInfo.md)

Shader Graph のときの作業内容です。

 [OmniAiHumanDecision](Omni.Editor.Manager.AiConversion.OmniAiHumanDecision.md)

AI が「人が判断すべき」と挙げた箇所です。

 [OmniAiOwnedFile](Omni.Editor.Manager.AiConversion.OmniAiOwnedFile.md)

プロンプトに入れる自作 Shader の 1 ファイル。チャット用は本文（<xref href="Omni.Editor.Manager.AiConversion.OmniAiOwnedFile.Content" data-throw-if-not-resolved="false"></xref>）が要り、エージェント用はパスだけを使います。

 [OmniAiPathRules](Omni.Editor.Manager.AiConversion.OmniAiPathRules.md)

AI が返す・Manager が扱うプロジェクト相対パスの規則です。

 [OmniAiPrompt](Omni.Editor.Manager.AiConversion.OmniAiPrompt.md)

組み立てたプロンプトと、コピー前に利用者へ見せる情報です。

 [OmniAiPromptBuilder](Omni.Editor.Manager.AiConversion.OmniAiPromptBuilder.md)

AI 変換依頼のプロンプトを組み立てます。単一の正本は <code>Documentation/CustomShaderAiPrompt.md</code>（<xref href="Omni.Editor.Manager.AiConversion.OmniAiPromptSource" data-throw-if-not-resolved="false"></xref>）で、
「守る規則」「状況別の振り分け」「してはいけないこと」「出力の形式」と結果 JSON の節はそこから取ります。
「対象」「今回の状況」「Omni が機械判定する条件」「ヒント」とファイル本文は、依頼ごとにここで組み立てます（日本語のみ）。

 [OmniAiPromptRequest](Omni.Editor.Manager.AiConversion.OmniAiPromptRequest.md)

プロンプトを組み立てるための事実です。閉包の収集（<code>OmniShaderLabClosureCollector.Collect</code>）と、本文・失敗の取得は呼び出し側が行います。

 [OmniAiPromptSection](Omni.Editor.Manager.AiConversion.OmniAiPromptSection.md)

プロンプトの 1 つの節（最上位の <code># 見出し</code> から次の見出しの前まで）。

 [OmniAiPromptSource](Omni.Editor.Manager.AiConversion.OmniAiPromptSource.md)

<code>Documentation/CustomShaderAiPrompt.md</code> のプロンプトを、目印の間から取り出して節に分けます（プロンプトの単一の正本）。
目印は 3 組あります: 本体 <code>omni:ai-prompt</code>、Manager が足す節 <code>omni:ai-prompt-manager</code>、実験的な振り分け <code>omni:ai-prompt-experimental</code>。
各目印の間の <code>````text</code> で囲んだ内側が本文で、最上位の <code># </code> 見出しで節に分けます。
読み込めない・形が崩れているときは例外ではなく理由を返します（呼び出し側はコピーを無効にして理由を出す）。

 [OmniAiRequest](Omni.Editor.Manager.AiConversion.OmniAiRequest.md)

AI への依頼の記録（<code>request.json</code>）です。依頼のたびに上書きします。

 [OmniAiRestoreItem](Omni.Editor.Manager.AiConversion.OmniAiRestoreItem.md)

退避から戻すときの 1 ファイルの説明です。

 [OmniAiRestoreReport](Omni.Editor.Manager.AiConversion.OmniAiRestoreReport.md)

戻した結果です。

 [OmniAiRuleResult](Omni.Editor.Manager.AiConversion.OmniAiRuleResult.md)

規則 1〜14 のうち 1 つの結果です。

 [OmniAiSnapshotEntry](Omni.Editor.Manager.AiConversion.OmniAiSnapshotEntry.md)

退避した 1 ファイル。<code>sha256</code> が "absent" なら、退避した時点でファイルが無かった。

 [OmniAiSnapshotManifest](Omni.Editor.Manager.AiConversion.OmniAiSnapshotManifest.md)

依頼時の退避の一覧（<code>snapshots/&lt;attempt&gt;/manifest.json</code>）です。

 [OmniJudgeCompileMessage](Omni.Editor.Manager.AiConversion.OmniJudgeCompileMessage.md)

生成物のコンパイルエラー（J6／G4）です。

 [OmniJudgePass](Omni.Editor.Manager.AiConversion.OmniJudgePass.md)

変換器が各 Pass に何をしたか（OmniShaderPatcher の診断を構造にしたもの）です。

 [OmniJudgeReport](Omni.Editor.Manager.AiConversion.OmniJudgeReport.md)

自作 Shader 1 本の機械判定の結果です。judge.json にそのまま保存します。

 [OmniJudgeSilentHit](Omni.Editor.Manager.AiConversion.OmniJudgeSilentHit.md)

生成に成功しても黙ってワープされない書き方の検出結果です（J3）。

 [OmniJudgeStage](Omni.Editor.Manager.AiConversion.OmniJudgeStage.md)

判定の段（J1〜J6／G1〜G5）ごとの結果です。

### 構造体（Structs）

 [OmniAiConversionInputs](Omni.Editor.Manager.AiConversion.OmniAiConversionInputs.md)

<xref href="Omni.Editor.Manager.AiConversion.OmniAiConversionState.Evaluate(Omni.Editor.Manager.AiConversion.OmniAiConversionInputs%40)" data-throw-if-not-resolved="false"></xref> への入力です。呼び出し側が、保存済みのデータから 1 本ぶん組み立てます。

### 列挙型（Enums）

 [OmniAiConversionIconColor](Omni.Editor.Manager.AiConversion.OmniAiConversionIconColor.md)

アイコンの色の分類です。

 [OmniAiConversionStatus](Omni.Editor.Manager.AiConversion.OmniAiConversionStatus.md)

自作 Shader 1 本の「AI 変換依頼」の状態です。Shaders タブのアイコンと詳細欄の見出しになります。

 [OmniAiRestoreChange](Omni.Editor.Manager.AiConversion.OmniAiRestoreChange.md)

退避との比較の種類。
