#!/usr/bin/env python3
"""
Windows 10 System-Accurate Theme Configuration for Hub4com GUI
Complete revised version with all enhancements
Matches exact Windows 10 system conventions for all UI elements
Based on official Microsoft design specifications and system measurements
"""

from PyQt6.QtGui import QFont, QColor, QIcon, QPixmap, QPainter
from PyQt6.QtCore import QSize, QRect, Qt
from PyQt6.QtSvg import QSvgRenderer
from PyQt6.QtWidgets import (QPushButton, QComboBox, QGroupBox, QTextEdit, 
                             QLineEdit, QCheckBox, QLabel, QListWidget, 
                             QProgressBar, QWidget, QTableWidget, QFrame,
                             QScrollArea, QDialog)
from dataclasses import dataclass
from typing import Dict, Any, Optional, Callable
import math
from .icons.icons import AppIcons

@dataclass
class AppColors:
    """Exact Windows 10 system color palette from registry and theme specifications"""
    
    # === PRIMARY WINDOWS 10 SYSTEM COLORS ===
    # Background colors (from Windows 10 registry defaults)
    BACKGROUND_LIGHT = "#f0f0f0"        # ButtonFace - Light gray (240, 240, 240)
    BACKGROUND_WHITE = "#ffffff"        # Window - Pure white (255, 255, 255)
    BACKGROUND_DISABLED = "#f4f7fc"     # InactiveBorder - Disabled background (244, 247, 252)
    BACKGROUND_DESKTOP = "#0063b1"      # Background - Desktop background (0, 99, 177)
    BACKGROUND_MENU = "#f0f0f0"         # Menu - Menu background (240, 240, 240)
    BACKGROUND_TOOLTIP = "#ffffe1"      # InfoWindow - Tooltip background (255, 255, 225)
    BACKGROUND_APPWORKSPACE = "#ababab" # AppWorkspace - MDI background (171, 171, 171)
    
    # Border colors (from Windows 10 system colors)
    BORDER_DEFAULT = "#a0a0a0"          # ButtonShadow - Default border (160, 160, 160)
    BORDER_FOCUS = "#0078d7"            # Windows 10 accent blue (0, 120, 215)
    BORDER_PRESSED = "#005a9e"          # Darker blue for pressed state
    BORDER_DISABLED = "#d0d0d0"         # Lighter gray for disabled
    BORDER_LIGHT = "#e3e3e3"            # ButtonLight - Light border (227, 227, 227)
    BORDER_DARK_SHADOW = "#696969"      # ButtonDkShadow - Dark shadow (105, 105, 105)
    BORDER_ACTIVE = "#b4b4b4"           # ActiveBorder - Active window border (180, 180, 180)
    BORDER_INACTIVE = "#f4f7fc"         # InactiveBorder - Inactive window border (244, 247, 252)
    BORDER_WINDOW_FRAME = "#646464"     # WindowFrame - Window frame (100, 100, 100)
    
    # Button colors (Windows 10 button system)
    BUTTON_DEFAULT = "#f0f0f0"          # ButtonFace - Default button (240, 240, 240)
    BUTTON_HOVER = "#e5f1fb"            # Light blue hover (derived from accent)
    BUTTON_PRESSED = "#cce4f7"          # Pressed blue (derived from accent)
    BUTTON_HIGHLIGHT = "#ffffff"        # ButtonHilight - Button highlight (255, 255, 255)
    BUTTON_SHADOW = "#a0a0a0"           # ButtonShadow - Button shadow (160, 160, 160)
    
    # Text colors (Windows 10 text system)
    TEXT_DEFAULT = "#000000"            # WindowText/ButtonText - Black text (0, 0, 0)
    TEXT_DISABLED = "#6d6d6d"           # GrayText - Disabled text (109, 109, 109)
    TEXT_WHITE = "#ffffff"              # HilightText - White text (255, 255, 255)
    TEXT_CAPTION = "#000000"            # TitleText - Caption text (0, 0, 0)
    TEXT_INACTIVE_CAPTION = "#000000"   # InactiveTitleText - Inactive caption (0, 0, 0)
    TEXT_MENU = "#000000"               # MenuText - Menu text (0, 0, 0)
    TEXT_TOOLTIP = "#000000"            # InfoText - Tooltip text (0, 0, 0)
    
    # Icon colors (based on Windows 10 system)
    ICON_DEFAULT = "#000000"            # Default icon color
    ICON_HOVER = "#0078d7"              # Windows 10 accent blue
    ICON_PRESSED = "#005a9e"            # Darker blue for pressed
    ICON_DISABLED = "#6d6d6d"           # Matches disabled text
    
    # Selection colors (Windows 10 selection system)
    SELECTION_BG = "#3399ff"            # Hilight - Selection background (51, 153, 255)
    SELECTION_TEXT = "#ffffff"          # HilightText - Selection text (255, 255, 255)
    SELECTION_MENU = "#3399ff"          # MenuHilight - Menu selection (51, 153, 255)
    
    # Windows 10 Accent Colors (official Microsoft palette)
    ACCENT_BLUE = "#0078d7"             # Default Windows 10 accent (0, 120, 215)
    ACCENT_BLUE_DARK = "#002050"        # Dark blue (0, 32, 80)
    ACCENT_GREEN = "#107c10"            # Green accent (16, 124, 16)
    ACCENT_ORANGE = "#d83b01"           # Orange accent (216, 59, 1)
    ACCENT_RED = "#e81123"              # Red accent (232, 17, 35)
    ACCENT_PURPLE = "#5c2d91"           # Purple accent (92, 45, 145)
    ACCENT_MAGENTA = "#b4009e"          # Magenta accent (180, 0, 158)
    ACCENT_YELLOW = "#ffb900"           # Yellow accent (255, 185, 0)
    ACCENT_TEAL = "#008272"             # Teal accent (0, 130, 114)
    
    # Title bar colors (Windows 10 gradient system)
    TITLEBAR_ACTIVE = "#99b4d1"         # ActiveTitle - Active title (153, 180, 209)
    TITLEBAR_INACTIVE = "#bfcddb"       # InactiveTitle - Inactive title (191, 205, 219)
    TITLEBAR_GRADIENT_ACTIVE = "#b9d1ea"    # GradientActiveTitle (185, 209, 234)
    TITLEBAR_GRADIENT_INACTIVE = "#d7e4f2"  # GradientInactiveTitle (215, 228, 242)
    
    # Scrollbar colors
    SCROLLBAR_BACKGROUND = "#c8c8c8"    # Scrollbar - Scrollbar background (200, 200, 200)
    
    # Hot tracking (hover) color
    HOT_TRACKING = "#0066cc"            # HotTrackingColor - Hot tracking (0, 102, 204)
    
    # === SEMANTIC COLORS (Windows 10 Style) ===
    # Success colors
    SUCCESS_PRIMARY = "#107c10"         # Windows 10 green
    SUCCESS_BACKGROUND = "#dff6dd"      # Light green background
    SUCCESS_BORDER = "#0e5a0e"          # Dark green border
    
    # Warning colors
    WARNING_PRIMARY = "#ffb900"         # Windows 10 yellow
    WARNING_BACKGROUND = "#fff4ce"      # Light yellow background
    WARNING_BORDER = "#d39400"          # Dark yellow border
    
    # Error colors
    ERROR_PRIMARY = "#e81123"           # Windows 10 red
    ERROR_BACKGROUND = "#fde7e9"        # Light red background
    ERROR_BORDER = "#b4161c"            # Dark red border
    
    # Info colors
    INFO_PRIMARY = "#0078d7"            # Windows 10 blue
    INFO_BACKGROUND = "#e5f1fb"         # Light blue background
    INFO_BORDER = "#005a9e"             # Dark blue border
    
    # === SPECIAL APPLICATION COLORS ===
    # Port pair highlighting (keeping your existing functionality)
    PAIR_HIGHLIGHT = "#f0f8ff"          # Light blue for pairs with features
    PAIR_INFO = "#fffff8"               # Cream for info items
    
    # Progressive colors for advanced theming
    GRAY_50 = "#fafafa"                 # Lightest gray
    GRAY_100 = "#f5f5f5"                # Very light gray
    GRAY_200 = "#eeeeee"                # Light gray
    GRAY_300 = "#e0e0e0"                # Medium light gray
    GRAY_400 = "#bdbdbd"                # Medium gray
    GRAY_500 = "#9e9e9e"                # True gray
    GRAY_600 = "#757575"                # Medium dark gray
    GRAY_700 = "#616161"                # Dark gray
    GRAY_800 = "#424242"                # Very dark gray
    GRAY_900 = "#212121"                # Darkest gray
    
    # High contrast mode colors (Windows accessibility)
    HIGH_CONTRAST_BACKGROUND = "#000000"
    HIGH_CONTRAST_TEXT = "#ffffff"
    HIGH_CONTRAST_BORDER = "#ffffff"
    HIGH_CONTRAST_BUTTON = "#000000"
    HIGH_CONTRAST_BUTTON_TEXT = "#ffffff"


