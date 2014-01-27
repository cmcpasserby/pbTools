class PsAdjustmentReference :
    psRelative = 1
    psAbsolute = 2
    
class PsAnchorPosition :
    psTopLeft = 1
    psTopCenter = 2
    psTopRight = 3
    psMiddleLeft = 4
    psMiddleCenter = 5
    psMiddleRight = 6
    psBottomLeft = 7
    psBottomCenter = 8
    psBottomRight = 9
class PsAntiAlias  :
    psNoAntialias = 1
    psSharp = 2
    psCrisp = 3
    psStrong = 4
    psSmooth = 5

class PsAutoKernType  :
    psManual = 1
    psMetrics = 2
    psOptical = 3

class PsBatchDestinationType  :
    psNoDestination = 1
    psSaveAndClose = 2
    psFolder = 3

class PsBitmapConversionType  :
    psHalfThreshold = 1
    psPatternDither = 2
    psDiffusionDither = 3
    psHalftoneScreen = 4
    psCustomPattern = 5

class PsBitmapHalfToneType  :
    psHalftoneRound = 1
    psHalftoneDiamond = 2
    psHalftoneEllipse = 3
    psHalftoneLine = 4
    psHalftoneSquare = 5
    psHalftoneCross = 6

class PsBitsPerChannelType  :
    psDocument1Bit = 1
    psDocument8Bits = 8
    psDocument16Bits = 16
    psDocument32Bit = 32
    psPassThrough = 1
    psNormalBlend = 2
    psDissolve = 3
    psDarken = 4
    psMultiply = 5
    psColorBurn = 6
    psLinearBurn = 7
    psLighten = 8
    psScreen = 9
    psColorDodge = 10
    psLinearDodge = 11
    psOverlay = 12
    psSoftLight = 13
    psHardLight = 14
    psVividLight = 15
    psLinearLight = 16
    psPinLight = 17
    psDifference = 18
    psExclusion = 19
    psHue = 20
    psSaturationBlend = 21
    psColorBlend = 22
    psLuminosity = 23
    psHardMix = 26
    psLighterColor = 27
    psDarkerColor = 28
    psSubtract = 29
    psDivid = 30

class PsBMPDepthType  :
    psBMP1Bit = 1
    psBMP4Bits = 4
    psBMP8Bits = 8
    psBMP16Bits = 16
    psBMP24Bits = 24
    psBMP32Bits = 32
    psBMP_X1R5G5B5 = 60
    psBMP_A1R5G5B5 = 61
    psBMP_R5G6B5 = 62
    psBMP_X4R4G4B4 = 63
    psBMP_A4R4G4B4 = 64
    psBMP_R8G8B8 = 65
    psBMP_X8R8G8B8 = 66
    psBMP_A8R8G8B8 = 67

class PsByteOrder  :
    psIBMByteOrder = 1
    psMacOSByteOrder = 2

class PsCameraRAWSettingsType  :
    psCameraDefault = 0
    psSelectedImage = 1
    psCustomSettings = 2

class PsCameraRAWSize  :
    psMinimumCameraRAW = 0
    psSmallCameraRAW = 1
    psMediumCameraRAW = 2
    psLargeCameraRAW = 3
    psExtraLargeCameraRAW = 4
    psMaximumCameraRAW = 5
    psNormalCase = 1
    psAllCaps = 2
    psSmallCaps = 3

class PsChangeMode   :
    psConvertToGrayscale = 1
    psConvertToRGB = 2
    psConvertToCMYK = 3
    psConvertToLab = 4
    psConvertToBitmap = 5
    psConvertToIndexedColor = 6
    psConvertToMultiChannel = 7

class PsChannelType  :
    psComponentChannel = 1
    psMaskedAreaAlphaChannel = 2
    psSelectedAreaAlphaChannel = 3
    psSpotColorChannel = 4

class PsColorBlendMode  :
    psNormalBlendColor = 2
    psDissolveBlend = 3
    psDarkenBlend = 4
    psMultiplyBlend = 5
    psColorBurnBlend = 6
    psLinearBurnBlend = 7
    psLightenBlend = 8
    psScreenBlend = 9
    psColorDodgeBlend = 10
    psLinearDodgeBlend = 11
    psOverlayBlend = 12
    psSoftLightBlend = 13
    psHardLightBlend = 14
    psVividLightBlend = 15
    psLinearLightBlend = 16
    psPinLightBlend = 17
    psDifferenceBlend = 18
    psExclusionBlend = 19
    psHueBlend = 20
    psSaturationBlendColo = 21
    psColorBlendMode = 22
    psLuminosityBlen = 23
    psBehindBlend = 24
    psClearBlend = 25
    psHardMixBlend = 26
    psSubtract = 27
    psDivide = 28

