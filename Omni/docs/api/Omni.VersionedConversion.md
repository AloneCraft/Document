# <a id="Omni_VersionedConversion"></a> Namespace Omni.VersionedConversion

### クラス（Classes）

 [ConverterCandidate](Omni.VersionedConversion.ConverterCandidate.md)

特定の Editor と依存実体に対して検証された変換器の候補です。

 [UnityPackageObservation.ObservedPackage](Omni.VersionedConversion.UnityPackageObservation.ObservedPackage.md)

 [PackageContentDigest](Omni.VersionedConversion.PackageContentDigest.md)

解決済みパッケージの全ファイルを、パスと内容の両方で識別します。

 [PackageIdentity](Omni.VersionedConversion.PackageIdentity.md)

変換器を選ぶための、パッケージの版と解決済み内容の識別情報です。

 [ShaderConversionResult](Omni.VersionedConversion.ShaderConversionResult.md)

シェーダー変換の出力と失敗・除外・副生成物です。

 [ShaderPassDiagnostic](Omni.VersionedConversion.ShaderPassDiagnostic.md)

Pass ごとの元の判定と診断を、共通入口へ渡します。

 [UnityPackageObservation](Omni.VersionedConversion.UnityPackageObservation.md)

URP 固有の型へ参照せず、Package Manager の解決結果を記録します。

 [VersionedConverterCatalog<T\>](Omni.VersionedConversion.VersionedConverterCatalog\-1.md)

版別実装を登録し、適合するものが一つだけの場合に取得します。

 [VersionedConverterSelection](Omni.VersionedConversion.VersionedConverterSelection.md)

完全に一致する検証済み候補が一つだけの場合に選択します。

### インターフェース（Interfaces）

 [IShaderSourceAccess](Omni.VersionedConversion.IShaderSourceAccess.md)

版別変換器がシェーダーの論理パスを読み取る境界です。

 [IVersionedShaderConverter](Omni.VersionedConversion.IVersionedShaderConverter.md)

URP シェーダー本文の版別変換を表します。ファイルの書込みは行いません。

### 列挙型（Enums）

 [ShaderPassOutcome](Omni.VersionedConversion.ShaderPassOutcome.md)

共通入口が理解できる Pass の判定です。
