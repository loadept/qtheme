from pydantic import BaseModel


class ThemeSelector(BaseModel):
    position: str
    theme: str


class ArchLogo(BaseModel):
    foreground: str


class CurrentWindow(BaseModel):
    this_current_screen_border: str


class WindowName(BaseModel):
    foreground: str


class Arrow(BaseModel):
    background: str


class Icon(BaseModel):
    foreground: str


class CheckUpdates(BaseModel):
    foreground: str


class Memory(BaseModel):
    foreground: str


class Layout(BaseModel):
    foreground: str


class Clock(BaseModel):
    foreground: str


class Sep(BaseModel):
    foreground: str


class WidgetUpdate(BaseModel):
    arrow: Arrow
    icon: Icon
    checkupdates: CheckUpdates


class WidgetMemory(BaseModel):
    arrow: Arrow
    icon: Icon
    memory: Memory


class WidgetLayout(BaseModel):
    arrow: Arrow
    layout: Layout


class WidgetClock(BaseModel):
    arrow: Arrow
    icon: Icon
    clock: Clock
    sep: Sep


class Theme(BaseModel):
    bar: str
    arch_logo: ArchLogo
    current_window: CurrentWindow
    window_name: WindowName
    widget_update: WidgetUpdate
    widget_memory: WidgetMemory
    widget_layout: WidgetLayout
    widget_clock: WidgetClock
