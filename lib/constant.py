#coding=utf-8

OKBUTTONPATH="//div[contains(@style,'display:block;') or contains(@style, 'display: block')]//button[contains(text(),'确定')]"
QUERYBUTTONPATH=u"//div[contains(@style,'display:block;') or contains(@style, 'display: block')]//button[contains(text(),'查询')]"

from enum import Enum

class poolType(Enum):
    staticOnly="静态专有"
    staticShare="静态共享"
    dynamicOnly="动态专有"

class poolType2(Enum):
    staticOnly="静态专用桌面"
    staticShare="静态共享桌面"
    dynamicOnly="动态专用桌面"

