# <a id="Omni_Logical_PoseBakeRejection"></a> Enum PoseBakeRejection

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Omni.Sequencer.Runtime.dll  

ベイク済みサンプルを使えないと判断した理由です。

<p>
「使えない」ことを bool ひとつで返すと、どの前提が崩れたのかが再生時に分からなくなります。
フォールバックは正常動作の一部（ベイク未生成のクリーンチェックアウトでも絵は出る）なので、
理由を値として持ち、診断とテストの両方から同じ列挙で確認できるようにします。
</p>

```csharp
public enum PoseBakeRejection
```

## フィールド（Fields）

`ChannelUnavailable = 9` 

チャンネルが要求された種類のデータを持っていません。



`ContentHashMismatch = 6` 

ベイク後にシーケンスまたは天体配置が変更されています。



`EmptySamples = 7` 

サンプルが1つも入っていないか、配列長が宣言と食い違っています。



`FormatVersionMismatch = 2` 

ベイクデータの形式バージョンが現在の実装と一致しません。



`InterpolationFailed = 14` 

Logical値の復元または補間が失敗しました。



`MissingAsset = 1` 

ベイクアセットが割り当てられていません。



`None = 0` 

棄却していません。ベイク済みサンプルをそのまま使えます。



`ObserverEyeRequired = 12` 

Observerの視点差分が必要な状態です。ベイクは絶対Logical座標なので使えません。



`PrecisionMismatch = 3` 

ベイク時と現在で固定小数点の構成（総ビット数・小数部ビット数）が異なります。
raw limbの意味が変わるため、詰め直さずに棄却します。



`SceneMismatch = 4` 

ベイク元のシーンが現在のシーンと一致しません。



`SourceMismatch = 5` 

ベイク元のシーケンス（Timeline）が一致しません。



`TargetMoved = 11` 

ベイク時の対象位置と現在の対象位置が一致しません（動的ターゲットが移動した）。



`TargetUnresolved = 10` 

注視対象IDをシーン上のオブジェクトへ解決できませんでした。



`TimeOutOfRange = 8` 

この時刻に有効な（重みが正の）ベイククリップがありません。ベイク範囲の外の時刻は端のサンプルへ寄せるので、このコードにはなりません。



`UserCameraOverride = 13` 

ユーザーがカメラを操作したため、演出の姿勢を上書きできません。