class PsColorModel  :
    psGrayscaleModel = 1
    psRGBModel = 2
    psCMYKModel = 3
    psLabModel = 4
    psHSBModel = 5
    psNoModel = 50

class PsColorPicker  :
    psAdobeColorPicker = 1
    psAppleColorPicker = 2
    psWindowsColorPicker = 3
    psPlugInColorPicker = 4

class PsColorProfileType  :
    psNo = 1
    psWorking = 2
    psCustom = 3

class PsColorReductionType  :
    psPerceptualReduction = 0
    psSelective = 1
    psAdaptive = 2
    psRestrictive = 3
    psCustomReduction = 4
    psBlackWhiteReduction = 5
    psSFWGrayscale = 6
    psMacintoshColors = 7
    psWindowsColors = 8

class PsColorSpaceType  :
    psAdobeRGB = 0
    psColorMatchRGB = 1
    psProPhotoRGB = 2
    psSRGB = 3

class PsCopyrightedType  :
    psCopyrightedWork = 1
    psPublicDomain = 2
    psUnmarked = 3

class PsCreateFields   :
    psDuplication = 1
    psInterpolation = 2

class PsCropToType  :
    psBoundingBox = 0
    psMediaBox = 1
    psCropBox = 2
    psBleedBox = 3
    psTrimBox = 4
    psArtBox = 5

class PsDCSType  :
    psNoComposite = 1
    psGrayscaleComposite = 2
    psColorComposite = 3

class PsDepthMapSource  :
    psNoSource = 1
    psTransparencyChannel = 2
    psLayerMask = 3
    psImageHighlight = 4

class PsDescValueType  :
    psIntegerType = 1
    psDoubleType = 2
    psUnitDoubleType = 3
    psStringType = 4
    psBooleanType = 5
    psListType = 6
    psObjectType = 7
    psEnumeratedType = 8
    psReferenceType = 9
    psClassType = 10
    psAliasType = 11
    psRawType = 12

class PsDialogModes  :
    psDisplayAllDialogs = 1
    psDisplayErrorDialogs = 2
    psDisplayNoDialogs = 3

class PsDirection  :
    psHorizontal = 1
    psVertical = 2

class PsDisplacementMapType  :
    psStretchToFit = 1
    psTile = 2

class PsDitherType  :
    psNoDither = 1
    psDiffusion = 2
    psPattern = 3
    psNoise = 4

class PsDocumentFill  :
    psWhite = 1
    psBackgroundColor = 2
    psTransparent = 3

class PsDocumentMode  :
    psGrayscale = 1
    psRGB = 2
    psCMYK = 3
    psLab = 4
    psBitmap = 5
    psIndexedColor = 6
    psMultiChannel = 7
    psDuotone = 8

class PsEditLogItemsType  :
    psSessionOnly = 1
    psConcise = 2
    psDetailed = 3

class PsElementPlacement  :
    psPlaceInside = 0
    psPlaceAtBeginning = 1
    psPlaceAtEnd = 2
    psPlaceBefore = 3
    psPlaceAfter = 4

class PsEliminateFields   :
    psOddFields = 1
    psEvenFields = 2

class PsExportType  :
    psIllustratorPaths = 1
    psSaveForWeb = 2

class PsExtensionType  :
    psLowercase = 2
    psUppercase = 3

class PsFileNamingType  :
    psDocumentNameMixed = 1
    psDocumentNameLower = 2
    psDocumentNameUpper = 3
    psSerialNumber1 = 4
    psSerialNumber2 = 5
    psSerialNumber3 = 6
    psSerialNumber4 = 7
    psSerialLetterLower = 8
    psSerialLetterUpper = 9
    psMmddyy = 10
    psMmdd = 11
    psYyyymmdd = 12
    psYymmdd = 13
    psYyddmm = 14
    psDdmmyy = 15
    psDdmm = 16
    psExtensionLower = 17
    psExtensionUpper = 18
    psFontPreviewNone = 0
    psFontPreviewSmall = 1
    psFontPreviewMedium = 2
    psFontPreviewLarge = 3

