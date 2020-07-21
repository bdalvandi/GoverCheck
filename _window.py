# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class mainWin
###########################################################################

class mainWin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"GoverCheck +", pos = wx.DefaultPosition, size = wx.Size( 634,436 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
		self.SetLayoutDirection(wx.Layout_LeftToRight)

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		szPmrFile = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"PMR File" ), wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnOpen = wx.Button( szPmrFile.GetStaticBox(), wx.ID_ANY, u"Open", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.btnOpen, 0, wx.ALL, 5 )

		self.txtPmrFilename = wx.TextCtrl( szPmrFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		bSizer11.Add( self.txtPmrFilename, 1, wx.ALL, 5 )


		szPmrFile.Add( bSizer11, 1, wx.EXPAND, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText11 = wx.StaticText( szPmrFile.GetStaticBox(), wx.ID_ANY, u"Date:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer13.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.txtDate = wx.TextCtrl( szPmrFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_CENTER )
		bSizer13.Add( self.txtDate, 1, wx.ALL, 5 )


		bSizer12.Add( bSizer13, 1, wx.EXPAND, 5 )


		bSizer12.Add( ( 10, 0), 0, 0, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText12 = wx.StaticText( szPmrFile.GetStaticBox(), wx.ID_ANY, u"Time", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer14.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.txtTime = wx.TextCtrl( szPmrFile.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.TE_CENTER )
		bSizer14.Add( self.txtTime, 1, wx.ALL, 5 )


		bSizer12.Add( bSizer14, 1, wx.EXPAND, 5 )


		szPmrFile.Add( bSizer12, 1, wx.EXPAND, 5 )


		bSizer10.Add( szPmrFile, 1, wx.EXPAND, 5 )

		szPreview = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Preview" ), wx.VERTICAL )

		fgSizer3 = wx.FlexGridSizer( 2, 5, 0, 0 )
		fgSizer3.AddGrowableCol( 1 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )


		fgSizer3.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		fgSizer3.Add( ( 20, 0), 0, 0, 5 )

		self.m_staticText17 = wx.StaticText( szPreview.GetStaticBox(), wx.ID_ANY, u"Start Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		fgSizer3.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( szPreview.GetStaticBox(), wx.ID_ANY, u"Peak Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer3.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( szPreview.GetStaticBox(), wx.ID_ANY, u"End Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer3.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.btnPreview = wx.Button( szPreview.GetStaticBox(), wx.ID_ANY, u"Preview Frequency", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnPreview.Enable( False )

		fgSizer3.Add( self.btnPreview, 0, wx.ALL, 5 )


		fgSizer3.Add( ( 20, 0), 0, 0, 5 )

		selStartChoices = []
		self.selStart = wx.Choice( szPreview.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, selStartChoices, 0 )
		self.selStart.SetSelection( 0 )
		fgSizer3.Add( self.selStart, 0, wx.ALL, 5 )

		selPeakChoices = []
		self.selPeak = wx.Choice( szPreview.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, selPeakChoices, 0 )
		self.selPeak.SetSelection( 0 )
		fgSizer3.Add( self.selPeak, 0, wx.ALL, 5 )

		selEndChoices = []
		self.selEnd = wx.Choice( szPreview.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, selEndChoices, 0 )
		self.selEnd.SetSelection( 0 )
		fgSizer3.Add( self.selEnd, 0, wx.ALL, 5 )


		szPreview.Add( fgSizer3, 1, wx.EXPAND, 5 )


		bSizer10.Add( szPreview, 1, wx.EXPAND, 5 )

		szTrends = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Delay Correction" ), wx.VERTICAL )

		bSizer16 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnCreateTrend = wx.Button( szTrends.GetStaticBox(), wx.ID_ANY, u"Create Trends", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnCreateTrend.Enable( False )

		bSizer16.Add( self.btnCreateTrend, 0, wx.ALL, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btnShowTrend = wx.Button( szTrends.GetStaticBox(), wx.ID_ANY, u"Show Trends", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnShowTrend.Enable( False )

		bSizer16.Add( self.btnShowTrend, 0, wx.ALL, 5 )


		bSizer16.Add( ( 0, 0), 1, wx.EXPAND, 5 )


		szTrends.Add( bSizer16, 1, wx.EXPAND, 5 )


		bSizer10.Add( szTrends, 1, wx.EXPAND, 5 )

		szResult = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Result" ), wx.VERTICAL )

		bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnSelectFolder = wx.Button( szResult.GetStaticBox(), wx.ID_ANY, u"Selcet Folder", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.btnSelectFolder.Enable( False )

		bSizer17.Add( self.btnSelectFolder, 0, wx.ALL, 5 )

		self.txtFolder = wx.TextCtrl( szResult.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.txtFolder.Enable( False )

		bSizer17.Add( self.txtFolder, 1, wx.ALL, 5 )


		szResult.Add( bSizer17, 1, wx.EXPAND, 5 )

		bSizer18 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer18.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_staticText20 = wx.StaticText( szResult.GetStaticBox(), wx.ID_ANY, u"Filename Tag:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		bSizer18.Add( self.m_staticText20, 0, wx.ALL, 5 )

		selTagChoices = [ u"A", u"B", u"C", u"G", u"X" ]
		self.selTag = wx.Choice( szResult.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, selTagChoices, 0 )
		self.selTag.SetSelection( 0 )
		self.selTag.Enable( False )

		bSizer18.Add( self.selTag, 0, wx.ALL, 5 )


		szResult.Add( bSizer18, 1, wx.EXPAND, 5 )


		bSizer10.Add( szResult, 1, wx.EXPAND, 5 )

		szGenerate = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Generate" ), wx.VERTICAL )

		self.btnGen = wx.Button( szGenerate.GetStaticBox(), wx.ID_ANY, u"Generate", wx.DefaultPosition, wx.Size( 150,40 ), 0 )
		self.btnGen.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btnGen.Enable( False )

		szGenerate.Add( self.btnGen, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer10.Add( szGenerate, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer10 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnOpen.Bind( wx.EVT_BUTTON, self.onOpenPMR )
		self.btnPreview.Bind( wx.EVT_BUTTON, self.onPreviewFreq )
		self.btnCreateTrend.Bind( wx.EVT_BUTTON, self.onCreateTrends )
		self.btnShowTrend.Bind( wx.EVT_BUTTON, self.onShowTrends )
		self.btnSelectFolder.Bind( wx.EVT_BUTTON, self.onSelFolder )
		self.btnGen.Bind( wx.EVT_BUTTON, self.onGenerate )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def onOpenPMR( self, event ):
		event.Skip()

	def onPreviewFreq( self, event ):
		event.Skip()

	def onCreateTrends( self, event ):
		event.Skip()

	def onShowTrends( self, event ):
		event.Skip()

	def onSelFolder( self, event ):
		event.Skip()

	def onGenerate( self, event ):
		event.Skip()


