from PyQt4 import QtGui, QtCore
from .display import DisplayObject
from .utils import Object, getColor


__author__ = "Yuehao Wang"


class TextFormatAlign(Object):
	RIGHT = "right"
	LEFT = "left"
	CENTER = "center"
	START = "start"
	END = "end"

	def __init__(self):
		raise Exception("TextFormatAlign cannot be instantiated.")


class TextFormatBaseline(Object):
	ALPHABETIC = "alphabetic"
	BOTTOM = "bottom"
	MIDDLE = "middle"
	HANGING = "hanging"
	TOP = "top"

	def __init__(self):
		raise Exception("TextFormatBaseline cannot be instantiated.")


class TextFormatWeight(Object):
	NORMAL = "normal"
	BOLD = "bold"
	BOLDER = "bolder"
	LIGHTER = "lighter"

	def __init__(self):
		raise Exception("TextFormatWeight cannot be instantiated.")
			

class TextField(DisplayObject):
	def __init__(self):
		super(TextField, self).__init__()

		self.text = ""
		self.font = "Arial"
		self.size = 15
		self.textColor = "#000000"
		self.italic = False
		self.weight = TextFormatWeight.NORMAL
		self.textAlign = TextFormatAlign.LEFT
		self.textBaseline = TextFormatBaseline.TOP
		
	def _getOriginalWidth(self):
		font = self.__getFont()
		fontMetrics = QtGui.QFontMetrics(font)

		return fontMetrics.width(self.text)

	def _getOriginalHeight(self):
		font = self.__getFont()
		fontMetrics = QtGui.QFontMetrics(font)

		return fontMetrics.height()

	def __getFont(self):
		weight = self.weight

		if self.weight == TextFormatWeight.NORMAL:
			weight = QtGui.QFont.Normal
		elif self.weight == TextFormatWeight.BOLD:
			weight = QtGui.QFont.Bold
		elif self.weight == TextFormatWeight.BOLDER:
			weight = QtGui.QFont.Black
		elif self.weight == TextFormatWeight.LIGHTER:
			weight = QtGui.QFont.Light

		font = QtGui.QFont()
		font.setFamily(self.font)
		font.setPixelSize(self.size)
		font.setWeight(weight)
		font.setItalic(self.italic)

		return font

	def __getTextStartX(self):
		if self.textAlign == TextFormatAlign.END or self.textAlign == TextFormatAlign.RIGHT:
			return -self.width
		elif self.textAlign == TextFormatAlign.CENTER:
			return -self.width / 2
		else:
			return 0

	def __getTextStartY(self):
		if self.textBaseline == TextFormatBaseline.ALPHABETIC or self.textBaseline == TextFormatBaseline.MIDDLE:
			return -self.height
		elif self.textBaseline == TextFormatBaseline.MIDDLE:
			return -self.height / 2
		else:
			return 0

	def _loopDraw(self, c):
		font = self.__getFont()
		flags = QtCore.Qt.AlignCenter
		startX = self.__getTextStartX()
		startY = self.__getTextStartY()

		c.setFont(font)
		c.setPen(getColor(self.textColor))
		c.drawText(startX, startY, self.width, self.height, flags, self.text)