class PsForcedColors  :
    psNoForced = 1
    psBlackWhite = 2
    psPrimaries = 3
    psWeb = 4

class PsFormatOptionsType  :
    psStandardBaseline = 1
    psOptimizedBaseline = 2
    psProgressive = 3

class PsGalleryConstrainType  :
    psConstrainWidth = 1
    psConstrainHeight = 2
    psConstrainBoth = 3

class PsGalleryFontType  :
    psArial = 1
    psCourierNew = 2
    psHelvetica = 3
    psTimesNewRoman = 4

class PsGallerySecurityTextPositionType  :
    psCentered = 1
    psUpperLeft = 2
    psLowerLeft = 3
    psUpperRight = 4
    psLowerRight = 5

class PsGallerySecurityTextRotateType  :
    psZero = 1
    psClockwise45 = 2
    psClockwise90 = 3
    psCounterClockwise45 = 4
    psCounterClockwise90 = 5

class PsGallerySecurityType  :
    psNoSecurity = 1
    psCustomSecurityText = 2
    psFilename = 3
    psCopyright = 4
    psCaption = 5
    psCredit = 6
    psTitle = 7

class PsGalleryThumbSizeType  :
    psSmall = 1
    psMedium = 2
    psLarge = 3
    psCustomThumbnail = 4

class PsGeometry  :
    psTriangle = 0
    psPentagon = 1
    psHexagon = 2
    psSquareGeometry = 3
    psHeptagon = 4
    psOctagon = 5

class PsGridLineStyle  :
    psGridSolidLine = 1
    psGridDashedLine = 2
    psGridDottedLine = 3

class PsGridSize  :
    psNoGrid = 1
    psSmallGrid = 2
    psMediumGrid = 3
    psLargeGrid = 4

class PsGuideLineStyle  :
    psGuideSolidLine = 1
    psGuideDashedLine = 2

class PsIllustratorPathType  :
    psDocumentBounds = 1
    psAllPaths = 2
    psNamedPath = 3

class PsIntent  :
    psPerceptual = 1
    psSaturation = 2
    psRelativeColorimetric = 3
    psAbsoluteColorimetric = 4

class PsJavaScriptExecutionMode  :
    psNeverShowDebugger = 1
    psDebuggerOnError = 2
    psBeforeRunning = 3

class PsJustification  :
    psLeft = 1
    psCenter = 2
    psRight = 3
    psLeftJustified = 4
    psCenterJustified = 5
    psRightJustified = 6
    psFullyJustified = 7

class PsLanguage  :
    psEnglishUSA = 1
    psEnglishUK = 2
    psFrench = 3
    psCanadianFrench = 4
    psFinnish = 5
    psGerman = 6
    psOldGerman = 7
    psSwissGerman = 8
    psItalian = 9
    psNorwegian = 10
    psNynorskNorwegian = 11
    psPortuguese = 12
    psBrazillianPortuguese = 13
    psSpanish = 14
    psSwedish = 15
    psDutch = 16
    psDanish = 17

class PsLayerCompressionType  :
    psRLELayerCompression = 1
    psZIPLayerCompression = 2

class PsLayerKind  :
    psNormalLayer = 1
    psTextLayer = 2
    psSolidFillLayer = 3
    psGradientFillLayer = 4
    psPatternfillLayer = 5
    psLevelsLayer = 6
    psCurvesLayer = 7
    psColorBalanceLayer = 8
    psBrightnessContrastLayer = 9
    psHueSaturationLayer = 10
    psSelectiveColorLayer = 11
    psChannelMixerLayer = 12
    psGradientMapLayer = 13
    psInversionLayer = 14
    psThresholdLayer = 15
    psPosterizeLayer = 16
    psSmartObjectLayer = 17
    psPhotoFilterLayer = 18
    psExposureLayer = 19
    psLayer3D = 20
    psVideoLayer = 21
    psBlackAndWhiteLayer = 22
    psVibrance = 23

class PsLayerType  :
    psArtLayer = 1
    psLayerSet = 2

class PsLensType  :
    psZoomLens = 1
    psPrime35 = 2
    psPrime105 = 3
    psMoviePrime = 5

class PsMagnificationType  :
    psActualSize = 0
    psFitPage = 1