@dataclass
class AppFonts:
    """Windows 10 system fonts - exact specifications"""
    # Windows 10 uses Segoe UI as the primary system font
    HEADER = QFont("Segoe UI", 14, QFont.Weight.Bold)
    CONSOLE = QFont("Consolas", 9)
    CONSOLE_LARGE = QFont("Consolas", 10)
    DEFAULT_FAMILY = "Segoe UI"
    DEFAULT_SIZE = "9pt"      # Standard Windows 10 size
    SMALL_SIZE = "8pt"
    CAPTION_SIZE = "11pt"     # Windows 10 caption font size
    
    # Additional font specifications
    BOLD_WEIGHT = "bold"
    NORMAL_WEIGHT = "normal"
    ITALIC_STYLE = "italic"


@dataclass 
class AppDimensions:
    """Exact Windows 10 system dimensions based on Microsoft specifications"""
    
    # === BUTTON DIMENSIONS (Based on Windows UX Guidelines) ===
    # Standard button: 73x21 pixels (75x23 with 1px invisible border)
    BUTTON_WIDTH_STANDARD = 75          # Standard button width
    BUTTON_HEIGHT_STANDARD = 23         # Standard button height (with border)
    BUTTON_HEIGHT_SMALL = 21            # Small button height
    BUTTON_HEIGHT_MEDIUM = 23           # Medium button height (standard)
    BUTTON_HEIGHT_LARGE = 28            # Large button height
    
    # === CHECKBOX DIMENSIONS (Windows 10 specifications) ===
    # Windows 10 checkbox: 20x20 pixels at 100% DPI, 18x18 for modern UI
    CHECKBOX_SIZE_STANDARD = 18         # Modern UI checkbox size
    CHECKBOX_SIZE_SYSTEM = 20           # System checkbox size (100% DPI)
    CHECKBOX_BORDER_WIDTH = 1           # Checkbox border width
    
    # === COMBOBOX DIMENSIONS ===
    COMBOBOX_HEIGHT = 23                # Standard combobox height
    COMBOBOX_ARROW_WIDTH = 16           # Width of dropdown arrow area
    COMBOBOX_ARROW_SIZE = 8             # Actual arrow glyph size
    COMBOBOX_MIN_WIDTH = 120            # Minimum combobox width
    
    # === ICON DIMENSIONS ===
    # Based on Windows 10 icon sizes (16x16, 20x20, 24x24, 32x32)
    ICON_SIZE_SMALL = 16
    ICON_SIZE_MEDIUM = 20
    ICON_SIZE_LARGE = 24
    ICON_SIZE_XLARGE = 32
    
    # === SPACING (Based on 4px grid system) ===
    SPACING_TINY = 2
    SPACING_SMALL = 4
    SPACING_MEDIUM = 6
    SPACING_LARGE = 8
    SPACING_XLARGE = 12
    SPACING_XXLARGE = 16
    
    # === MARGINS (Windows 10 dialog standards) ===
    MARGIN_DIALOG = (11, 11, 11, 11)   # Standard dialog margins
    MARGIN_CONTROL = (7, 7, 7, 7)      # Control spacing margins
    MARGIN_SMALL = (4, 4, 4, 4)        # Small margins
    MARGIN_NONE = (0, 0, 0, 0)         # No margins
    
    # === PADDING VALUES ===
    PADDING_TINY = "1px"
    PADDING_SMALL = "3px"
    PADDING_MEDIUM = "5px"
    PADDING_LARGE = "7px"
    PADDING_BUTTON_STANDARD = "3px 8px"        # Standard button padding
    PADDING_BUTTON_LARGE = "5px 12px"          # Large button padding
    PADDING_BUTTON_COMPACT = "2px 6px"         # Compact button padding
    
    # === WIDGET HEIGHTS ===
    HEIGHT_TEXT_SMALL = 100
    HEIGHT_TEXT_MEDIUM = 120
    HEIGHT_TEXT_LARGE = 180
    HEIGHT_TEXT_XLARGE = 200
    HEIGHT_LIST_MEDIUM = 150
    HEIGHT_LIST_LARGE = 180
    HEIGHT_PROGRESS = 20
    HEIGHT_SEPARATOR = 1                # Height of horizontal separators
    
    # === WIDGET WIDTHS ===
    WIDTH_LABEL_PORT = 55               # Fixed width for port labels
    WIDTH_BAUD_COMBO = 100              # Fixed width for baud rate combos
    WIDTH_BUTTON_QUICK_BAUD = 50        # Quick baud rate button width
    WIDTH_BUTTON_ICON_CONTAINER = 28    # Icon button container width
    
    # === WIDGET MINIMUMS ===
    MIN_DIALOG_WIDTH = 500
    MIN_DIALOG_HEIGHT = 300
    
    # === BORDER SPECIFICATIONS ===
    BORDER_WIDTH_STANDARD = 1          # Standard 1px border
    BORDER_WIDTH_THICK = 2             # Thick border for focus
    BORDER_RADIUS_STANDARD = 0         # Windows 10 uses square corners
    BORDER_RADIUS_MODERN = 2           # Modern slight rounding
    
    # === FOCUS RECTANGLE ===
    FOCUS_RECT_WIDTH = 1               # Focus rectangle line width
    FOCUS_RECT_OFFSET = 2              # Focus rectangle offset from control
    
    # === OUTPUT PORT WIDGET SPECIFICS ===
    OUTPUT_PORT_MIN_COUNT = 1          # Minimum number of output ports


