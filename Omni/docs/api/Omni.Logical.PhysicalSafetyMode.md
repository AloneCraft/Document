# <a id="Omni_Logical_PhysicalSafetyMode"></a> Enum PhysicalSafetyMode

Namespace: [Omni.Logical](Omni.Logical.md)  
Assembly: Radial.Runtime.dll  

有限描画プロキシを強制するかどうかです。設定UIには出さず、既定はAutoです（ForceProxyはテストが使います）。

```csharp
public enum PhysicalSafetyMode
```

## フィールド（Fields）

`Auto = 0` 

論理AABBが安全域内ならUnity標準Transformを使います。



`ForceProxy = 1` 

安全域内でも有限描画プロキシを使います。