class PsMatteType  :
    psNoMatte = 1
    psForegroundColorMatte = 2
    psBackgroundColorMatte = 3
    psWhiteMatte = 4
    psBlackMatte = 5
    psSemiGra = 6
    psNetscapeGrayMatte = 7

class PsMeasurementRange  :
    psAllMeasurements = 1
    psActiveMeasurements = 2

class PsMeasurementSource  :
    psMeasureSelection = 1
    psMeasureCountTool = 2
    psMeasureRulerTool = 3

class PsNewDocumentMode  :
    psNewGray = 1
    psNewRGB = 2
    psNewCMYK = 3
    psNewLab = 4
    psNewBitmap = 5

class PsNoiseDistribution  :
    psUniformNoise = 1
    psGaussianNoise = 2

class PsOffsetUndefinedAreas   :
    psOffsetSetToLayerFill = 1
    psOffsetWraparound = 2
    psOffsetRepeatEdgePixels = 3

class PsOpenDocumentMode  :
    psOpenGray = 1
    psOpenRGB = 2
    psOpenCMYK = 3
    psOpenLab = 4

class PsOpenDocumentType  :
    psPhotoshopOpen = 1
    psBMPOpen = 2
    psCompuServeGIFOpen = 3
    psPhotoshopEPSOpen = 4
    psFilmstripOpen = 5
    psJPEGOpe = 6
    psPCXOpen = 7
    psPhotoshopPDFOpen = 8
    psPhotoCDOpen = 9
    psPICTFileFormatOpen = 10
    psPICTResourceFormatOpen = 11
    psPixarOpen = 12
    psPNGOpen = 13
    psRawOpen = 14
    psScitexCTOpen = 15
    psTargaOpen = 16
    psTIFFOpen = 17
    psPhotoshopDCS_1Open = 18
    psPhotoshopDCS_2Open = 19
    psPDFOpen = 21
    psEPSOpen = 22
    psEPSPICTPreviewOpen = 23
    psEPSTIFFPreviewOpen = 24
    psAliasPIXOpen = 25
    psElectricImageOpen = 26
    psPortableBitmapOpen = 27
    psWavefrontRLAOpen = 28
    psSGIRGBOpen = 29
    psSoftImageOpen = 30
    psWirelessBitmapOpen = 31
    psCameraRAWOpen = 32
    psDICOMOpen = 33

class PsOperatingSystem  :
    psOS2 = 1
    psWindows = 2

class PsOrientation  :
    psLandscape = 1
    psPortrait = 2

class PsOtherPaintingCursors  :
    psStandardOther = 1
    psPreciseOther = 2

class PsPaintingCursors  :
    psStandard = 1
    psPrecise = 2
    psBrushsize = 3

class PsPaletteType  :
    psExact = 1
    psMacOSPalette = 2
    psWindowsPalett = 3
    psWebPalette = 4
    psUniform = 5
    psLocalPerceptual = 6
    psLocalSelective = 7
    psLocalAdaptive = 8
    psMasterPerceptual = 9
    psMasterSelective = 10
    psMasterAdaptive = 11
    psPreviousPalette = 12

class PsPathKind  :
    psNormalPath = 1
    psClippingPath = 2
    psWorkPath = 3
    psVectorMask = 4
    psTextMask = 5

class PsPDFCompatibilityType  :
    psPDF1 = 1
    psPDF1 = 2
    psPDF1 = 3
    psPDF1 = 4

class PsPDFEncoding  :
    psPDFNon = 0
    psPDFZip = 1
    psPDFJPEG = 2
    psPDFPDFZip4Bi = 3
    psPDFJPEGHIG = 4
    psPDFJPEGMEDHIG = 5
    psPDFJPEGME = 6
    psPDFJPEGMEDLO = 7
    psPDFJPEGLO = 8
    psPDFJPEG2000High = 9
    psPDFJPEG2000MEDHIGH = 10
    psPDFJPEG2000MED = 11
    psPDFJPEG2000MEDLOW = 12
    psPDFJPEG2000LOW = 13
    psPDFJPEG2000LOSSLESS = 14

class PsPDFResampleType  :
    psNoResampl = 0
    psPDFAverag = 1
    psPDFSubSample = 2
    psPDFBicubi = 3

class PsPDFStandardType  :
    psNoStandar = 0
    psPDFX1A200 = 1
    psPDFX1A200 = 2
    psPDFX3200 = 3
    psPDFX32003 = 4