class AppMessages:
    """Centralized messages for consistency"""
    READY = "Ready"
    SCANNING = "Scanning for serial ports..."
    NO_DEVICES = "No COM devices detected"
    NO_DEVICES_FULL = "No COM devices detected. Please connect equipment and refresh."
    PORT_PAIR_CREATED = "Virtual COM port pair created successfully"
    PORT_PAIR_REMOVED = "Virtual COM port pair removed successfully"
    HUBCOM_RUNNING = "Hub4com routing service is active - Data routing operational"
    HUBCOM_STOPPED = "Hub4com routing service stopped"
    ERROR_OCCURRED = "Error occurred"
    LISTING_PAIRS = "Checking virtual COM port pairs..."
    CREATING_PAIR = "Creating virtual COM port pair..."
    REMOVING_PAIR = "Removing virtual COM port pair..."
    STARTING_HUBCOM = "Starting hub4com routing service..."
    STOPPING_HUBCOM = "Stopping hub4com routing service..."
    
    # Tooltips
    PAIR_TOOLTIP_TEMPLATE = """Port A ({port_a}): {params_a}
Port B ({port_b}): {params_b}

Right-click or use 'Configure Features' to modify settings
Click 'Help' button for detailed explanations of all features"""
    
    # Button labels
    BUTTON_ROUTE_MODE = "Route Mode: {mode} ▼"
    BUTTON_PORT_LABEL = "Port {number}:"
    BUTTON_SET_ALL = "Set All:"
    
    # Port type indicators
    PORT_TYPE_MOXA = "🌐 MOXA Network Device - Make sure baud rate matches your source device"
    PORT_TYPE_PHYSICAL = "🔌 PHYSICAL PORT - Connected to real hardware, verify device baud rate"
    PORT_TYPE_VIRTUAL = "💻 VIRTUAL PORT - Software-created port for inter-application communication"


