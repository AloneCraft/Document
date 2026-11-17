# <a id="Omni_Converter_RadialSourceResolver_PathRuleSourceProbe"></a> Enum RadialSourceResolver.PathRuleSourceProbe

Namespace: [Omni.Converter](Omni.Converter.md)  
Assembly: Omni.Converter.dll  

パス規則で元アセットを探した結果です。

```csharp
public enum RadialSourceResolver.PathRuleSourceProbe
```

## フィールド（Fields）

`Found = 1` 

元アセットが見つかった。



`Missing = 2` 

元の候補（ファイルまたは同名コンテナ）が一つも存在しない。



`NotApplicable = 0` 

生成物のフォルダ（Project/Packages/User）に当てはまらない。



`Unverifiable = 3` 

候補はあるが一致を確定できない、または元のPackage自体が見つからない。
