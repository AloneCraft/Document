# <a id="Omni_BatchRendering_RadialBatchBackendState"></a> Enum RadialBatchBackendState

Namespace: [Omni.BatchRendering](Omni.BatchRendering.md)  
Assembly: Omni.BatchRendering.Runtime.dll  

SaturnのMesoリングをBRGで描画するバックエンドの状態です。

<p>
<code>MacroOnly</code> はMacroリングだけを描く安全な縮退であり、BRG描画の成功を意味しません。
Saturnシーンの <code>SaturnMesoBatchRenderer</code> がこの値を通信UIとbenchmark JSONへ公開します。
</p>

```csharp
public enum RadialBatchBackendState
```

## フィールド（Fields）

`Active = 3` 

少なくとも1つのCamera viewが最新フレームの資源を持つ稼働状態です。



`Disabled = 0` 

資源をまだ確保していない停止状態です。



`Faulted = 6` 

予期しないBRG例外が起き、明示的な再初期化まで描画を停止した状態です。



`Initializing = 1` 

BRG、Mesh、Material、RawBufferを検証・確保している状態です。



`MacroOnly = 5` 

BRGを使わずMacroリングのみを描く安全な縮退状態です。



`Ready = 2` 

BRGは有効だが、描画可能なCamera viewがまだ登録されていない状態です。



`Rebuilding = 4` 

viewごとのGPU資源を置換中で、旧資源を保持したまま更新する状態です。