class AppStyles:
    """Exact Windows 10 system stylesheets matching native controls"""
    
    @staticmethod
    def button(style_variant: str = "default") -> str:
        """Windows 10 system button - exact match to native controls"""
        base_style = f"""
        QPushButton {{
            background-color: {AppColors.BUTTON_DEFAULT};
            color: {AppColors.TEXT_DEFAULT};
            padding: {AppDimensions.PADDING_BUTTON_STANDARD};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-width: {AppDimensions.BUTTON_WIDTH_STANDARD}px;
            min-height: {AppDimensions.BUTTON_HEIGHT_STANDARD}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QPushButton:hover {{
            background-color: {AppColors.BUTTON_HOVER};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
        }}
        QPushButton:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_PRESSED};
        }}
        QPushButton:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QPushButton:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        """
        
        # Add variant-specific styles
        if style_variant == "primary":
            base_style += f"""
            QPushButton {{
                background-color: {AppColors.ACCENT_BLUE};
                color: {AppColors.TEXT_WHITE};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.ACCENT_BLUE};
            }}
            QPushButton:hover {{
                background-color: {AppColors.HOT_TRACKING};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.HOT_TRACKING};
            }}
            QPushButton:pressed {{
                background-color: {AppColors.BORDER_PRESSED};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_PRESSED};
            }}
            """
        elif style_variant == "success":
            base_style += f"""
            QPushButton {{
                background-color: {AppColors.SUCCESS_PRIMARY};
                color: {AppColors.TEXT_WHITE};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.SUCCESS_BORDER};
            }}
            QPushButton:hover {{
                background-color: {AppColors.SUCCESS_BORDER};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.SUCCESS_BORDER};
            }}
            """
        elif style_variant == "danger":
            base_style += f"""
            QPushButton {{
                background-color: {AppColors.ERROR_PRIMARY};
                color: {AppColors.TEXT_WHITE};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.ERROR_BORDER};
            }}
            QPushButton:hover {{
                background-color: {AppColors.ERROR_BORDER};
                border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.ERROR_BORDER};
            }}
            """
            
        return base_style
    
    @staticmethod
    def button_large() -> str:
        """Large button for primary actions"""
        return f"""
        QPushButton {{
            background-color: {AppColors.BUTTON_DEFAULT};
            color: {AppColors.TEXT_DEFAULT};
            padding: {AppDimensions.PADDING_BUTTON_LARGE};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-width: {AppDimensions.BUTTON_WIDTH_STANDARD + 20}px;
            min-height: {AppDimensions.BUTTON_HEIGHT_LARGE}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QPushButton:hover {{
            background-color: {AppColors.BUTTON_HOVER};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
        }}
        QPushButton:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_PRESSED};
        }}
        QPushButton:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QPushButton:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def button_compact() -> str:
        """Compact button for toolbars and space-constrained areas"""
        return f"""
        QPushButton {{
            background-color: {AppColors.BUTTON_DEFAULT};
            color: {AppColors.TEXT_DEFAULT};
            padding: {AppDimensions.PADDING_BUTTON_COMPACT};
            font-size: {AppFonts.SMALL_SIZE};
            min-height: {AppDimensions.BUTTON_HEIGHT_SMALL}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QPushButton:hover {{
            background-color: {AppColors.BUTTON_HOVER};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
        }}
        QPushButton:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_PRESSED};
        }}
        QPushButton:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QPushButton:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def icon_button() -> str:
        """Icon-only button matching Windows 10 toolbar buttons"""
        return f"""
        QPushButton {{
            background-color: transparent;
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid transparent;
            padding: {AppDimensions.PADDING_SMALL};
            color: {AppColors.TEXT_DEFAULT};
            min-width: {AppDimensions.ICON_SIZE_MEDIUM + 8}px;
            min-height: {AppDimensions.ICON_SIZE_MEDIUM + 8}px;
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN}px;
        }}
        QPushButton:hover {{
            background-color: {AppColors.INFO_BACKGROUND};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_LIGHT};
        }}
        QPushButton:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
        }}
        QPushButton:focus {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QPushButton:disabled {{
            color: {AppColors.ICON_DISABLED};
            background-color: transparent;
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid transparent;
        }}
        """
    
    @staticmethod
    def combobox() -> str:
        """Windows 10 system combobox - exact native styling"""
        return f"""
        QComboBox {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            padding: {AppDimensions.PADDING_SMALL} {AppDimensions.COMBOBOX_ARROW_WIDTH + 4}px {AppDimensions.PADDING_SMALL} {AppDimensions.PADDING_SMALL};
            background-color: {AppColors.BACKGROUND_WHITE};
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-height: {AppDimensions.COMBOBOX_HEIGHT}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QComboBox:hover {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
            background-color: {AppColors.BACKGROUND_WHITE};
        }}
        QComboBox:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            background-color: {AppColors.BACKGROUND_WHITE};
            outline: none;
        }}
        QComboBox:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        QComboBox::drop-down {{
            border: none;
            width: {AppDimensions.COMBOBOX_ARROW_WIDTH}px;
            background-color: transparent;
        }}
        QComboBox::drop-down:hover {{
            background-color: rgba(0, 120, 215, 0.1);
        }}
        QComboBox::down-arrow {{
            width: {AppDimensions.COMBOBOX_ARROW_SIZE}px;
            height: {AppDimensions.COMBOBOX_ARROW_SIZE}px;
            image: none;
            border: none;
        }}
        QComboBox::down-arrow:on {{
            /* Arrow when dropdown is open */
            top: 1px;
        }}
        QComboBox QAbstractItemView {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            background-color: {AppColors.BACKGROUND_WHITE};
            selection-background-color: {AppColors.SELECTION_BG};
            selection-color: {AppColors.SELECTION_TEXT};
            outline: none;
        }}
        QComboBox QAbstractItemView::item {{
            min-height: 20px;
            padding: 2px 4px;
        }}
        QComboBox QAbstractItemView::item:hover {{
            background-color: {AppColors.BUTTON_HOVER};
        }}
        """
    
    @staticmethod
    def checkbox() -> str:
        """Windows 10 system checkbox - exact native appearance"""
        return f"""
        QCheckBox {{
            color: {AppColors.TEXT_DEFAULT};
            spacing: {AppDimensions.SPACING_MEDIUM}px;
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        QCheckBox:disabled {{
            color: {AppColors.TEXT_DISABLED};
        }}
        QCheckBox::indicator {{
            width: {AppDimensions.CHECKBOX_SIZE_STANDARD}px;
            height: {AppDimensions.CHECKBOX_SIZE_STANDARD}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QCheckBox::indicator:unchecked {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_DEFAULT};
            background-color: {AppColors.BACKGROUND_WHITE};
        }}
        QCheckBox::indicator:unchecked:hover {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_FOCUS};
            background-color: {AppColors.BUTTON_HOVER};
        }}
        QCheckBox::indicator:unchecked:pressed {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_PRESSED};
            background-color: {AppColors.BUTTON_PRESSED};
        }}
        QCheckBox::indicator:checked {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.ACCENT_BLUE};
            background-color: {AppColors.ACCENT_BLUE};
            image: none;
        }}
        QCheckBox::indicator:checked:hover {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.HOT_TRACKING};
            background-color: {AppColors.HOT_TRACKING};
        }}
        QCheckBox::indicator:checked:pressed {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_PRESSED};
            background-color: {AppColors.BORDER_PRESSED};
        }}
        QCheckBox::indicator:indeterminate {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.ACCENT_BLUE};
            background-color: {AppColors.ACCENT_BLUE};
        }}
        QCheckBox::indicator:disabled {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_DISABLED};
            background-color: {AppColors.BACKGROUND_DISABLED};
        }}
        QCheckBox::indicator:checked:disabled {{
            border: {AppDimensions.CHECKBOX_BORDER_WIDTH}px solid {AppColors.BORDER_DISABLED};
            background-color: {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def groupbox() -> str:
        """Windows 10 system groupbox"""
        return f"""
        QGroupBox {{
            font-weight: normal;
            color: {AppColors.TEXT_DEFAULT};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            margin-top: {AppDimensions.SPACING_LARGE}px;
            padding-top: {AppDimensions.SPACING_MEDIUM}px;
            background-color: {AppColors.BACKGROUND_LIGHT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QGroupBox::title {{
            subcontrol-origin: margin;
            left: {AppDimensions.SPACING_LARGE}px;
            padding: 0 {AppDimensions.SPACING_MEDIUM}px;
            background-color: {AppColors.BACKGROUND_LIGHT};
            color: {AppColors.TEXT_DEFAULT};
        }}
        """
    
    @staticmethod
    def textedit() -> str:
        """Windows 10 system text edit"""
        return f"""
        QTextEdit {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            padding: {AppDimensions.PADDING_SMALL};
            background-color: {AppColors.BACKGROUND_WHITE};
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
            selection-background-color: {AppColors.SELECTION_BG};
            selection-color: {AppColors.SELECTION_TEXT};
        }}
        QTextEdit:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QTextEdit:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def lineedit() -> str:
        """Windows 10 system line edit"""
        return f"""
        QLineEdit {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            padding: {AppDimensions.PADDING_SMALL};
            background-color: {AppColors.BACKGROUND_WHITE};
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-height: {AppDimensions.BUTTON_HEIGHT_SMALL}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
            selection-background-color: {AppColors.SELECTION_BG};
            selection-color: {AppColors.SELECTION_TEXT};
        }}
        QLineEdit:hover {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_FOCUS};
        }}
        QLineEdit:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
            outline: none;
        }}
        QLineEdit:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            color: {AppColors.TEXT_DISABLED};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def label() -> str:
        """Standard label"""
        return f"""
        QLabel {{
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        """
    
    @staticmethod
    def label_status() -> str:
        """Status label with Windows 10 styling"""
        return f"""
        QLabel {{
            color: {AppColors.TEXT_DEFAULT};
            padding: {AppDimensions.PADDING_SMALL} {AppDimensions.PADDING_LARGE};
            background-color: {AppColors.BACKGROUND_LIGHT};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-height: {AppDimensions.BUTTON_HEIGHT_MEDIUM}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        """
    
    @staticmethod
    def listwidget() -> str:
        """Windows 10 system list widget"""
        return f"""
        QListWidget {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            background-color: {AppColors.BACKGROUND_WHITE};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            padding: {AppDimensions.SPACING_TINY}px;
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
            outline: none;
        }}
        QListWidget::item {{
            border-bottom: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_LIGHT};
            padding: {AppDimensions.PADDING_SMALL};
            margin: 1px 0px;
            color: {AppColors.TEXT_DEFAULT};
            min-height: 18px;
        }}
        QListWidget::item:selected {{
            background-color: {AppColors.SELECTION_BG};
            color: {AppColors.SELECTION_TEXT};
        }}
        QListWidget::item:hover {{
            background-color: {AppColors.BUTTON_HOVER};
        }}
        QListWidget:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
        }}
        """
    
    @staticmethod
    def tablewidget() -> str:
        """Windows 10 system table widget"""
        return f"""
        QTableWidget {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            background-color: {AppColors.BACKGROUND_WHITE};
            color: {AppColors.TEXT_DEFAULT};
            gridline-color: {AppColors.BORDER_LIGHT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
            outline: none;
        }}
        QTableWidget::item {{
            padding: {AppDimensions.PADDING_SMALL};
            border: none;
        }}
        QTableWidget::item:selected {{
            background-color: {AppColors.SELECTION_BG};
            color: {AppColors.SELECTION_TEXT};
        }}
        QTableWidget::item:hover {{
            background-color: {AppColors.BUTTON_HOVER};
        }}
        QHeaderView::section {{
            background-color: {AppColors.BACKGROUND_LIGHT};
            color: {AppColors.TEXT_DEFAULT};
            padding: {AppDimensions.PADDING_SMALL};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-weight: bold;
        }}
        QTableWidget:focus {{
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
        }}
        """
    
    @staticmethod
    def progress_bar() -> str:
        """Windows 10 system progress bar"""
        return f"""
        QProgressBar {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN}px;
            text-align: center;
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            min-height: {AppDimensions.HEIGHT_PROGRESS}px;
            background-color: {AppColors.BACKGROUND_LIGHT};
        }}
        QProgressBar::chunk {{
            background-color: {AppColors.ACCENT_BLUE};
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN - 1}px;
        }}
        """
    
    @staticmethod
    def scroll_area() -> str:
        """Windows 10 system scroll area"""
        return f"""
        QScrollArea {{
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            background-color: {AppColors.BACKGROUND_WHITE};
            border-radius: {AppDimensions.BORDER_RADIUS_STANDARD}px;
        }}
        QScrollBar:vertical {{
            background-color: {AppColors.SCROLLBAR_BACKGROUND};
            width: 16px;
            border-radius: 0px;
            border: none;
        }}
        QScrollBar::handle:vertical {{
            background-color: {AppColors.BORDER_DEFAULT};
            border-radius: 0px;
            min-height: 20px;
        }}
        QScrollBar::handle:vertical:hover {{
            background-color: {AppColors.BORDER_FOCUS};
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
        }}
        """
    
    @staticmethod
    def tooltip() -> str:
        """Windows 10 system tooltip"""
        return f"""
        QToolTip {{
            background-color: {AppColors.BACKGROUND_TOOLTIP};
            color: {AppColors.TEXT_TOOLTIP};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            padding: {AppDimensions.PADDING_MEDIUM};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN}px;
        }}
        """
    
    @staticmethod
    def notification(notification_type: str = "info") -> str:
        """Windows 10 notification panel styles"""
        type_colors = {
            "success": (AppColors.SUCCESS_BACKGROUND, AppColors.SUCCESS_BORDER, AppColors.SUCCESS_PRIMARY),
            "warning": (AppColors.WARNING_BACKGROUND, AppColors.WARNING_BORDER, AppColors.WARNING_PRIMARY),
            "error": (AppColors.ERROR_BACKGROUND, AppColors.ERROR_BORDER, AppColors.ERROR_PRIMARY),
            "info": (AppColors.INFO_BACKGROUND, AppColors.INFO_BORDER, AppColors.INFO_PRIMARY)
        }
        
        bg_color, border_color, text_color = type_colors.get(notification_type, type_colors["info"])
        
        return f"""
        QLabel {{
            background-color: {bg_color};
            color: {text_color};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {border_color};
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN}px;
            padding: {AppDimensions.PADDING_MEDIUM};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        """
    
    @staticmethod
    def separator(orientation: str = "horizontal") -> str:
        """Windows 10 separator line style"""
        if orientation == "horizontal":
            return f"""
            QFrame {{
                color: {AppColors.BORDER_LIGHT};
                background-color: {AppColors.BORDER_LIGHT};
                max-height: {AppDimensions.HEIGHT_SEPARATOR}px;
            }}
            """
        else:  # vertical
            return f"""
            QFrame {{
                color: {AppColors.BORDER_DEFAULT};
                background-color: {AppColors.BORDER_DEFAULT};
                max-width: {AppDimensions.BORDER_WIDTH_STANDARD}px;
                margin: {AppDimensions.PADDING_SMALL} {AppDimensions.PADDING_MEDIUM};
            }}
            """
    
    @staticmethod
    def status_label_inline() -> str:
        """Inline status label style for section headers"""
        return f"""
        QLabel {{
            color: {AppColors.TEXT_DISABLED};
            font-style: {AppFonts.ITALIC_STYLE};
            margin-left: {AppDimensions.PADDING_MEDIUM};
        }}
        """
    
    @staticmethod
    def port_label() -> str:
        """Port number label style"""
        return f"""
        QLabel {{
            font-weight: {AppFonts.BOLD_WEIGHT};
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        """
    
    @staticmethod
    def output_port_widget() -> str:
        """Output port widget container style"""
        return f"""
        OutputPortWidget {{
            background-color: {AppColors.BACKGROUND_WHITE};
            padding: {AppDimensions.PADDING_MEDIUM};
            margin-bottom: {AppDimensions.SPACING_SMALL}px;
        }}
        OutputPortWidget:hover {{
            background-color: {AppColors.BUTTON_HOVER};
        }}
        """
    
    @staticmethod
    def output_port_widget_pressed() -> str:
        """Output port widget pressed state"""
        return f"""
        OutputPortWidget {{
            background-color: {AppColors.BUTTON_PRESSED};
            border: {AppDimensions.BORDER_WIDTH_THICK}px solid {AppColors.BORDER_FOCUS};
        }}
        """
    
    @staticmethod
    def output_port_widget_disabled() -> str:
        """Output port widget disabled state"""
        return f"""
        OutputPortWidget:disabled {{
            background-color: {AppColors.BACKGROUND_DISABLED};
            border-color: {AppColors.BORDER_DISABLED};
        }}
        """
    
    @staticmethod
    def port_type_indicator(style_type: str = "info") -> str:
        """Port type indicator label style"""
        from .theme import ThemeManager  # Local import to avoid circular dependency
        bg_color = ThemeManager.get_semantic_color(style_type, "background")
        border_color = ThemeManager.get_semantic_color(style_type, "border")
        text_color = ThemeManager.get_semantic_color(style_type, "primary")
        
        return f"""
        QLabel {{
            color: {text_color};
            font-style: {AppFonts.ITALIC_STYLE};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.SMALL_SIZE};
            padding: {AppDimensions.PADDING_SMALL} {AppDimensions.PADDING_MEDIUM};
            background-color: {bg_color};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {border_color};
            border-radius: {AppDimensions.BORDER_RADIUS_MODERN}px;
            margin-top: {AppDimensions.SPACING_SMALL}px;
        }}
        """
    
    @staticmethod
    def baud_label() -> str:
        """Baud rate label style"""
        return f"""
        QLabel {{
            color: {AppColors.TEXT_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            margin-right: {AppDimensions.SPACING_SMALL}px;
        }}
        """
    
    @staticmethod
    def section_header_label() -> str:
        """Section header label style"""
        return f"""
        QLabel {{
            color: {AppColors.TEXT_DEFAULT};
            font-weight: {AppFonts.BOLD_WEIGHT};
            margin-right: {AppDimensions.SPACING_SMALL}px;
        }}
        """
    
    @staticmethod
    def icon_button_hover_danger() -> str:
        """Icon button with danger hover effect"""
        base = AppStyles.icon_button()
        return base + f"""
        QPushButton:hover {{
            background-color: {AppColors.ERROR_BACKGROUND};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.ERROR_BORDER};
        }}
        """
    
    @staticmethod
    def splitter() -> str:
        """Splitter widget style"""
        return f"""
        QSplitter::handle {{
            background-color: {AppColors.BORDER_LIGHT};
            width: {AppDimensions.SPACING_SMALL}px;
            height: {AppDimensions.SPACING_SMALL}px;
        }}
        QSplitter::handle:hover {{
            background-color: {AppColors.BORDER_FOCUS};
        }}
        """


class IconManager:
    """Enhanced icon manager with Windows 10 system icon support"""
    
    @staticmethod
    def get_scaled_size(base_size: int, scale_factor: float = 1.0) -> QSize:
        """Calculate scaled icon size based on Windows 10 DPI scaling"""
        from PyQt6.QtWidgets import QApplication
        
        # Get screen DPI scaling if application exists
        if QApplication.instance():
            screen = QApplication.primaryScreen()
            if screen:
                dpi_ratio = screen.devicePixelRatio()
                scale_factor *= dpi_ratio
        
        scaled_size = int(base_size * scale_factor)
        return QSize(scaled_size, scaled_size)
    
    @staticmethod
    def create_svg_icon(svg_template: str, color: str, size: QSize) -> QIcon:
        """Create a QIcon from SVG template with Windows 10 native icon states"""
        # Replace color placeholder in SVG
        svg_data = svg_template.format(color=color)
        
        # Create QIcon with multiple states
        icon = QIcon()
        
        # Normal state
        normal_pixmap = IconManager._svg_to_pixmap(svg_data, size)
        icon.addPixmap(normal_pixmap, QIcon.Mode.Normal, QIcon.State.Off)
        
        # Hover state
        hover_svg = svg_template.format(color=AppColors.ICON_HOVER)
        hover_pixmap = IconManager._svg_to_pixmap(hover_svg, size)
        icon.addPixmap(hover_pixmap, QIcon.Mode.Active, QIcon.State.Off)
        
        # Pressed state
        pressed_svg = svg_template.format(color=AppColors.ICON_PRESSED)
        pressed_pixmap = IconManager._svg_to_pixmap(pressed_svg, size)
        icon.addPixmap(pressed_pixmap, QIcon.Mode.Selected, QIcon.State.Off)
        
        # Disabled state
        disabled_svg = svg_template.format(color=AppColors.ICON_DISABLED)
        disabled_pixmap = IconManager._svg_to_pixmap(disabled_svg, size)
        icon.addPixmap(disabled_pixmap, QIcon.Mode.Disabled, QIcon.State.Off)
        
        return icon
    
    @staticmethod
    def create_combobox_arrow_icon(size: QSize) -> QIcon:
        """Create Windows 10 system combobox dropdown arrow"""
        return IconManager.create_svg_icon(AppIcons.DROPDOWN_ARROW, AppColors.ICON_DEFAULT, size)
    
    @staticmethod
    def create_checkbox_check_icon(size: QSize) -> QIcon:
        """Create Windows 10 system checkbox checkmark"""
        return IconManager.create_svg_icon(AppIcons.CHECKBOX_CHECK, AppColors.TEXT_WHITE, size)
    
    @staticmethod
    def _svg_to_pixmap(svg_data: str, size: QSize) -> QPixmap:
        """Convert SVG data to QPixmap"""
        renderer = QSvgRenderer()
        renderer.load(svg_data.encode('utf-8'))
        
        pixmap = QPixmap(size)
        pixmap.fill(QColor(0, 0, 0, 0))  # Transparent background
        
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return pixmap


class ThemeManager:
    """Enhanced theme manager with Windows 10 system accuracy"""
    
    # Widget factory methods with exact Windows 10 specifications
    @staticmethod
    def create_button(text: str, callback: Optional[Callable] = None, 
                     style_type: str = "standard", variant: str = "default", 
                     enabled: bool = True) -> QPushButton:
        """Create Windows 10 system-accurate button"""
        button = QPushButton(text)
        
        # Apply appropriate style based on type
        if style_type == "large":
            button.setStyleSheet(AppStyles.button_large())
        elif style_type == "compact":
            button.setStyleSheet(AppStyles.button_compact())
        elif style_type == "icon":
            button.setStyleSheet(AppStyles.icon_button())
        else:  # standard
            button.setStyleSheet(AppStyles.button(variant))
        
        button.setEnabled(enabled)
        if callback:
            button.clicked.connect(callback)
        
        return button
    
    @staticmethod
    def create_combobox(editable: bool = False) -> QComboBox:
        """Create Windows 10 system-accurate combobox"""
        combo = QComboBox()
        combo.setEditable(editable)
        combo.setStyleSheet(AppStyles.combobox())
        
        # Set minimum height to match Windows 10 system comboboxes
        combo.setMinimumHeight(AppDimensions.COMBOBOX_HEIGHT)
        
        return combo
    
    @staticmethod
    def create_checkbox(text: str) -> QCheckBox:
        """Create Windows 10 system-accurate checkbox"""
        checkbox = QCheckBox(text)
        checkbox.setStyleSheet(AppStyles.checkbox())
        return checkbox
    
    @staticmethod
    def create_groupbox(title: str) -> QGroupBox:
        """Create Windows 10 system-accurate groupbox"""
        group = QGroupBox(title)
        group.setStyleSheet(AppStyles.groupbox())
        return group
    
    @staticmethod
    def create_label(text: str, style_type: str = "standard") -> QLabel:
        """Create styled label"""
        label = QLabel(text)
        
        style_map = {
            "standard": AppStyles.label(),
            "status": AppStyles.label_status(),
        }
        label.setStyleSheet(style_map.get(style_type, AppStyles.label()))
        
        return label
    
    @staticmethod
    def create_textedit(font_type: str = "standard") -> QTextEdit:
        """Create Windows 10 system-accurate text edit"""
        textedit = QTextEdit()
        textedit.setStyleSheet(AppStyles.textedit())
        
        if font_type == "console":
            textedit.setFont(AppFonts.CONSOLE)
        elif font_type == "console_large":
            textedit.setFont(AppFonts.CONSOLE_LARGE)
        
        return textedit
    
    @staticmethod
    def create_lineedit() -> QLineEdit:
        """Create Windows 10 system-accurate line edit"""
        lineedit = QLineEdit()
        lineedit.setStyleSheet(AppStyles.lineedit())
        return lineedit
    
    @staticmethod
    def create_listwidget() -> QListWidget:
        """Create Windows 10 system-accurate list widget"""
        listwidget = QListWidget()
        listwidget.setStyleSheet(AppStyles.listwidget())
        return listwidget
    
    @staticmethod
    def create_tablewidget() -> QTableWidget:
        """Create Windows 10 system-accurate table widget"""
        tablewidget = QTableWidget()
        tablewidget.setStyleSheet(AppStyles.tablewidget())
        return tablewidget
    
    @staticmethod
    def create_progress_bar() -> QProgressBar:
        """Create Windows 10 system-accurate progress bar"""
        progress = QProgressBar()
        progress.setStyleSheet(AppStyles.progress_bar())
        return progress
    
    @staticmethod
    def create_icon_button(icon_name: str, tooltip: str = "", size: str = "medium") -> QPushButton:
        """Create Windows 10 icon button"""
        button = QPushButton()
        
        # Get base size
        size_map = {
            "small": AppDimensions.ICON_SIZE_SMALL,
            "medium": AppDimensions.ICON_SIZE_MEDIUM,
            "large": AppDimensions.ICON_SIZE_LARGE,
            "xlarge": AppDimensions.ICON_SIZE_XLARGE
        }
        base_size = size_map.get(size, AppDimensions.ICON_SIZE_MEDIUM)
        
        # Calculate scaled size
        icon_size = IconManager.get_scaled_size(base_size)
        
        # Get SVG template
        icon_template = getattr(AppIcons, icon_name.upper(), None)
        if icon_template:
            icon = IconManager.create_svg_icon(icon_template, AppColors.ICON_DEFAULT, icon_size)
            button.setIcon(icon)
            button.setIconSize(icon_size)
        
        # Apply styling
        button.setStyleSheet(AppStyles.icon_button())
        
        if tooltip:
            button.setToolTip(tooltip)
        
        return button
    
    @staticmethod
    def create_notification_label(text: str, notification_type: str = "info") -> QLabel:
        """Create Windows 10 notification label"""
        label = QLabel(text)
        label.setStyleSheet(AppStyles.notification(notification_type))
        return label
    
    @staticmethod
    def create_separator(orientation: str = "horizontal", parent: Optional[QWidget] = None) -> QFrame:
        """Create a styled separator line"""
        separator = QFrame(parent)
        if orientation == "horizontal":
            separator.setFrameShape(QFrame.Shape.HLine)
        else:
            separator.setFrameShape(QFrame.Shape.VLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet(AppStyles.separator(orientation))
        return separator
    
    @staticmethod
    def create_status_label_inline(text: str) -> QLabel:
        """Create inline status label for section headers"""
        label = QLabel(text)
        label.setStyleSheet(AppStyles.status_label_inline())
        return label
    
    @staticmethod
    def create_port_label(number: int) -> QLabel:
        """Create port number label"""
        label = QLabel(AppMessages.BUTTON_PORT_LABEL.format(number=number))
        label.setFixedWidth(AppDimensions.WIDTH_LABEL_PORT)
        label.setStyleSheet(AppStyles.port_label())
        return label
    
    @staticmethod
    def create_baud_label(text: str = "Baud:") -> QLabel:
        """Create baud rate label"""
        label = QLabel(text)
        label.setStyleSheet(AppStyles.baud_label())
        return label
    
    @staticmethod
    def create_section_header_label(text: str) -> QLabel:
        """Create section header label"""
        label = QLabel(text)
        label.setStyleSheet(AppStyles.section_header_label())
        return label
    
    @staticmethod
    def create_quick_baud_button(rate: str, callback: Callable) -> QPushButton:
        """Create quick baud rate button"""
        btn = ThemeManager.create_button(rate, lambda checked, r=rate: callback(r), "compact")
        btn.setFixedWidth(AppDimensions.WIDTH_BUTTON_QUICK_BAUD)
        btn.setToolTip(f"Set all ports to {rate} baud")
        return btn
    
    @staticmethod
    def create_port_type_indicator() -> QLabel:
        """Create port type indicator label"""
        label = QLabel("")
        label.setWordWrap(True)
        label.setStyleSheet(AppStyles.port_type_indicator())
        label.setVisible(False)
        return label
    
    @staticmethod
    def create_route_mode_button(initial_mode: str = "one_way", callback: Callable = None) -> QPushButton:
        """Create route mode dropdown button"""
        mode_names = {
            'one_way': 'One-Way',
            'two_way': 'Two-Way',
            'full_network': 'Full Network'
        }
        text = AppMessages.BUTTON_ROUTE_MODE.format(mode=mode_names.get(initial_mode, 'One-Way'))
        btn = ThemeManager.create_button(text, callback)
        btn.setToolTip("Configure data routing between ports")
        return btn
    
    @staticmethod
    def configure_scroll_area(scroll_area, max_height: Optional[int] = None):
        """Configure a scroll area with proper styling"""
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setStyleSheet(AppStyles.scroll_area())
        if max_height:
            scroll_area.setMaximumHeight(max_height)
        return scroll_area
    
    @staticmethod
    def create_splitter(orientation: Qt.Orientation = Qt.Orientation.Horizontal) -> QWidget:
        """Create a styled splitter"""
        from PyQt6.QtWidgets import QSplitter
        splitter = QSplitter(orientation)
        splitter.setChildrenCollapsible(False)
        splitter.setStyleSheet(AppStyles.splitter())
        return splitter
    
    @staticmethod
    def set_widget_margins(widget, margin_type: str = "standard"):
        """Set widget margins based on type"""
        margin_map = {
            "dialog": AppDimensions.MARGIN_DIALOG,
            "control": AppDimensions.MARGIN_CONTROL,
            "small": AppDimensions.MARGIN_SMALL,
            "none": AppDimensions.MARGIN_NONE,
            "standard": AppDimensions.MARGIN_DIALOG
        }
        margins = margin_map.get(margin_type, AppDimensions.MARGIN_DIALOG)
        if hasattr(widget, 'setContentsMargins'):
            widget.setContentsMargins(*margins)
    
    @staticmethod
    def create_dialog_window(title: str, width: Optional[int] = None, height: Optional[int] = None):
        """Create a dialog window with standard dimensions"""
        from PyQt6.QtWidgets import QDialog
        dialog = QDialog()
        dialog.setWindowTitle(title)
        dialog.setMinimumSize(
            width or AppDimensions.MIN_DIALOG_WIDTH,
            height or AppDimensions.MIN_DIALOG_HEIGHT
        )
        return dialog
    
    # Layout and sizing helpers
    @staticmethod
    def get_standard_margins() -> tuple:
        """Get Windows 10 standard dialog margins"""
        return AppDimensions.MARGIN_DIALOG
    
    @staticmethod
    def get_control_margins() -> tuple:
        """Get Windows 10 control spacing margins"""
        return AppDimensions.MARGIN_CONTROL
    
    @staticmethod
    def get_standard_spacing() -> int:
        """Get Windows 10 standard spacing"""
        return AppDimensions.SPACING_MEDIUM
    
    # Color helpers
    @staticmethod
    def get_accent_color(color_type: str) -> QColor:
        """Get Windows 10 accent colors"""
        colors = {
            'blue': AppColors.ACCENT_BLUE,
            'green': AppColors.ACCENT_GREEN,
            'orange': AppColors.ACCENT_ORANGE,
            'red': AppColors.ACCENT_RED,
            'purple': AppColors.ACCENT_PURPLE,
            'magenta': AppColors.ACCENT_MAGENTA,
            'yellow': AppColors.ACCENT_YELLOW,
            'teal': AppColors.ACCENT_TEAL,
            'pair_highlight': AppColors.PAIR_HIGHLIGHT,
            'pair_info': AppColors.PAIR_INFO
        }
        color_hex = colors.get(color_type, AppColors.ACCENT_BLUE)
        return QColor(color_hex)
    
    @staticmethod
    def get_semantic_color(semantic_type: str, element: str = "primary") -> str:
        """Get semantic colors for Windows 10 notifications"""
        color_map = {
            "success": {
                "primary": AppColors.SUCCESS_PRIMARY,
                "background": AppColors.SUCCESS_BACKGROUND,
                "border": AppColors.SUCCESS_BORDER
            },
            "warning": {
                "primary": AppColors.WARNING_PRIMARY,
                "background": AppColors.WARNING_BACKGROUND,
                "border": AppColors.WARNING_BORDER
            },
            "error": {
                "primary": AppColors.ERROR_PRIMARY,
                "background": AppColors.ERROR_BACKGROUND,
                "border": AppColors.ERROR_BORDER
            },
            "info": {
                "primary": AppColors.INFO_PRIMARY,
                "background": AppColors.INFO_BACKGROUND,
                "border": AppColors.INFO_BORDER
            }
        }
        
        return color_map.get(semantic_type, color_map["info"]).get(element, AppColors.INFO_PRIMARY)
    
    @staticmethod
    def apply_global_stylesheet(app) -> None:
        """Apply Windows 10 system-accurate global stylesheet"""
        global_style = f"""
        /* Windows 10 Global Application Styling */
        QApplication {{
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        
        /* Windows 10 Tooltips */
        {AppStyles.tooltip()}
        
        /* Windows 10 Menu Bar */
        QMenuBar {{
            background-color: {AppColors.BACKGROUND_MENU};
            color: {AppColors.TEXT_MENU};
            border-bottom: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        
        QMenuBar::item {{
            padding: 4px 8px;
            background-color: transparent;
            margin: 0px;
        }}
        
        QMenuBar::item:selected {{
            background-color: {AppColors.SELECTION_MENU};
            color: {AppColors.SELECTION_TEXT};
        }}
        
        QMenuBar::item:pressed {{
            background-color: {AppColors.BUTTON_PRESSED};
        }}
        
        /* Windows 10 Context Menus */
        QMenu {{
            background-color: {AppColors.BACKGROUND_MENU};
            color: {AppColors.TEXT_MENU};
            border: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
            padding: 2px;
        }}
        
        QMenu::item {{
            padding: 4px 16px;
            margin: 1px;
        }}
        
        QMenu::item:selected {{
            background-color: {AppColors.SELECTION_MENU};
            color: {AppColors.SELECTION_TEXT};
        }}
        
        QMenu::separator {{
            height: 1px;
            background-color: {AppColors.BORDER_LIGHT};
            margin: 2px 4px;
        }}
        
        /* Windows 10 Status Bar */
        QStatusBar {{
            background-color: {AppColors.BACKGROUND_LIGHT};
            color: {AppColors.TEXT_DEFAULT};
            border-top: {AppDimensions.BORDER_WIDTH_STANDARD}px solid {AppColors.BORDER_DEFAULT};
            font-family: {AppFonts.DEFAULT_FAMILY};
            font-size: {AppFonts.DEFAULT_SIZE};
        }}
        
        QStatusBar::item {{
            border: none;
        }}
        """
        
        app.setStyleSheet(global_style)


# Configuration constants that should be in the theme
class Config:
    """Application configuration constants using theme system"""
    BAUD_RATES = ["1200", "2400", "4800", "9600", "14400", "19200", 
                  "38400", "57600", "115200", "230400", "460800", "921600"]
    QUICK_BAUD_RATES = ["9600", "19200", "38400", "57600", "115200"]
    DEFAULT_BAUD = "115200"
    MIN_OUTPUT_PORTS = AppDimensions.OUTPUT_PORT_MIN_COUNT