class PsPhotoCDColorSpace  :
    psRGB8 = 1
    psRGB16 = 2
    psLab8 = 3
    psLab16 = 4

class PsPhotoCDSize  :
    psMinimumPhotoCD = 1
    psSmallPhotoCD = 2
    psMediumPhotoCD = 3
    psLargePhotoCD = 4
    psExtralargePhotoCD = 5
    psMaximumPhotoCD = 6

class PsPICTBitsPerPixels  :
    psPICTTwoBits = 2
    psPICTFourBits = 4
    psPICTEightBits = 8
    psPICTSixteenBits = 16
    psPICTThirtyTwoBits = 32

class PsPICTCompression  :
    psNoPICTCompression = 1
    psJPEGLowPICT = 2
    psJPEGMediumPICT = 4
    psJPEGHighPICT = 5
    psJPEGMaximumPICT = 6

class PsPicturePackageTextType  :
    psNoText = 1
    psUserText = 2
    psFilenameText = 3
    psCopyrightText = 4
    psCaptionText = 5
    psCreditText = 6
    psOriginText = 7

class PsPointKind  :
    psSmoothPoint = 1
    psCornerPoint = 2

class PsPointType  :
    psPostScriptPoints = 1
    psTraditionalPoints = 2

class PsPolarConversionType  :
    psRectangularToPolar = 1
    psPolarToRectangular = 2

class PsPreviewType  :
    psNoPreview = 1
    psMonochromeTIFF = 2
    psEightbitTIFF = 3

class PsPurgeTarget   :
    psUndoCaches = 1
    psHistoryCaches = 2
    psClipboardCache = 3
    psAllCaches = 4

class PsQueryStateType  :
    psAlways = 1
    psAsk = 2
    psNever = 3

class PsRadialBlurMethod :
    psSpin = 1
    psZoom = 2

class PsRadialBlurQuality  :
    psRadialBlurDraft = 1
    psRadialBlurGood = 2
    psRadialBlurBest = 3

class PsRasterizeType  :
    psTextContents = 1
    psShape = 2
    psFillContent = 3
    psLayerClippingPath = 4
    psEntireLayer = 5
    psLinkedLayers = 6

class PsReferenceFormType   :
    psReferenceNameType = 1
    psReferenceIndexType = 2
    psReferenceIdentifierType = 3
    psReferenceOffsetType = 4
    psReferenceEnumeratedType = 5
    psReferencePropertyType = 6
    psReferenceClassType = 7

class PsResampleMethod  :
    psNoResampling = 1
    psNearestNeighbor = 2
    psBilinear = 3
    psBicubic = 4
    psBicubicSharper = 5
    psBicubicSmoother = 6

class PsRippleSize  :
    psSmallRipple = 1
    psMediumRipple = 2
    psLargeRipple = 3

class PsSaveBehavior  :
    psNeverSave = 1
    psAlwaysSave = 2
    psAskWhenSaving = 3

class PsSaveDocumentType  :
    psPhotoshopSave = 1
    psBMPSave = 2
    psCompuServeGIFSave = 3
    psPhotoshopEPSSave = 4
    psJPEGSave = 6
    psPCXSave = 7
    psPhotoshopPDFSave = 8
    psPICTFileFormatSave = 10
    psPixarSave = 12
    psPNGSave = 13
    psRawSave = 14
    psScitexCTSave = 15
    psTargaSave = 16
    psTIFFSave = 17
    psPhotoshopDCS_1Save = 18
    psPhotoshopDCS_2Save = 19
    psAliasPIXSave = 25
    psElectricImageSave = 26
    psPortableBitmapSave = 27
    psWavefrontRLASave = 28
    psSGIRGBSave = 29
    psSoftImageSave = 30
    psWirelessBitmapSave = 31

class PsSaveEncoding  :
    psBinary = 1
    psJPEGLow = 2
    psAscii = 3
    psJPEGMedium = 4
    psJPEGHigh = 5
    psJPEGMaximum = 6

class PsSaveLogItemsType  :
    psMetadata = 1
    psLogFile = 2
    psLogFileAndMetadata = 3

class PsSaveOptions  :
    psSaveChanges = 1
    psDoNotSaveChanges = 2
    psPromptToSaveChanges = 3

class PsSelectionType  :
    psReplaceSelection = 1
    psExtendSelection = 2
    psDiminishSelection = 3
    psIntersectSelection = 4

