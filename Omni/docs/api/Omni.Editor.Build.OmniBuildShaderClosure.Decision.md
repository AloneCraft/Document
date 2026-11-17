# <a id="Omni_Editor_Build_OmniBuildShaderClosure_Decision"></a> Enum OmniBuildShaderClosure.Decision

Namespace: [Omni.Editor.Build](Omni.Editor.Build.md)  
Assembly: Omni.Editor.dll  

Shader の扱い。

```csharp
public enum OmniBuildShaderClosure.Decision
```

## フィールド（Fields）

`Engine = 1` 

エンジン内蔵（Assets / Packages の外）なので判定しない。



`Keep = 0` 

理由があって残す。



`Strip = 3` 

外す。



`UnclassifiedHidden = 2` 

どの理由にも当たらないが、Hidden/ なので外さない（StripUnclassifiedHidden が false のとき）。