class PsShapeOperation  :
    psShapeAdd = 1
    psShapeXOR = 2
    psShapeIntersect = 3
    psShapeSubtract = 4

class PsSmartBlurMode   :
    psSmartBlurNormal = 1
    psSmartBlurEdgeOnly = 2
    psSmartBlurOverlayEdge = 3

class PsSmartBlurQuality  :
    psSmartBlurLow = 1
    psSmartBlurMedium = 2
    psSmartBlurHigh = 3

class PsSourceSpaceType  :
    psDocumentSpace = 1
    psProofSpace = 2

class PsSpherizeMode   :
    psNormalSpherize = 1
    psHorizontalSpherize = 2
    psVerticalSpherize = 3

class PsStrikeThruType  :
    psStrikeOff = 1
    psStrikeHeight = 2
    psStrikeBox = 3

class PsStrokeLocation  :
    psInsideStroke = 1
    psCenterStroke = 2
    psOutsideStroke = 3

class PsTargaBitsPerPixels  :
    psTarga16Bits = 16
    psTarga24Bits = 24
    psTarga32Bits = 32

class PsTextComposer  :
    psAdobeSingleLine = 1
    psAdobeEveryLine = 2

class PsTextType  :
    psPointText = 1
    psParagraphText = 2

class PsTextureType  :
    psBlocksTexture = 1
    psCanvasTexture = 2
    psFrostedTexture = 3
    psTinyLensTexture = 4
    psTextureFile = 5

class PsTIFFEncodingType  :
    psNoTIFFCompression = 1
    psTiffLZW = 2
    psTiffJPEG = 3
    psTiffZIP = 4

class PsToolType  :
    psPencil = 1
    psBrush = 2
    psEraser = 3
    psBackgroundEraser = 4
    psCloneStamp = 5
    psPatternStamp = 6
    psHealingBrush = 7
    psHistoryBrush = 8
    psArtHistoryBrush = 9
    psSmudge = 10
    psBlur = 11
    psSharpen = 12
    psDodge = 13
    psBurn = 14
    psSponge = 15
    psColorReplacementTool = 16

class PsTransitionType  :
    psBlindsHorizontal = 1
    psBlindsVertical = 2
    psDissolveTransition = 3
    psBoxIn = 4
    psBoxOut = 5
    psGlitterDown = 6
    psGlitterRight = 7
    psGlitterRightDown = 8
    psNoTransition = 9
    psRandom = 10
    psSplitHorizontalIn = 11
    psSplitHorizontalOut = 12
    psSplitVerticalIn = 13
    psSplitVerticalOut = 14
    psWipeDown = 15
    psWipeLleft = 16
    psWipeRight = 17
    psWipeUp = 18

class PsTrimType  :
    psTransparentPixels = 0
    psTopLeftPixel = 1
    psBottomRightPixe = 9

class PsTypeUnits  :
    psTypePixels = 1
    psTypeMM = 4
    psTypePoints = 5

class PsUndefinedAreas   :
    psWrapAround = 1
    psRepeatEdgePixels = 2

class PsUnderlineType  :
    psUnderlineOff = 1
    psUnderlineRight = 2
    psUnderlineLeft = 3

class PsUnits  :
    psPixels = 1
    psInches = 2
    psCM = 3
    psMM = 4
    psPoints = 5
    psPicas = 6
    psPercent = 7

class PsUrgency  :
    psNone = 0
    psLow = 1
    psTwo = 2
    psThree = 3
    psFour = 4
    psNormal = 5
    psSix = 6
    psSeven = 7
    psHigh = 8

class PsWarpStyle  :
    psNone = 1
    psArc = 2
    psArcLower = 3
    psArcUpper = 4
    psArch = 5
    psBulge = 6
    psShellLower = 7
    psShellUpper = 8
    psFlag = 9
    psWave = 10
    psFish = 11
    psRise = 12
    psFishEye = 13
    psInflate = 14
    psSqueeze = 15
    psTwist = 16

class PsWaveType  :
    psSine = 1
    psTriangular = 2
    psSquare = 3

class PsWhiteBalanceType  :
    psAsShot = 0
    psAuto = 1
    psDaylight = 2
    psCloudy = 3
    psShade = 4
    psTungsten = 5
    psFluorescent = 6
    psFlash = 7
    psCustomCameraSettings = 8

class PsZigZagType   :
    psAroundCenter = 1
    psOutFromCenter = 2
    psPondRipples = 3
